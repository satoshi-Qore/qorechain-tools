# QoreChain Tools

QoreChain node tools, scripts, monitoring stack, and operator playbooks for community operators, light node users, and infrastructure maintainers.

## Overview

This repository collects practical utilities for working with QoreChain infrastructure. It covers node health checks, RPC monitoring, Prometheus/Grafana monitoring, incident response, and upgrade procedures.

The repository is intentionally conservative: examples use placeholders, avoid private data, and do not assume final mainnet behavior.

## Focus Areas

- Light node setup support
- RPC endpoint health monitoring
- Prometheus + Grafana monitoring stack
- Incident response and runbooks
- Node operation and upgrade procedures
- Community-maintained QoreChain resources

## Repository Structure

```text
scripts/           Python scripts and shell helpers
docs/              Operational documentation, incidents, and runbooks
examples/          Example configs, reports, and templates
monitoring/        Docker Compose monitoring stack (Prometheus + Grafana)
.github/workflows/ GitHub Actions workflows
CONTRIBUTING.md    Contribution guidelines
SECURITY.md        Security and sensitive-data policy
LICENSE            MIT License
README.md          This file
```

## Operator Preflight Check

A minimal read-only Python utility for checking whether an operator environment appears ready before setup, troubleshooting, or support requests.

The v0.1 prototype checks:

- Docker availability
- Docker Compose availability
- Available disk space
- Available memory

It does not perform RPC checks, port checks, or config file checks yet.

```bash
python3 scripts/operator_preflight_check.py
python3 scripts/operator_preflight_check.py --profile light-node
python3 scripts/operator_preflight_check.py --profile monitoring-node --output reports/preflight.md
python3 scripts/operator_preflight_check.py --profile validator-preparation --path /var/lib/qorechain
```

Using `--output` writes only the generated Markdown report file; it does not change node, Docker, or system configuration.

See [docs/operator-preflight-check-spec.md](./docs/operator-preflight-check-spec.md) for the full design specification.

## RPC Health Monitor

A Python CLI tool that checks JSON-RPC endpoint availability and generates Markdown reports.

```bash
# Copy and configure endpoints
cp examples/endpoints.example.json endpoints.local.json
# Edit endpoints.local.json with your RPC URLs

# Run health check
python3 scripts/rpc_health_monitor.py endpoints.local.json

# Save report to file
python3 scripts/rpc_health_monitor.py endpoints.local.json --output reports/latest-report.md
```

See [docs/rpc-configuration.md](./docs/rpc-configuration.md) for full configuration reference.

## Monitoring Stack (Prometheus + Grafana)

```bash
cd monitoring/

# Configure Prometheus
cp prometheus/prometheus.example.yml prometheus/prometheus.yml
# Edit prometheus.yml — replace YOUR_NODE_IP and YOUR_CHAIN_ID

# Start the stack
docker compose up -d

# View dashboards at http://127.0.0.1:3000 (admin/admin — change on first login)
# Prometheus at http://127.0.0.1:9090
```

Before deploying, review [docs/monitoring-checklist.md](./docs/monitoring-checklist.md).

## Incident Response

| Document | Purpose |
|---|---|
| [docs/incidents/node-down.md](./docs/incidents/node-down.md) | Node down response steps |
| [docs/incidents/high-resource.md](./docs/incidents/high-resource.md) | High CPU/memory/disk response |
| [docs/runbooks/restart-decision-tree.md](./docs/runbooks/restart-decision-tree.md) | When and how to restart a node |
| [docs/runbooks/upgrade-checklist.md](./docs/runbooks/upgrade-checklist.md) | Safe upgrade procedure |
| [examples/post-incident-report.md](./examples/post-incident-report.md) | Post-incident report template |

## All Resources

| Resource | Purpose |
|---|---|
| [scripts/rpc_health_monitor.py](./scripts/rpc_health_monitor.py) | RPC endpoint health check CLI |
| [scripts/operator_preflight_check.py](./scripts/operator_preflight_check.py) | Read-only operator environment preflight check prototype |
| [scripts/health-check.sh](./scripts/health-check.sh) | Read-only system and Docker health check |
| [docs/operator-preflight-check-spec.md](./docs/operator-preflight-check-spec.md) | Operator preflight check design specification |
| [docs/rpc-configuration.md](./docs/rpc-configuration.md) | RPC monitor configuration guide |
| [docs/monitoring-checklist.md](./docs/monitoring-checklist.md) | Monitoring deployment checklist |
| [docs/operator-safety.md](./docs/operator-safety.md) | Safe log and credential handling |
| [docs/troubleshooting.md](./docs/troubleshooting.md) | Structured troubleshooting guide |
| [docs/incidents/node-down.md](./docs/incidents/node-down.md) | Node down incident guide |
| [docs/incidents/high-resource.md](./docs/incidents/high-resource.md) | High resource incident guide |
| [docs/runbooks/restart-decision-tree.md](./docs/runbooks/restart-decision-tree.md) | Restart decision runbook |
| [docs/runbooks/upgrade-checklist.md](./docs/runbooks/upgrade-checklist.md) | Upgrade checklist runbook |
| [monitoring/docker-compose.yml](./monitoring/docker-compose.yml) | Prometheus + Grafana stack |
| [monitoring/prometheus/prometheus.example.yml](./monitoring/prometheus/prometheus.example.yml) | Prometheus config example |
| [monitoring/alerts/example-rules.yml](./monitoring/alerts/example-rules.yml) | Example alert rules |
| [examples/endpoints.example.json](./examples/endpoints.example.json) | RPC endpoint config example |
| [examples/sample-rpc-report.md](./examples/sample-rpc-report.md) | Sample RPC health report |
| [examples/operator-preflight-report.md](./examples/operator-preflight-report.md) | Sample operator preflight report |
| [examples/post-incident-report.md](./examples/post-incident-report.md) | Post-incident report template |
| [examples/operator-daily-check.md](./examples/operator-daily-check.md) | Daily operator checklist |
| [examples/support-request-template.md](./examples/support-request-template.md) | Support request template |
| [examples/rpc-checklist.md](./examples/rpc-checklist.md) | RPC configuration checklist |
| [examples/node-health-check.md](./examples/node-health-check.md) | Node health check flow |
| [examples/log-checklist.md](./examples/log-checklist.md) | Log review checklist |

## Usage

```bash
git clone https://github.com/satoshi-Qore/qorechain-tools.git
cd qorechain-tools
```

Run the operator preflight check:

```bash
python3 scripts/operator_preflight_check.py
```

Run a specific preflight profile:

```bash
python3 scripts/operator_preflight_check.py --profile light-node
python3 scripts/operator_preflight_check.py --profile monitoring-node
python3 scripts/operator_preflight_check.py --profile validator-preparation
```

Save a Markdown preflight report:

```bash
python3 scripts/operator_preflight_check.py --output reports/preflight.md
```

Always replace placeholder values (`YOUR_RPC_URL`, `YOUR_CHAIN_ID`, `YOUR_NODE_IP`) with verified values before use.

## Related Projects

- [QoreChain Guides](https://github.com/satoshi-Qore/qorechain-guides)
- [QoreChain Light Node](https://github.com/satoshi-Qore/qorechain-lightnode)
- [QoreChain Notes](https://github.com/satoshi-Qore/Qorechain-notes)
- [QoreChain Academic Paper](https://github.com/satoshi-Qore/qorechain-academic-paper)

## Contribution

See [CONTRIBUTING.md](./CONTRIBUTING.md) and [SECURITY.md](./SECURITY.md).
