# Incident: High Resource Usage

**Severity:** Warning / Critical (depending on threshold)
**Template version:** 1.0

---

## Detection

- [ ] Alert fired: CPU / Memory / Disk above threshold
- [ ] Resource type: CPU / Memory / Disk (circle one)
- [ ] Time detected: YYYY-MM-DD HH:MM UTC
- [ ] Current usage level: ____%

## Initial Assessment (first 5 minutes)

### CPU

```bash
top -bn1 | head -20
ps aux --sort=-%cpu | head -10
```

### Memory

```bash
free -h
ps aux --sort=-%mem | head -10
```

### Disk

```bash
df -h
du -sh /var/log/* | sort -h | tail -10
```

## Diagnosis

**Is the spike sustained or transient?**

- Transient (< 5 minutes) -> Monitor; likely a sync burst or garbage collection
- Sustained -> Investigate root cause

**Common causes by resource:**

| Resource | Common cause |
|---|---|
| CPU | Block sync burst, consensus computation, log spam |
| Memory | Memory leak, large mempool, insufficient swap |
| Disk | Log growth, chain data growth, core dumps |

## Mitigation

- [ ] For disk: rotate logs, remove unnecessary files, expand volume if needed
- [ ] For memory: restart service during low-activity window if safe
- [ ] For CPU: check for runaway processes, consider rate limiting

## Recovery

- [ ] Resource usage returned to normal
- [ ] Root cause identified
- [ ] Monitoring alert resolved

## Post-Incident

- [ ] Filed post-incident report
- [ ] Updated capacity planning notes
- [ ] Added log rotation or cleanup automation if needed
