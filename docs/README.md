# Documentation

This directory contains operational notes for QoreChain-related infrastructure workflows.

The goal is to collect practical, repeatable, and reviewable documentation for community operators without making unsupported assumptions about mainnet behavior or future reward mechanics.

## Available Topics

| Topic | Description | Status |
|---|---|---|
| [RPC Configuration](./rpc-configuration.md) | Configuration guidance for the RPC health monitor and endpoint files | Available |
| [Monitoring Checklist](./monitoring-checklist.md) | Review checklist before deploying or sharing monitoring configuration | Available |
| [Operator Safety Guidelines](./operator-safety.md) | Safe handling of logs, configuration files, credentials, support requests, and public examples | Available |
| [Troubleshooting Checklist](./troubleshooting.md) | Structured checks for service status, logs, network, disk, configuration, and support requests | Available |

## Incident Guides

| Guide | Purpose | Status |
|---|---|---|
| [Node Down](./incidents/node-down.md) | Response steps for node downtime or unreachable services | Available |
| [High Resource Usage](./incidents/high-resource.md) | Response steps for high CPU, memory, disk, or resource pressure | Available |

## Runbooks

| Runbook | Purpose | Status |
|---|---|---|
| [Restart Decision Tree](./runbooks/restart-decision-tree.md) | Helps decide when a restart is appropriate and what to check first | Available |
| [Upgrade Checklist](./runbooks/upgrade-checklist.md) | Safe upgrade preparation and review checklist | Available |

## Writing Style

- Keep steps short and verifiable.
- Separate confirmed facts from assumptions.
- Use placeholders instead of real private information.
- Point users back to official sources for critical or changing details.
- Prefer tables, checklists, and examples over long explanations.

## Disclaimer

These notes are community-maintained and should be treated as practical learning material. Official QoreChain documentation and announcements should be checked for critical steps.
