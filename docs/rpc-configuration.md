# RPC Monitor Configuration

The monitor reads endpoint definitions from a JSON file.

Start from:

```bash
cp examples/endpoints.example.json endpoints.local.json
```

Then edit `endpoints.local.json`.

## Fields

| Field | Required | Description |
|---|---|---|
| `name` | Yes | Human-readable endpoint label |
| `url` | Yes | RPC endpoint URL |
| `method` | No | JSON-RPC method to call. Defaults to `status` |
| `timeout_seconds` | No | Request timeout. Defaults to `10` |

## Example

```json
{
  "endpoints": [
    {
      "name": "Example QoreChain RPC",
      "url": "https://YOUR_RPC_URL",
      "method": "status",
      "timeout_seconds": 10
    }
  ]
}
```

## Local Files

Use `endpoints.local.json` for personal testing. Avoid committing real private endpoints, API keys, tokens, or paid-provider URLs.

## Recommended Workflow

1. Copy the example configuration: `cp examples/endpoints.example.json endpoints.local.json`
2. Replace placeholders with endpoints you are allowed to test.
3. Run the monitor: `python3 scripts/rpc_health_monitor.py endpoints.local.json`
4. Review the generated Markdown report.
5. Remove sensitive data before sharing results.
