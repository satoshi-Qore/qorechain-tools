# Node Health Check Example

This checklist provides a safe, generic flow for reviewing the basic health of a QoreChain-related node or server. It uses placeholder values and does not assume final mainnet behavior.

## Purpose

Use this checklist when you need to confirm whether a node or server appears healthy at a basic operational level.

This document is not official QoreChain documentation. Always compare critical steps with official sources and current network instructions.

## Basic Server Checks

### 1. Confirm server access

```bash
ssh USER@YOUR_SERVER_IP
```

Replace:

- `USER` with your server username
- `YOUR_SERVER_IP` with your server IP address

### 2. Check system uptime

```bash
uptime
```

Look for:

- Server uptime
- Load average
- Whether the server was restarted unexpectedly

### 3. Check disk usage

```bash
df -h
```

Watch for disks that are close to full. A full disk can break logs, databases, containers, and node processes.

### 4. Check memory usage

```bash
free -h
```

If memory usage is consistently high, review running services and logs before restarting anything.

## Container Checks

### 1. List running containers

```bash
docker ps
```

Confirm that the expected QoreChain-related containers are running.

### 2. List all containers

```bash
docker ps -a
```

Use this when a service is missing from the running container list.

### 3. Check recent logs

```bash
docker logs --tail 100 CONTAINER_NAME
```

Replace `CONTAINER_NAME` with the relevant container name.

### 4. Follow live logs

```bash
docker logs -f CONTAINER_NAME
```

Use live logs only when you need to observe current behavior. Stop with `Ctrl+C` when done.

## Network and Port Checks

### 1. Check listening ports

```bash
ss -tulpn
```

Look for expected service ports. If a panel or endpoint does not open, confirm that the related port is listening.

### 2. Test a local endpoint

```bash
curl http://127.0.0.1:PORT
```

Replace `PORT` with the relevant local service port.

### 3. Test a public endpoint

```bash
curl http://YOUR_SERVER_IP:PORT
```

If this fails but the local test works, check firewall rules, provider security groups, and public network access.

## Light Node Panel Check

If your setup includes a web panel, open it with the relevant server IP and port:

```text
http://YOUR_SERVER_IP:8420
```

If the panel does not open, check:

- Server is online
- Container is running
- Correct IP address is used
- Correct port is used
- Firewall allows access
- Logs do not show startup errors

## Safe Restart Notes

Restart only after checking logs and service state.

Generic Docker restart example:

```bash
docker restart CONTAINER_NAME
```

Avoid restarting repeatedly without reading logs. Repeated restarts can hide the original error.

## Health Summary Template

Use this template for your own notes:

```text
Date:
Server IP:
Service checked:
Containers running:
Disk usage:
Memory usage:
Panel reachable:
Recent errors:
Action taken:
Next check:
```

## Common Warning Signs

| Signal | Possible Meaning | First Check |
|---|---|---|
| Container restarting repeatedly | Startup or configuration error | `docker logs --tail 100 CONTAINER_NAME` |
| Panel not reachable | Port, firewall, or service issue | `docker ps` and `ss -tulpn` |
| Disk usage near 100% | Logs or data consuming storage | `df -h` |
| High memory usage | Service load or leak | `free -h` and container logs |
| RPC unreachable | Endpoint, network, or service issue | Local curl test and firewall check |

## Security Reminder

Do not share:

- Private keys
- Seed phrases
- Server passwords
- API keys
- RPC credentials
- Private logs containing sensitive data

Use placeholders when asking for community help.
