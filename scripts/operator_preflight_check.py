#!/usr/bin/env python3
"""
Operator Preflight Check v0.1

Read-only environment checks for QoreChain-related operator machines.

Usage:
    python3 scripts/operator_preflight_check.py
    python3 scripts/operator_preflight_check.py --profile light-node
    python3 scripts/operator_preflight_check.py --profile monitoring-node --output reports/preflight.md
    python3 scripts/operator_preflight_check.py --profile validator-preparation --path /var/lib/qorechain
"""

from __future__ import annotations

import argparse
import ctypes
import os
import platform
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

PASS = "PASS"
WARNING = "WARNING"
FAIL = "FAIL"

GB = 1024 ** 3

PROFILE_THRESHOLDS = {
    "light-node": {
        "label": "Light Node",
        "memory_warning_gb": 4,
        "memory_fail_gb": 2,
        "disk_warning_gb": 20,
        "disk_fail_gb": 10,
    },
    "monitoring-node": {
        "label": "Monitoring Node",
        "memory_warning_gb": 4,
        "memory_fail_gb": 2,
        "disk_warning_gb": 15,
        "disk_fail_gb": 5,
    },
    "validator-preparation": {
        "label": "Validator Preparation",
        "memory_warning_gb": 8,
        "memory_fail_gb": 4,
        "disk_warning_gb": 100,
        "disk_fail_gb": 50,
    },
}


@dataclass
class CheckResult:
    name: str
    status: str
    summary: str
    details: str = ""


def run_command(command: list[str]) -> tuple[bool, str]:
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=8,
            check=False,
        )
    except FileNotFoundError:
        return False, "command not found"
    except subprocess.TimeoutExpired:
        return False, "command timed out"
    except OSError as exc:
        return False, str(exc)

    output = (result.stdout or result.stderr or "").strip()
    if result.returncode == 0:
        return True, output
    return False, output or f"exit code {result.returncode}"


def format_gb(value: float | None) -> str:
    if value is None:
        return "unknown"
    return f"{value:.2f} GB"


def get_memory_info() -> tuple[float | None, float | None, str]:
    system = platform.system().lower()

    if system == "windows":
        class MemoryStatus(ctypes.Structure):
            _fields_ = [
                ("dwLength", ctypes.c_ulong),
                ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong),
                ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong),
                ("ullAvailVirtual", ctypes.c_ulonglong),
                ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]

        status = MemoryStatus()
        status.dwLength = ctypes.sizeof(MemoryStatus)
        try:
            kernel32 = ctypes.windll.kernel32
            if kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
                return status.ullTotalPhys / GB, status.ullAvailPhys / GB, "Windows GlobalMemoryStatusEx"
        except (AttributeError, OSError) as exc:
            return None, None, f"Windows memory API unavailable: {exc}"
        return None, None, "Windows memory API unavailable"

    if hasattr(os, "sysconf"):
        try:
            page_size = os.sysconf("SC_PAGE_SIZE")
            total_pages = os.sysconf("SC_PHYS_PAGES")
            available_pages = os.sysconf("SC_AVPHYS_PAGES")
            return (total_pages * page_size) / GB, (available_pages * page_size) / GB, "POSIX sysconf"
        except (ValueError, OSError, AttributeError):
            pass

    return None, None, "memory check not supported on this platform"


def evaluate_threshold(value: float | None, warning: float, fail: float) -> str:
    if value is None:
        return WARNING
    if value < fail:
        return FAIL
    if value < warning:
        return WARNING
    return PASS


def check_docker() -> CheckResult:
    docker_path = shutil.which("docker")
    if not docker_path:
        return CheckResult("Docker installed", FAIL, "Docker CLI was not found in PATH")

    ok, output = run_command([docker_path, "--version"])
    if ok:
        return CheckResult("Docker installed", PASS, "Docker CLI is available", output)
    return CheckResult("Docker installed", WARNING, "Docker CLI was found but did not respond as expected", output)


def check_docker_compose() -> CheckResult:
    docker_path = shutil.which("docker")
    if docker_path:
        ok, output = run_command([docker_path, "compose", "version"])
        if ok:
            return CheckResult("Docker Compose available", PASS, "Docker Compose plugin is available", output)

    compose_path = shutil.which("docker-compose")
    if compose_path:
        ok, output = run_command([compose_path, "--version"])
        if ok:
            return CheckResult("Docker Compose available", PASS, "Legacy docker-compose is available", output)
        return CheckResult("Docker Compose available", WARNING, "docker-compose was found but did not respond as expected", output)

    return CheckResult("Docker Compose available", FAIL, "Neither 'docker compose' nor 'docker-compose' is available")


