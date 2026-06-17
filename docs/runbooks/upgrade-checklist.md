# Upgrade Checklist

Use this checklist before and after upgrading a QoreChain node binary or configuration.

---

## Before Upgrading

- [ ] Read the release notes for the new version
- [ ] Confirm the upgrade is not breaking / requires governance vote
- [ ] Check community channels for known issues with the new version
- [ ] Back up current binary: `cp YOUR_NODE_BINARY YOUR_NODE_BINARY.bak`
- [ ] Back up current config: `cp -r ~/.YOUR_NODE_CONFIG ~/.YOUR_NODE_CONFIG.bak`
- [ ] Note current block height for comparison after upgrade
- [ ] Inform any co-validators or dependent services

## During Upgrade

- [ ] Stop the node gracefully: `systemctl stop YOUR_NODE_SERVICE`
- [ ] Replace binary or apply config changes
- [ ] Verify binary version: `YOUR_NODE_BINARY version`
- [ ] Restart node: `systemctl start YOUR_NODE_SERVICE`
- [ ] Check logs immediately: `journalctl -u YOUR_NODE_SERVICE -f`

## After Upgrading

- [ ] Node is syncing and advancing beyond the pre-upgrade block height
- [ ] RPC endpoint is responding
- [ ] No errors in logs within first 5 minutes
- [ ] Monitoring alerts resolved
- [ ] Remove backup binary/config after confirming stability (keep for 24h)

## Rollback Plan

If the upgrade fails:

```bash
systemctl stop YOUR_NODE_SERVICE
cp YOUR_NODE_BINARY.bak YOUR_NODE_BINARY
systemctl start YOUR_NODE_SERVICE
```

Check logs and report the failure to the community.
