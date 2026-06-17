# Monitoring Checklist

Use this checklist before deploying monitoring in a production or public environment.

## Before Starting

- [ ] Reviewed all configuration files and replaced placeholder values
- [ ] Confirmed you have permission to monitor the target nodes
- [ ] Ensured no private IPs, credentials, or API keys are hardcoded in config files
- [ ] Reviewed firewall rules -- Prometheus and Grafana ports are NOT publicly exposed

## Prometheus

- [ ] `prometheus.yml` created from `monitoring/prometheus/prometheus.example.yml`
- [ ] All `YOUR_NODE_IP` placeholders replaced with real values
- [ ] `YOUR_CHAIN_ID` label updated
- [ ] Alert rule thresholds reviewed and adjusted for your environment
- [ ] Scrape intervals set appropriately (default: 15s)

## Grafana

- [ ] Default admin password changed after first login
- [ ] Dashboard JSON imported via Grafana UI
- [ ] Prometheus data source added and tested
- [ ] No public internet access to port 3000

## Docker

- [ ] Docker and Docker Compose installed
- [ ] Stack started with `docker compose up -d` from `monitoring/`
- [ ] Container logs checked: `docker compose logs -f`
- [ ] Volumes are persisting data correctly

## After Deployment

- [ ] Test alerts fire correctly in a safe environment before relying on them
- [ ] Confirm no sensitive data appears in dashboard panels or alert annotations
- [ ] Document your configuration privately -- do not commit live configs to public repos
- [ ] Schedule regular reviews of alert thresholds

## Disclaimer

This checklist is a community guide. It does not guarantee production readiness or security compliance.
