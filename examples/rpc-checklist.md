# RPC Endpoint Checklist

This checklist helps community operators review basic RPC endpoint and network configuration details before using them in scripts, dashboards, or node-related tools.

It is intentionally generic and does not assume a specific mainnet or production endpoint.

## 1. Confirm the Source

Before using an RPC endpoint, identify where it came from.

| Check | Notes |
|---|---|
| Official documentation | Prefer official sources for critical configuration |
| Community guide | Useful for learning, but verify against official information |
| Private message or random link | Treat with caution |
| Old screenshot or copied note | Re-check before use |

## 2. Record Basic Details

Use a small table like this when tracking endpoint information.

| Field | Value |
|---|---|
| RPC URL | `YOUR_RPC_URL` |
| Chain ID | `YOUR_CHAIN_ID` |
| Source | `OFFICIAL_DOC_OR_LINK` |
| Date checked | `YYYY-MM-DD` |
| Purpose | `dashboard / node config / script test` |

## 3. Basic Connectivity Checks

Use safe, read-only checks first.

```bash
curl -I YOUR_RPC_URL
```

If the endpoint uses a JSON-RPC interface, the exact request format may vary. Check official documentation before sending requests.

## 4. Configuration Review

Before adding an endpoint to a node configuration file, confirm:

- The endpoint matches the intended network.
- The chain ID is correct.
- The endpoint is current and not copied from an outdated guide.
- The configuration file has been backed up before editing.
- No private keys, seed phrases, or credentials are stored in public files.

## 5. Troubleshooting Notes

Common issues may include:

| Symptom | Possible Cause |
|---|---|
| Timeout | Endpoint offline, firewall issue, or network problem |
| Connection refused | Service not running or wrong port |
| Wrong chain data | Endpoint belongs to a different network |
| Dashboard not updating | Node sync, RPC, or local service issue |

## 6. Safety Reminder

Do not publish private node credentials, wallet seeds, API keys, or personally sensitive infrastructure details. Public examples should use placeholders only.

## Disclaimer

This checklist is community-maintained and educational. Always verify critical network configuration against official QoreChain sources and current announcements.
