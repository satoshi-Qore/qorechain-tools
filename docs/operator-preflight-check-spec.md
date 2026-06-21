# Operator Preflight Check Utility - Design Specification

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. Scope](#2-scope)
- [3. Checks Performed](#3-checks-performed)
- [4. Pass / Warning / Fail Criteria](#4-pass--warning--fail-criteria)
- [5. Output Format](#5-output-format)
- [6. Security Considerations](#6-security-considerations)
- [7. Future Extensions](#7-future-extensions)
- [Profiles](#profiles)
  - [Light Node](#light-node)
  - [Monitoring Node](#monitoring-node)
  - [Validator Preparation](#validator-preparation)

## 1. Purpose

The Operator Preflight Check utility is a read-only diagnostic tool for QoreChain node operators, validators, and infrastructure maintainers.

Its purpose is to verify whether a machine appears ready for basic node or monitoring operations before the operator starts installation, requests support, or submits an issue.

The tool should not configure the system, install packages, restart services, modify files, or change network settings. It only observes the environment and reports findings.

## 2. Scope

The utility should check local system readiness and basic network reachability.

Included scope:

- Docker availability
- Docker Compose availability
- Disk space
- Memory availability
- Required port status
- RPC endpoint reachability
- Expected configuration file presence

Out of scope:

- Installing Docker
- Starting or stopping containers
- Editing configuration files
- Opening firewall ports
- Managing wallets, keys, or validator identity
- Verifying rewards, commissions, or token balances
- Performing destructive troubleshooting actions

## 3. Checks Performed

### Docker Installed

The utility should detect whether Docker is installed and accessible from the current shell/session.

It should report:

- Docker CLI availability
- Docker version, if available
- Whether Docker appears usable by the current user

### Docker Compose Available

The utility should check both modern and legacy Compose formats:

- `docker compose`
- `docker-compose`

Preferred result should identify which Compose interface is available.

### Available Disk Space

The utility should check free disk space on the target working directory or configured node data path.

It should report:

- Checked path
- Total disk size
- Available disk space
- Status based on configurable thresholds

### Available Memory

The utility should check system memory.

It should report:

- Total memory
- Available memory
- Whether available memory is sufficient for the intended profile

Profiles may include:

- Light node
- Monitoring node
- Validator preparation

### Required Ports

The utility should check whether expected ports are in the correct state.

Example ports may include:

- P2P port
- RPC port
- API port
- EVM/RPC port, if applicable
- Prometheus port
- Grafana port

Port checks should be configurable because different operators may use different ports.

The utility should support two modes:

- Pre-start mode: ports should be free
- Running-node mode: ports should be listening

### RPC Reachability

The utility should test configured RPC endpoints using safe, read-only requests.

It should report:

- Endpoint label
- Reachability
- HTTP status or connection error
- Basic JSON-RPC response validity
- Response latency
- Sanitized endpoint URL

The tool should not expose authentication tokens, query strings, or sensitive headers.

### Expected Config Files

The utility should check whether expected configuration files exist.

Examples:

- Endpoint configuration file
- Docker Compose file
- Monitoring configuration file
- Node configuration path supplied by the operator

The tool should only check existence and readability unless a future schema validation mode is added.

## 4. Pass / Warning / Fail Criteria

### Pass

A check should pass when the required condition is clearly satisfied.

Examples:

- Docker is installed and accessible
- Docker Compose is available
- Disk space is above the recommended threshold
- Memory is above the recommended threshold
- Required ports are in the expected state
- RPC endpoint responds successfully
- Required config files exist and are readable

### Warning

A check should warn when the system may work but deserves attention.

Examples:

- Disk space is close to the minimum threshold
- Memory is low but not unusable
- Docker is installed but current user permissions may be limited
- RPC endpoint responds slowly
- Optional config file is missing
- A port state is unexpected but not critical for the selected profile

### Fail

A check should fail when the environment is not ready for the selected operation.

Examples:

- Docker is missing
- Docker Compose is unavailable
- Required disk space is below minimum threshold
- Available memory is critically low
- Required port is blocked or already occupied in pre-start mode
- Required service port is not listening in running-node mode
- RPC endpoint is unreachable
- Required config file is missing

Overall result:

- `PASS`: no warnings or failures
- `WARNING`: at least one warning, no failures
- `FAIL`: at least one failure

## 5. Output Format

Default output should be a Markdown report suitable for sharing in GitHub issues, support requests, or operator notes.

Suggested sections:

```md
# Operator Preflight Check Report

## Summary
Overall status: PASS / WARNING / FAIL
Profile: Light Node / Validator / Monitoring
Checked at: YYYY-MM-DD HH:MM UTC

## System Environment
- OS:
- Architecture:
- Hostname:
- Working directory:

## Docker
- Docker installed:
- Docker version:
- Docker Compose available:
- Compose mode:

## Resources
- Disk path:
- Available disk:
- Total disk:
- Available memory:
- Total memory:

## Ports
| Port | Purpose | Expected State | Actual State | Status |
|---|---|---|---|---|

## RPC Reachability
| Endpoint | Status | Latency | Notes |
|---|---|---|---|

## Config Files
| File | Required | Found | Readable | Status |
|---|---|---|---|---|

## Findings
- PASS:
- WARNING:
- FAIL:

## Recommended Next Actions
- ...
```

Optional future output formats may include:

- JSON
- CSV
- compact terminal summary
- support bundle summary

## 6. Security Considerations

The utility must remain strictly read-only.

It must not:

- Install packages
- Start or stop containers
- Modify firewall rules
- Edit configuration files
- Change permissions
- Delete files
- Upload reports automatically
- Read private keys, seed phrases, wallet files, or secrets

Sensitive data handling:

- Redact authentication tokens
- Remove query strings from URLs
- Avoid printing private headers
- Avoid printing full contents of config files
- Clearly warn users to review reports before posting publicly

RPC safety:

- Use only read-only RPC methods
- Avoid high-frequency requests
- Avoid stress testing public endpoints
- Use timeouts to prevent hanging

## 7. Future Extensions

Possible future additions:

- JSON output mode for automation
- Config schema validation
- Validator-specific readiness profile
- Monitoring stack readiness profile
- Historical comparison between preflight reports
- Basic latency trend reporting
- Prometheus/Grafana readiness checks
- Support bundle generator
- CI validation for sample config files
- Windows, Linux, and VPS-specific check profiles
- Offline mode for machines without public network access

This utility should become the first step an operator runs before setup, troubleshooting, or asking for support. It strengthens operational safety by turning common environment problems into a clear, shareable checklist without touching the system.

## Profiles

The Operator Preflight Check utility should support explicit operating profiles so that checks are evaluated according to the operator's intended role. Profiles prevent the tool from applying validator-level expectations to a light node operator or monitoring-specific checks to a basic node setup.

### Light Node

The Light Node profile is intended for operators preparing to register, run, or troubleshoot a basic QoreChain light node environment.

**Mandatory checks:**

- Docker installed
- Docker Compose available
- Available memory
- Available disk space
- Required ports
- RPC reachability

**Optional checks:**

- Presence of local endpoint configuration file
- Basic Docker permission check
- Existing container status, if a node is already running
- Latency check against multiple RPC endpoints

**Recommended thresholds:**

| Resource | Recommended Minimum | Warning Level | Fail Level |
|---|---:|---:|---:|
| Available memory | 4 GB+ | 2-4 GB | Below 2 GB |
| Available disk space | 20 GB+ | 10-20 GB | Below 10 GB |
| RPC latency | Below 1s | 1-3s | Timeout / unreachable |

**Port expectations:**

In pre-start mode, required node ports should be free.

In running-node mode, required node ports should be listening.

### Monitoring Node

The Monitoring Node profile is intended for operators running observability tools such as Prometheus, Grafana, alerting rules, or external RPC monitoring.

**Mandatory checks:**

- Docker installed
- Docker Compose available
- Prometheus port availability or listening status
- Grafana port availability or listening status
- Monitoring configuration files
- Available system resources

**Optional checks:**

- Prometheus rule file presence
- Alert rule syntax validation, future extension
- Grafana provisioning file presence
- RPC endpoint configuration file
- Existing monitoring container status

**Recommended thresholds:**

| Resource | Recommended Minimum | Warning Level | Fail Level |
|---|---:|---:|---:|
| Available memory | 4 GB+ | 2-4 GB | Below 2 GB |
| Available disk space | 15 GB+ | 5-15 GB | Below 5 GB |
| Prometheus port | Configurable, commonly 9090 | Occupied unexpectedly | Required port unavailable |
| Grafana port | Configurable, commonly 3000 | Occupied unexpectedly | Required port unavailable |

**Expected configuration files may include:**

- Monitoring Docker Compose file
- Prometheus configuration file
- Alert rule file
- Endpoint configuration file

The utility should not assume every operator uses the same monitoring stack. Monitoring file paths should be configurable.

### Validator Preparation

The Validator Preparation profile is intended for operators checking whether their environment is broadly ready for future validator-related setup. This profile should remain conservative and should not imply validator activation, eligibility, staking status, or reward expectations.

**Mandatory checks:**

- Docker installed
- Docker Compose available
- Resource thresholds
- Required ports
- Configuration files
- RPC reachability

**Optional checks:**

- Time synchronization check
- Public IP or network reachability check
- Existing node service/container status
- Multiple RPC endpoint comparison
- Backup path presence
- Log directory presence

**Recommended thresholds:**

| Resource | Recommended Minimum | Warning Level | Fail Level |
|---|---:|---:|---:|
| Available memory | 8 GB+ | 4-8 GB | Below 4 GB |
| Available disk space | 100 GB+ | 50-100 GB | Below 50 GB |
| RPC latency | Below 1s | 1-3s | Timeout / unreachable |
| Required ports | Configurable | Unexpected state | Required port blocked/unavailable |

**Configuration expectations:**

The utility should check only for the presence and readability of expected configuration files. It should not validate private validator keys, wallet files, mnemonic phrases, or staking-related data.

Validator Preparation should be treated as an environment readiness profile, not a guarantee that the machine is production-ready or eligible to validate.
