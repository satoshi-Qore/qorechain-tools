# Incident: Node Down

**Severity:** Critical
**Template version:** 1.0

---

## Detection

- [ ] Alert fired: node exporter unreachable / block production stopped
- [ ] Confirmed via: RPC health check / monitoring dashboard / community report
- [ ] Time detected: YYYY-MM-DD HH:MM UTC

## Initial Response (first 5 minutes)

- [ ] Check if the VPS/server is reachable via SSH
- [ ] Check system logs: `journalctl -u YOUR_NODE_SERVICE -n 100 --no-pager`
- [ ] Check disk space: `df -h`
- [ ] Check memory: `free -h`
- [ ] Check running processes: `ps aux | grep YOUR_NODE_BINARY`

## Diagnosis

**Is the host reachable?**

- Yes -> Continue to service diagnosis
- No -> Contact VPS provider / check for host-level outage

**Is the service running?**

```bash
systemctl status YOUR_NODE_SERVICE
```

- Running but not producing blocks -> check peer connections and sync status
- Stopped -> check exit code and logs, then decide whether to restart

**Common causes:**

| Symptom | Likely cause |
|---|---|
| OOM killed | Insufficient memory |
| Disk full | Log or data growth |
| Port conflict | Service config issue |
| Chain halt | Network-level event |

## Recovery

- [ ] Restarted service: `systemctl restart YOUR_NODE_SERVICE`
- [ ] Confirmed node is syncing
- [ ] Confirmed RPC endpoint is responding
- [ ] Monitoring alert resolved

## Post-Incident

- [ ] Filed post-incident report (see [examples/post-incident-report.md](../../examples/post-incident-report.md))
- [ ] Updated runbooks if a new failure mode was discovered
- [ ] Notified relevant community channels if public impact occurred
