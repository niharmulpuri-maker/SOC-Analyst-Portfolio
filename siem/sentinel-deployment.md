# Cloud SIEM Deployment & Log Aggregation (Microsoft Sentinel)

## Overview
Engineered a hybrid cloud SIEM architecture by connecting local virtual workstations (`SOC-WKS01` and `SOC-MGMT01`) to a Microsoft Sentinel workspace (`law-soc-sentinel`) using Azure Arc and the Azure Monitor Agent (AMA). Configured automated Data Collection Rules (DCR) and ingestion guardrails to establish centralized cloud security monitoring.

---

## Architecture & Configuration Details
* **SIEM Workspace:** Microsoft Sentinel on `law-soc-sentinel`
* **Hybrid Connectivity:** Azure Arc Connected Machine Agent
* **Ingestion Pipeline:** Azure Monitor Agent (AMA) via Data Collection Rule (`dcr-windows-security-sysmon`)
* **Cost Controls:** Enforced a strict `0.5 GB/day` Daily Ingestion Cap in Log Analytics to safeguard Azure student credits.
* **Data Sources Ingested:** 
  * Windows Security Event Logs (`SecurityEvent` table)
  * System Monitor Logs (`Event` table - `Microsoft-Windows-Sysmon/Operational`)

---

## Telemetry Verification (KQL Queries)

### 1. Windows Security Log Aggregation
```kql
SecurityEvent
| summarize EventCount = count() by Computer, EventID
| order by EventCount desc
```
### 2. Sysmon Telemetry Aggregation
```Event
| where EventLog == "Microsoft-Windows-Sysmon/Operational"
| summarize EventCount = count() by Computer, EventID
| order by EventCount desc
```
### Key Takeaways
Dual-Tier Visibility: Local endpoint telemetry routes instantaneously to LimaCharlie EDR for real-time D&R containment, while OS audit logs stream concurrently to Microsoft Sentinel for long-term cloud correlation and threat hunting.

Resource & Budget Safeguards: Enforcing daily ingestion caps prevents log volume spikes from exhausting cloud credits while maintaining security visibility.
<img width="1440" height="777" alt="Screenshot 2026-08-10 at 8 16 16 PM" src="https://github.com/user-attachments/assets/8e83d2a7-9609-45ce-8bae-9bb7d8c2b019" />
