# Scripts

This directory contains reusable QoreChain infrastructure helper scripts.

Scripts should be small, readable, and safe to review before execution. Avoid adding scripts that make irreversible changes without clear warnings and confirmation steps.

## Available Scripts

| Script | Purpose | Safety Profile |
|---|---|---|
| [health-check.sh](./health-check.sh) | Collect basic system, disk, memory, port, Docker, and optional container log information | Read-only |
| [operator_preflight_check.py](./operator_preflight_check.py) | Check Docker, Docker Compose, disk space, and memory before setup or troubleshooting | Read-only; optional report export |
| [rpc_health_monitor.py](./rpc_health_monitor.py) | Check configured JSON-RPC endpoints and generate Markdown health reports | Read-only |

## Script Guidelines

- Keep scripts focused on one task.
- Add comments for non-obvious commands.
- Use placeholder values for RPC URLs, ports, wallet addresses, and server IPs.
- Avoid hardcoding private keys, seeds, tokens, or credentials.
- Include a short usage example at the top of each script.
- Prefer read-only checks before restart, delete, or update operations.

## Usage Examples

Run the basic read-only health check:

```bash
bash scripts/health-check.sh
```

Include recent logs for one container:

```bash
bash scripts/health-check.sh CONTAINER_NAME
```

Run the operator preflight check:

```bash
python3 scripts/operator_preflight_check.py
```

Run a specific operator preflight profile:

```bash
python3 scripts/operator_preflight_check.py --profile light-node
python3 scripts/operator_preflight_check.py --profile monitoring-node
python3 scripts/operator_preflight_check.py --profile validator-preparation
```

Save an operator preflight report to a file:

```bash
python3 scripts/operator_preflight_check.py --output reports/preflight.md
```

Run the RPC health monitor with a local endpoint configuration:

```bash
python3 scripts/rpc_health_monitor.py endpoints.local.json
```

Save an RPC health report to a file:

```bash
python3 scripts/rpc_health_monitor.py endpoints.local.json --output reports/latest-report.md
```

Replace `CONTAINER_NAME` and `endpoints.local.json` with values appropriate for your environment.

## Script Categories

| Script Type | Purpose | Status |
|---|---|---|
| Service checks | Verify whether expected services are running | Started |
| Preflight checks | Check operator environment readiness before setup or troubleshooting | Available |
| Log helpers | Show recent logs or filter common errors | Started |
| RPC checks | Test connectivity to configured JSON-RPC endpoints | Available |
| Backup helpers | Copy configuration files before changes | Planned |

## Safety Note

Always review scripts before running them on a VPS or node environment. This repository is community-maintained and does not replace official QoreChain documentation.

Do not share script output publicly before removing private keys, seed phrases, server IPs, credentials, tokens, and sensitive log lines.
