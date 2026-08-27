# Security Automation: Automated SOC Incident Alert Collector

## Overview
Engineered a standalone Python automation pipeline (`alert_collector.py`) that interfaces with LimaCharlie's REST API to programmatically extract, normalize, and export high-severity endpoint detections generated over a rolling 24-hour window.

---

## Technical Features
* **REST Authentication:** Authenticates against `https://jwt.limacharlie.io` using scoped organization credentials to obtain temporary JSON Web Tokens (JWT).
* **Telemetry Extraction:** Automatically queries detection endpoints (`/v1/insight/{oid}/detections`) to pull real-time security events across Windows workstations.
* **JSON Schema Normalization:** Recursively parses nested Windows Event Logs (`WEL`) and Sysmon Event ID 1 payloads (`CommandLine`, `ParentImage`, `User`, `Timestamp`).
* **CSV Reporting Pipeline:** Generates structured deliverables (`recent_alerts_report.csv`) for tier-1 SOC triage workflows and incident ticket ingestion.

---

## Automation Script Architecture
* **Script:** `alert_collector.py`
* **Dependencies:** `requests`, `csv`, `datetime`, `os`
* **Output Deliverable:** `recent_alerts_report.csv`

---

## Sample Execution & Output
```bash
$ export LC_OID="73b3f241-5aa9-4a07-b4c2-a67ce39efd93"
$ export LC_API_KEY="********-****-****-****-************"
$ python3 alert_collector.py

============================================================
      LIMACHARLIE SOC AUTOMATION: ALERT COLLECTOR
============================================================
[*] Authenticating with LimaCharlie API for OID: 73b3f241-5aa9-4a07-b4c2-a67ce39efd93...
[+] JWT Token successfully acquired.
[*] Retrieving detection telemetry for the last 24 hours...
[+] Retrieved 3 detection event(s). Parsing records...
[+] Successfully parsed and exported 3 detection(s) to: automation/recent_alerts_report.csv
[+] Automation pipeline execution completed successfully.