def check_disk(path: Path, thresholds: dict[str, float]) -> CheckResult:
    try:
        usage = shutil.disk_usage(path)
    except OSError as exc:
        return CheckResult("Available disk space", FAIL, f"Could not read disk usage for {path}", str(exc))

    total_gb = usage.total / GB
    free_gb = usage.free / GB
    status = evaluate_threshold(free_gb, thresholds["disk_warning_gb"], thresholds["disk_fail_gb"])
    summary = f"{format_gb(free_gb)} available at {path}"
    details = (
        f"Total: {format_gb(total_gb)}; "
        f"warning below {thresholds['disk_warning_gb']} GB; "
        f"fail below {thresholds['disk_fail_gb']} GB"
    )
    return CheckResult("Available disk space", status, summary, details)


def check_memory(thresholds: dict[str, float]) -> CheckResult:
    total_gb, available_gb, source = get_memory_info()
    status = evaluate_threshold(available_gb, thresholds["memory_warning_gb"], thresholds["memory_fail_gb"])
    summary = f"{format_gb(available_gb)} available memory"
    details = (
        f"Total: {format_gb(total_gb)}; "
        f"source: {source}; "
        f"warning below {thresholds['memory_warning_gb']} GB; "
        f"fail below {thresholds['memory_fail_gb']} GB"
    )
    return CheckResult("Available memory", status, summary, details)


def overall_status(results: list[CheckResult]) -> str:
    if any(result.status == FAIL for result in results):
        return FAIL
    if any(result.status == WARNING for result in results):
        return WARNING
    return PASS


def build_markdown_report(profile: str, path: Path, results: list[CheckResult]) -> str:
    thresholds = PROFILE_THRESHOLDS[profile]
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    status = overall_status(results)

    lines = [
        "# Operator Preflight Check Report",
        "",
        "## Summary",
        "",
        f"- Overall status: `{status}`",
        f"- Profile: {thresholds['label']}",
        f"- Checked at: {generated_at}",
        f"- Checked path: `{path}`",
        "",
        "## System Environment",
        "",
        f"- OS: {platform.system()} {platform.release()}",
        f"- Architecture: {platform.machine()}",
        f"- Python: {platform.python_version()}",
        "",
        "## Checks",
        "",
        "| Check | Status | Summary | Details |",
        "|---|---|---|---|",
    ]

    for result in results:
        details = result.details.replace("|", "\\|") if result.details else "-"
        summary = result.summary.replace("|", "\\|")
        lines.append(f"| {result.name} | `{result.status}` | {summary} | {details} |")

    lines.extend([
        "",
        "## Not Implemented in v0.1",
        "",
        "- RPC checks",
        "- Port checks",
        "- Config file checks",
        "",
        "## Safety Note",
        "",
        "This prototype is read-only. It does not install packages, start or stop containers, edit configuration files, open ports, or inspect wallet/private key material.",
        "",
    ])

    return "\n".join(lines)


def print_terminal_summary(profile: str, path: Path, results: list[CheckResult]) -> None:
    thresholds = PROFILE_THRESHOLDS[profile]
    print("Operator Preflight Check v0.1")
    print(f"Profile: {thresholds['label']}")
    print(f"Path: {path}")
    print(f"Overall status: {overall_status(results)}")
    print("")
    for result in results:
        print(f"[{result.status}] {result.name}: {result.summary}")
        if result.details:
            print(f"  {result.details}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run read-only operator preflight checks.")
    parser.add_argument(
        "--profile",
        choices=sorted(PROFILE_THRESHOLDS),
        default="light-node",
        help="Preflight profile to evaluate. Default: light-node.",
    )
    parser.add_argument(
        "--path",
        default=".",
        help="Path used for disk-space checks. Default: current directory.",
    )
    parser.add_argument(
        "--output",
        help="Optional path for writing the Markdown report.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    thresholds = PROFILE_THRESHOLDS[args.profile]
    check_path = Path(args.path).expanduser().resolve()

    results = [
        check_docker(),
        check_docker_compose(),
        check_disk(check_path, thresholds),
        check_memory(thresholds),
    ]

    print_terminal_summary(args.profile, check_path, results)

    markdown_report = build_markdown_report(args.profile, check_path, results)
    if args.output:
        try:
            output_path = Path(args.output).expanduser().resolve()
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(markdown_report, encoding="utf-8")
        except OSError as exc:
            print("", file=sys.stderr)
            print(f"Could not write Markdown report: {exc}", file=sys.stderr)
            return 1
        print("")
        print(f"Markdown report written to: {output_path}")
    else:
        print("")
        print("Markdown report:")
        print("")
        print(markdown_report)

    return 1 if overall_status(results) == FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
