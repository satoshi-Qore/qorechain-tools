#!/usr/bin/env python3
"""
QoreChain RPC Health Monitor

Reads endpoint definitions from a JSON file, performs simple JSON-RPC
reachability checks, and writes a Markdown health report.
"""

from __future__ import annotations

import argparse
import json
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib import error, request
from urllib.parse import urlparse


@dataclass
class CheckResult:
    name: str
    url: str
    method: str
    ok: bool
    latency_ms: int | None
    http_status: int | None
    note: str


def load_config(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    endpoints = data.get("endpoints")
    if not isinstance(endpoints, list):
        raise ValueError("Configuration must contain an 'endpoints' list.")

    return endpoints


def sanitize_url_for_report(url: str) -> str:
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return "invalid-url"
    return f"{parsed.scheme}://{parsed.netloc}"


def check_endpoint(endpoint: dict[str, Any]) -> CheckResult:
    name = str(endpoint.get("name", "Unnamed endpoint"))
    url = str(endpoint.get("url", ""))
    method = str(endpoint.get("method", "status"))
    timeout_seconds = int(endpoint.get("timeout_seconds", 10))

    if "YOUR_RPC_URL" in url:
        return CheckResult(
            name=name,
            url=url,
            method=method,
            ok=False,
            latency_ms=None,
            http_status=None,
            note="Placeholder URL. Replace before real checks.",
        )

    payload = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": [],
        }
    ).encode("utf-8")

    rpc_request = request.Request(
        url=url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    started_at = time.perf_counter()
    try:
        with request.urlopen(rpc_request, timeout=timeout_seconds) as response:
            body = response.read().decode("utf-8", errors="replace")
            latency_ms = int((time.perf_counter() - started_at) * 1000)
            status_code = response.status

        try:
            parsed_body = json.loads(body)
        except json.JSONDecodeError:
            return CheckResult(
                name=name,
                url=url,
                method=method,
                ok=False,
                latency_ms=latency_ms,
                http_status=status_code,
                note="HTTP response received, but body is not valid JSON.",
            )

        if "result" in parsed_body:
            note = "JSON-RPC response includes result."
            ok = True
        elif "error" in parsed_body:
            note = "JSON-RPC response includes error."
            ok = False
        else:
            note = "JSON response received, but no result or error field found."
            ok = False

        return CheckResult(
            name=name,
            url=url,
            method=method,
            ok=ok,
            latency_ms=latency_ms,
            http_status=status_code,
            note=note,
        )

    except error.HTTPError as exc:
        latency_ms = int((time.perf_counter() - started_at) * 1000)
        return CheckResult(
            name=name,
            url=url,
            method=method,
            ok=False,
            latency_ms=latency_ms,
            http_status=exc.code,
            note=f"HTTP error: {exc.reason}",
        )
    except error.URLError as exc:
        latency_ms = int((time.perf_counter() - started_at) * 1000)
        return CheckResult(
            name=name,
            url=url,
            method=method,
            ok=False,
            latency_ms=latency_ms,
            http_status=None,
            note=f"Connection error: {exc.reason}",
        )
    except TimeoutError:
        latency_ms = int((time.perf_counter() - started_at) * 1000)
        return CheckResult(
            name=name,
            url=url,
            method=method,
            ok=False,
            latency_ms=latency_ms,
            http_status=None,
            note="Request timed out.",
        )


def render_markdown_report(results: list[CheckResult]) -> str:
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        "# RPC Health Report",
        "",
        f"Generated at: {generated_at}",
        "",
        "| Endpoint | Host | Method | Status | Latency | HTTP | Notes |",
        "|---|---|---|---|---|---|---|",
    ]

    for result in results:
        status = "OK" if result.ok else "Check"
        latency = f"{result.latency_ms} ms" if result.latency_ms is not None else "-"
        http_status = str(result.http_status) if result.http_status is not None else "-"
        host = sanitize_url_for_report(result.url)
        lines.append(
            f"| {result.name} | {host} | `{result.method}` | {status} | {latency} | {http_status} | {result.note} |"
        )

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- This report only checks whether configured endpoints respond to simple JSON-RPC requests.",
            "- It does not verify official network status or final chain correctness.",
            "- Review endpoints before publishing reports publicly.",
        ]
    )

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Check RPC endpoint health and generate a Markdown report.")
    parser.add_argument("config", help="Path to endpoint configuration JSON file.")
    parser.add_argument("--output", help="Optional path for the Markdown report.")
    args = parser.parse_args()

    endpoints = load_config(Path(args.config))
    results = [check_endpoint(endpoint) for endpoint in endpoints]
    report = render_markdown_report(results)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report, encoding="utf-8")
    else:
        print(report)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
