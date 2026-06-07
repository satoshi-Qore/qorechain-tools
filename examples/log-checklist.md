# Log Checklist Example

This checklist provides a safe, generic workflow for reviewing logs from a QoreChain-related node, container, or infrastructure service.

It is intended for community operators and does not replace official QoreChain documentation or environment-specific runbooks.

## Purpose

Use this checklist when you need to:

- Check recent service logs
- Follow live logs during troubleshooting
- Search for common error signals
- Save useful notes before restarting a service
- Share sanitized logs with the community or maintainers

## Basic Docker Log Commands

### 1. Show recent logs

```bash
docker logs --tail 100 CONTAINER_NAME
```

Use this for a quick look at the most recent activity.

### 2. Follow live logs

```bash
docker logs -f CONTAINER_NAME
```

Use this when you need to observe live behavior. Stop with `Ctrl+C`.

### 3. Show logs with timestamps

```bash
docker logs --timestamps --tail 100 CONTAINER_NAME
```

Timestamps make it easier to compare service behavior with restart times, network changes, or task submissions.

### 4. Save logs to a local file

```bash
docker logs --tail 300 CONTAINER_NAME > node-logs.txt
```

Review the file before sharing. Remove private data first.

## Searching Logs

### Search for errors

```bash
docker logs --tail 500 CONTAINER_NAME 2>&1 | grep -i "error"
```

### Search for warnings

```bash
docker logs --tail 500 CONTAINER_NAME 2>&1 | grep -i "warn"
```

### Search for connection issues

```bash
docker logs --tail 500 CONTAINER_NAME 2>&1 | grep -i "connection"
```

If `grep` is not available on your system, use the search function in your terminal or text editor after saving logs to a file.

## Before Restarting

Before restarting a container or service, capture basic evidence:

```text
Time of issue:
Container name:
Last successful state:
Recent error message:
Last action before issue:
```

Then check logs:

```bash
docker logs --tail 200 CONTAINER_NAME
```

Restart only after reviewing the most recent error context.

## Generic Restart Command

```bash
docker restart CONTAINER_NAME
```

Avoid repeated restarts without checking logs. Repeated restarts can hide the original problem.

## Sanitizing Logs Before Sharing

Before posting logs publicly, remove:

- Private keys
- Seed phrases
- Wallet private data
- API keys
- RPC credentials
- Server passwords
- Personal access tokens
- Private server paths if sensitive
- IP addresses you do not want public

Use placeholders instead:

```text
YOUR_SERVER_IP
YOUR_WALLET_ADDRESS
YOUR_RPC_URL
YOUR_API_KEY
```

## Incident Note Template

```text
Date:
Service/container:
Server environment:
What I expected:
What happened:
Recent command used:
Relevant sanitized log lines:
Action already tried:
Current status:
```

## Common Log Signals

| Log Signal | Possible Meaning | First Action |
|---|---|---|
| `connection refused` | Endpoint or service is not reachable | Check service status and port |
| `timeout` | Network delay or unavailable endpoint | Check RPC, network, and firewall |
| `permission denied` | File or process permission issue | Review user, file ownership, and paths |
| `no space left on device` | Disk is full | Check `df -h` and clean safely |
| `restart loop` | Service fails during startup | Review first error after container start |
| `invalid config` | Configuration issue | Compare config with official examples |

## Safe Sharing Example

```text
I am checking a QoreChain-related node service. The container starts but the panel does not open.

Sanitized logs:
[PASTE SHORT LOG EXCERPT]

Already checked:
- docker ps
- docker logs --tail 100 CONTAINER_NAME
- firewall / port access
```

## Notes

Keep log excerpts short and relevant. Do not paste long logs unless specifically requested by a maintainer or support channel.
