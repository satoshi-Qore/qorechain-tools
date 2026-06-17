# Restart Decision Tree

Use this runbook to decide whether, when, and how to restart a QoreChain node.

---

## Step 1: Is the node process running?

```bash
systemctl status YOUR_NODE_SERVICE
```

- **Yes, running** -> Go to Step 2
- **No, stopped** -> Check exit code and logs, then go to Step 3

---

## Step 2: Is the node producing blocks / syncing?

Check sync status via RPC or logs.

- **Yes, syncing normally** -> No restart needed. Monitor.
- **No, stuck** -> Go to Step 3

---

## Step 3: Is there a network-wide halt?

Check community channels (Discord, Telegram, Twitter) for announcements.

- **Yes, chain halt** -> Do NOT restart independently. Wait for official guidance.
- **No, local issue** -> Go to Step 4

---

## Step 4: Check for blocking conditions

- [ ] Disk space: `df -h` -- if full, clear logs before restarting
- [ ] Memory: `free -h` -- if critical, consider rebooting the host
- [ ] Config changes: confirm no recent config edits broke the service

---

## Step 5: Restart the node

```bash
systemctl restart YOUR_NODE_SERVICE
```

Wait 60-120 seconds and verify:

```bash
systemctl status YOUR_NODE_SERVICE
journalctl -u YOUR_NODE_SERVICE -n 50 --no-pager
```

---

## Step 6: Confirm recovery

- [ ] Node is syncing / producing blocks
- [ ] RPC endpoint is responding
- [ ] Monitoring alert resolved

---

## When NOT to restart

- During an active chain halt -- wait for official guidance
- Immediately after an upgrade without reviewing release notes
- If you have not checked disk/memory -- a blind restart may worsen the situation
