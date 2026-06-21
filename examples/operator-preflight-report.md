# Operator Preflight Check Report

This is a sample report showing the expected Markdown output shape for `scripts/operator_preflight_check.py`.

The values below are placeholders. Do not treat them as official hardware requirements, network status, or production readiness evidence.

## Summary

- Overall status: `WARNING`
- Profile: Light Node
- Checked at: 2026-06-21 12:00:00 UTC
- Checked path: `/home/operator/qorechain`

## System Environment

- OS: Linux 6.8.0
- Architecture: x86_64
- Python: 3.11.9

## Checks

| Check | Status | Summary | Details |
|---|---|---|---|
| Docker installed | `PASS` | Docker CLI is available | Docker version 27.0.0, build example |
| Docker Compose available | `PASS` | Docker Compose plugin is available | Docker Compose version v2.28.0 |
| Available disk space | `WARNING` | 14.75 GB available at `/home/operator/qorechain` | Total: 80.00 GB; warning below 20 GB; fail below 10 GB |
| Available memory | `PASS` | 5.80 GB available memory | Total: 8.00 GB; source: POSIX sysconf; warning below 4 GB; fail below 2 GB |

## Not Implemented in v0.1

- RPC checks
- Port checks
- Config file checks

## Safety Note

This prototype is read-only. It does not install packages, start or stop containers, edit configuration files, open ports, or inspect wallet/private key material.

If sharing a real report publicly, review it first and remove sensitive paths, hostnames, server IPs, credentials, tokens, or private infrastructure details.
