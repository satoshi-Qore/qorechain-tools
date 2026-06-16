# Examples

This directory contains example commands, checklists, and configuration snippets for QoreChain-related infrastructure work.

Examples should be safe, generic, and easy to adapt. They should not include private keys, seed phrases, personal wallet addresses, or production credentials.

## Available Examples

| Example | Purpose |
|---|---|
| [Operator Daily Check](./operator-daily-check.md) | Daily VPS, container, panel, log, and support-request review flow for operators |
| [Support Request Template](./support-request-template.md) | Structured template for asking for help while protecting sensitive information |
| [RPC Checklist](./rpc-checklist.md) | Basic checklist for reviewing RPC endpoint and network configuration |
| [Node Health Check](./node-health-check.md) | Generic server, container, port, log, and panel health-check flow |
| [Log Checklist](./log-checklist.md) | Generic log review, error search, restart preparation, and sanitized sharing flow |

## Example Rules

- Use placeholder values such as `YOUR_SERVER_IP`, `YOUR_RPC_URL`, or `YOUR_CHAIN_ID`.
- Avoid claiming that a command is universal for every environment.
- Add notes when behavior may depend on official documentation or current network status.
- Keep examples educational and reviewable.
- Prefer read-only checks before restart, delete, update, or migration steps.

## Recommended Starting Point

New operators should start with [Operator Daily Check](./operator-daily-check.md), then use [Support Request Template](./support-request-template.md) before asking for help publicly.

## Disclaimer

Examples are community-maintained and should be tested carefully before use in real infrastructure environments.