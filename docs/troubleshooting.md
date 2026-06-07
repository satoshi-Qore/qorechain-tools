# Troubleshooting Checklist

This checklist provides a general troubleshooting workflow for QoreChain-related node, server, container, and infrastructure experiments.

It is written for community operators and documentation contributors. It does not replace official QoreChain documentation, hosting-provider support, or environment-specific runbooks.

## Purpose

Use this page when a service is not behaving as expected and you need a structured way to collect information before restarting, editing configuration, or asking for help.

The goal is to avoid random changes and make each troubleshooting step clear, reversible, and easy to explain.

## First Checks

Start with basic observations:

- Is the server reachable?
- Is the container or service running?
- Did the issue start after a configuration change?
- Did the issue start after a restart?
- Are there recent error messages in the logs?
- Is the expected port open locally?
- Is disk space available?
- Is system time reasonably accurate?

Record what you see before making changes.

## Service Status

For a Docker-based setup, check running containers:

```bash
docker ps
```

Check all containers, including stopped ones:

```bash
docker ps -a
```

For a system service, use the relevant service name:

```bash
systemctl status SERVICE_NAME
```

Replace `SERVICE_NAME` with the actual service name used in your environment.

## Recent Logs

Check recent logs before restarting anything:

```bash
docker logs --tail 100 CONTAINER_NAME
```

Follow live logs when observing a repeated issue:

```bash
docker logs -f CONTAINER_NAME
```

If using a system service:

```bash
journalctl -u SERVICE_NAME --no-pager -n 100
```

Do not share full logs publicly without reviewing and sanitizing them first.

## Common Signals

| Signal | Possible Meaning | First Action |
|---|---|---|
| Connection timeout | Endpoint, network, or firewall issue | Check RPC endpoint and port access |
| Permission denied | File permission or user mismatch | Check file ownership and command user |
| Container exits repeatedly | Configuration or runtime failure | Review logs before restart loop continues |
| Disk full | Storage exhaustion | Check disk usage and clean safely |
| Unknown chain ID | Configuration mismatch | Verify chain ID from trusted sources |
| Port already in use | Another process is using the same port | Identify the process before changing ports |

These are general signals. Always compare them with the specific service documentation.

## Network Checks

Check whether the server can reach a domain or endpoint:

```bash
ping example.com
```

Check whether a port responds:

```bash
curl -I http://YOUR_RPC_URL
```

Check local listening ports:

```bash
ss -tulpen
```

Use placeholders in public examples instead of real private endpoints.

## Disk and Resource Checks

Check disk usage:

```bash
df -h
```

Check memory usage:

```bash
free -h
```

Check active processes:

```bash
top
```

If disk usage is high, avoid deleting files randomly. Identify large directories first and confirm what is safe to remove.

## Configuration Review

Before editing configuration:

1. Back up the current file.
2. Review the latest change.
3. Confirm endpoint, chain ID, and port values from trusted sources.
4. Avoid using private values in shared examples.
5. Restart only after saving notes about what changed.

Example backup command:

```bash
cp config.toml config.toml.backup
```

## Restart Notes

Before restart, write down:

- Current time
- Service or container name
- Current status
- Last relevant log message
- Configuration file changed
- Restart command used

After restart, write down:

- Whether the service started
- New error messages, if any
- Whether the previous issue changed
- Any next action needed

## Asking for Support

Use this format when asking the community for help:

```text
Environment: VPS / Docker / local machine
Service: SERVICE_NAME or CONTAINER_NAME
Goal: what I am trying to do
Issue: short description
Last change: what changed before the problem started
Checks done: status, logs, ports, disk, config backup
Sanitized log excerpt: relevant lines only
```

Do not include private keys, seed phrases, tokens, private RPC credentials, or full unreviewed logs.

## When to Stop

Stop and ask for help if:

- You are asked to enter a seed phrase or private key.
- A command would delete large directories and you are unsure what they contain.
- You do not understand what a restart, reset, or migration command will do.
- Logs show repeated failures and you are tempted to keep changing random settings.
- The issue relates to funds, staking, delegation, or future mainnet behavior.

## Related Pages

- [Operator Safety Guidelines](./operator-safety.md)
- [Node Health Check Example](../examples/node-health-check.md)
- [Log Checklist Example](../examples/log-checklist.md)
- [RPC Checklist Example](../examples/rpc-checklist.md)

## Disclaimer

This is a community-maintained troubleshooting checklist. Critical steps should be verified against official QoreChain documentation and trusted infrastructure sources.