# Operator Safety Guidelines

This document provides general safety practices for community members who operate, test, or document QoreChain-related infrastructure.

It is not a replacement for official QoreChain documentation, hosting-provider guidance, or security review. The goal is to reduce common mistakes when handling node logs, configuration files, credentials, and support requests.

## Scope

These guidelines apply to:

- Light node and server testing
- VPS-based infrastructure experiments
- Log review and troubleshooting
- Community support discussions
- Documentation examples and shared screenshots

They intentionally avoid assumptions about final mainnet behavior, future reward mechanics, or production validator requirements.

## Sensitive Information

Never share the following information in public channels, screenshots, GitHub issues, pull requests, or support messages:

- Seed phrases or private keys
- Wallet backup files
- API keys, access tokens, or session cookies
- SSH private keys
- Full server login details
- Private RPC credentials
- Unredacted configuration files
- Internal IP addresses when not necessary
- Personal identity documents or payment details

If a file or screenshot may contain sensitive data, review it before sharing.

## Safe Log Sharing

Logs are useful for troubleshooting, but they may contain information that should not be public.

Before sharing logs:

1. Remove wallet addresses if they are not required for the discussion.
2. Remove private endpoints, tokens, and authentication headers.
3. Replace server IP addresses with placeholders such as `YOUR_SERVER_IP`.
4. Keep only the relevant error window instead of pasting full log history.
5. Explain what action produced the log entry.

Example sanitized log note:

```text
Service: light-node-container
Time window: last 10 minutes
Action before issue: restarted container after editing config
Observed signal: repeated connection timeout
Sanitized log excerpt:
[time] failed to connect to RPC endpoint YOUR_RPC_URL
```

## Configuration File Handling

Before editing a configuration file:

- Make a backup copy.
- Confirm the source of endpoints, chain IDs, and ports.
- Use placeholder values in public examples.
- Avoid committing environment-specific configuration to GitHub.
- Review changes before restarting services.

Example backup command:

```bash
cp config.toml config.toml.backup
```

## Restart Safety

Before restarting a node, container, or service, record the current state:

- Current service status
- Recent logs
- Configuration file changed
- Command used for restart
- Time of restart
- Result after restart

This makes troubleshooting easier if the same issue returns later.

## Support Requests

When asking for help, include enough context to be useful without exposing private data.

Recommended format:

```text
Environment: VPS / Docker / local machine
Service: node or related container name
Goal: what you were trying to do
Issue: short description of the problem
Last action: what changed before the issue appeared
Sanitized logs: relevant excerpt only
Already checked: status, logs, ports, config backup
```

Avoid posting vague messages such as `not working` without context. Clear reports help community members and maintainers respond faster.

## GitHub Issue Safety

When opening a GitHub issue:

- Use a clear title.
- Describe expected and observed behavior.
- Include reproduction steps when possible.
- Use sanitized logs and placeholders.
- Do not attach private files.
- Separate questions from bug reports when possible.

For documentation issues, focus on what was unclear and what additional information would help new operators.

## Wallet and Reward Caution

Do not make operational decisions based only on unofficial reward expectations.

For any reward, delegation, staking, validator, or mainnet-related question:

- Check official QoreChain announcements.
- Avoid sharing seed phrases or private keys with anyone.
- Be cautious with direct messages offering support.
- Treat links from unknown users as untrusted.
- Do not assume future reward mechanics before they are officially documented.

## Quick Checklist

Before sharing anything publicly, ask:

- Does this include a private key, seed phrase, token, or password?
- Does this reveal a private endpoint or server login detail?
- Can I replace real values with placeholders?
- Is the log excerpt limited to the relevant issue?
- Am I making a claim that should wait for official confirmation?

If the answer is uncertain, do not share yet. Review and sanitize first.

## Disclaimer

These are community-maintained safety notes. They are intended for education and operational hygiene, not as formal security advice.