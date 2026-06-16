# Support Request Template

Use this template when asking for help with a QoreChain-related node, VPS, Docker container, panel, RPC, or infrastructure issue.

The goal is to provide enough context for others to understand the problem while keeping sensitive information private.

## Before Asking for Help

Run read-only checks first:

```bash
uptime
df -h
free -h
docker ps
docker ps -a
```

If you use this repository, you can also run:

```bash
bash scripts/health-check.sh
```

To include recent logs for one container:

```bash
bash scripts/health-check.sh CONTAINER_NAME
```

Review the output before sharing it.

## Short Support Request Format

```text
Environment: VPS / local machine / Docker / other
Goal: what I am trying to do
Issue: short description of what is not working
When it started: approximate time or after which change
Service or container name: CONTAINER_NAME
Checks completed: uptime, disk, memory, Docker status, logs, ports
Relevant command used: command or checklist followed
Sanitized log excerpt: only the relevant lines
Expected result: what I expected to happen
Actual result: what happened instead
```

## Node or Container Issue

```text
Environment: VPS with Docker
Container name: CONTAINER_NAME
Status from docker ps: running / restarting / exited
Recent log excerpt:
[replace with sanitized log lines]
Disk status: normal / high usage / full
Memory status: normal / high usage
Recent change made: none / config update / restart / system update
Question: what I need help understanding
```

## RPC or Network Configuration Issue

```text
Goal: connect to an RPC endpoint or network configuration
RPC endpoint used: YOUR_RPC_URL
Chain ID used: YOUR_CHAIN_ID
Source of the values: official docs / community guide / other
Error message:
[replace with sanitized error]
Checks completed: endpoint, chain ID, firewall, container status, logs
Question: what I need help verifying
```

## Panel or Dashboard Issue

```text
Goal: access or verify a node panel
Panel URL or port: use placeholder if public sharing is not safe
Service status: running / not running / unknown
Port check result: listening / not listening / blocked
Browser behavior: loads / blank page / connection refused / timeout
Recent logs:
[replace with sanitized log lines]
Question: what I need help checking next
```

## What to Remove Before Sharing

Never share:

- private keys;
- seed phrases;
- server passwords;
- API keys;
- access tokens;
- private RPC credentials;
- wallet files;
- full IP addresses if you do not want them public;
- personal documents or screenshots with unrelated private data.

Use placeholders instead:

```text
YOUR_SERVER_IP
YOUR_RPC_URL
YOUR_CHAIN_ID
CONTAINER_NAME
WALLET_ADDRESS_PLACEHOLDER
```

## Good Support Request Example

```text
Environment: VPS with Docker
Goal: check whether my light node container is running normally
Issue: the dashboard does not load in my browser
When it started: after a server reboot
Container name: qore-lightnode
Checks completed: uptime, df -h, free -h, docker ps, docker logs --tail 100, ss -tulpn
Port check result: expected port is not listening
Sanitized log excerpt: service failed to bind to configured port
Question: should I check the container configuration, firewall, or port mapping first?
```

## Poor Support Request Example

```text
It does not work. Help.
```

This does not provide enough information for others to help safely.

## Reminder

This repository is community-maintained and does not replace official QoreChain documentation. Verify critical commands, RPC endpoints, chain IDs, and mainnet-related details through official sources before making changes.