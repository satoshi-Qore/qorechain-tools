#!/usr/bin/env bash

# QoreChain community health-check helper.
# Usage: bash scripts/health-check.sh [CONTAINER_NAME]
# This script is read-only. It does not restart, delete, update, or modify files.

set -u

CONTAINER_NAME="${1:-}"

print_section() {
  printf '\n== %s ==\n' "$1"
}

run_if_available() {
  local command_name="$1"
  shift

  if command -v "$command_name" >/dev/null 2>&1; then
    "$@"
  else
    printf '%s is not installed or not available in PATH.\n' "$command_name"
  fi
}

print_section "System"
run_if_available uname uname -a
run_if_available uptime uptime

print_section "Disk Usage"
run_if_available df df -h

print_section "Memory Usage"
run_if_available free free -h

print_section "Listening Ports"
if command -v ss >/dev/null 2>&1; then
  ss -tulpn
elif command -v netstat >/dev/null 2>&1; then
  netstat -tulpn
else
  printf 'ss or netstat is not available.\n'
fi

print_section "Docker Containers"
if command -v docker >/dev/null 2>&1; then
  docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'
else
  printf 'docker is not installed or not available in PATH.\n'
fi

if [ -n "$CONTAINER_NAME" ]; then
  print_section "Recent Docker Logs: $CONTAINER_NAME"
  if command -v docker >/dev/null 2>&1; then
    docker logs --tail 80 "$CONTAINER_NAME" 2>&1
  else
    printf 'docker is not installed or not available in PATH.\n'
  fi
fi

print_section "Safety Reminder"
printf '%s\n' 'Review output before sharing it publicly.'
printf '%s\n' 'Remove private keys, seed phrases, IPs, credentials, tokens, and sensitive logs.'
printf '%s\n' 'Verify critical network values through official QoreChain sources.'
