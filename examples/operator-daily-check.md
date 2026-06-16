# Operator Daily Check Example

This example provides a short daily review flow for QoreChain-related node and infrastructure operators.

It is intentionally conservative. The goal is to observe system state, record useful notes, and avoid unnecessary changes before there is a clear reason to act.

## When to Use

Use this checklist when you want to perform a routine check of a VPS, light node, container-based setup, or related infrastructure environment.

This is not official QoreChain documentation. Always verify critical commands, network values, RPC endpoints, and mainnet-related details through official sources.

## Daily Review Flow

### 1. Confirm server access

```bash
ssh USER@YOUR_SERVER_IP
```

Record whether login works normally. Do not share server IPs, usernames, or access details publicly unless you intentionally use placeholders.

### 2. Check system uptime

```bash
uptime
```

Look for:

- unexpected reboot;
- unusually high load average;
- system behavior that changed since the last check.

### 3. Check disk space

```bash
df -h
```

Watch for disks that are close to full. A full disk can affect logs, databases, containers, and node processes.

### 4. Check memory usage

```bash
free -h
```

If memory usage is unusually high, review logs and running containers before restarting anything.

### 5. Check containers

```bash
docker ps
```

Then check stopped containers if something is missing:

```bash
docker ps -a
```

Record container names, status, restart count, and any unexpected exits.

### 6. Review recent logs

```bash
docker logs --tail 100 CONTAINER_NAME
```

Look for repeated errors, connection failures, configuration warnings, or restart loops.

Do not share full logs publicly without removing sensitive data.

### 7. Check listening ports

```bash
ss -tulpn
```

Use this when a panel, RPC endpoint, or service port does not appear reachable.

### 8. Run the read-only helper script

From the repository root:

```bash
bash scripts/health-check.sh
```

To include recent logs for one container:

```bash
bash scripts/health-check.sh CONTAINER_NAME
```

The script is read-only. It does not restart, delete, update, or modify files.

## Daily Notes Template

```text
Date:
Server:
Service or container checked:
Uptime:
Disk status:
Memory status:
Containers running:
Panel reachable:
Recent warnings or errors:
Action taken:
Next check:
```

## Warning Signs

| Signal | First Check | Avoid |
|---|---|---|
| Container restarting repeatedly | `docker logs --tail 100 CONTAINER_NAME` | Restarting repeatedly without reading logs |
| Disk almost full | `df -h` | Randomly deleting unknown files |
| Panel not reachable | `docker ps` and `ss -tulpn` | Changing ports before confirming service state |
| RPC connection fails | Endpoint, network, and firewall checks | Assuming the endpoint is correct without verification |
| High memory usage | `free -h` and logs | Killing processes without understanding impact |

## Sharing a Support Request

Use this short format when asking for help:

```text
Environment: VPS / Docker / local machine
Goal: what I am trying to check
Service: service or container name
Issue: short description
Checks completed: uptime, disk, memory, containers, logs, ports
Sanitized log excerpt: relevant lines only
```

## Security Reminder

Never share:

- private keys;
- seed phrases;
- server passwords;
- API keys;
- RPC credentials;
- private logs containing sensitive data;
- wallet files or personal documents.

Use placeholders such as `YOUR_SERVER_IP`, `YOUR_RPC_URL`, `YOUR_CHAIN_ID`, and `CONTAINER_NAME` in public examples.
