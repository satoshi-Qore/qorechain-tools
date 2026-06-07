# Scripts

This directory is reserved for reusable QoreChain infrastructure helper scripts.

Scripts should be small, readable, and safe to review before execution. Avoid adding scripts that make irreversible changes without clear warnings and confirmation steps.

## Script Guidelines

- Keep scripts focused on one task.
- Add comments for non-obvious commands.
- Use placeholder values for RPC URLs, ports, wallet addresses, and server IPs.
- Avoid hardcoding private keys, seeds, tokens, or credentials.
- Include a short usage example at the top of each script.
- Prefer read-only checks before restart, delete, or update operations.

## Suggested Script Types

| Script Type | Purpose | Status |
|---|---|---|
| Service checks | Verify whether expected services are running | Planned |
| Log helpers | Show recent logs or filter common errors | Planned |
| RPC checks | Test connectivity to a configured endpoint | Planned |
| Backup helpers | Copy configuration files before changes | Planned |

## Safety Note

Always review scripts before running them on a VPS or node environment. This repository is community-maintained and does not replace official QoreChain documentation.
