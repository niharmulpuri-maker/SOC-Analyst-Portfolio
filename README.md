# Enterprise SOC Analyst & Threat Detection Home Lab

[![MITRE ATT&CK](https://img.shields.io/badge/MITRE%20ATT%26CK-Mapped-blue.svg)](https://attack.mitre.org/)
[![SIEM](https://img.shields.io/badge/SIEM-Microsoft%20Sentinel-0078D4.svg)](https://azure.microsoft.com/services/microsoft-sentinel/)
[![EDR](https://img.shields.io/badge/EDR-LimaCharlie-2D5BFF.svg)](https://limacharlie.io/)
[![Python](https://img.shields.io/badge/Automation-Python%203-3776AB.svg)](https://www.python.org/)

---

## Executive Summary
This repository documents the end-to-end architecture, adversary emulation, detection engineering, and automation workflows of a hybrid enterprise **Security Operations Center (SOC)** lab. 

The lab bridges local virtualized endpoints (`SOC-WKS01`, `SOC-MGMT01`) with cloud-native security platforms (**LimaCharlie EDR** and **Microsoft Sentinel SIEM**). Controlled adversary techniques were executed using **Atomic Red Team**, validated through **Sysmon** telemetry, codified into custom **Sigma / D&R rules**, and integrated into an automated **Python REST API** triage pipeline.

---

## Architecture Topology

```mermaid
flowchart TD
    subgraph Virtual_Lab_UTM ["Virtual Lab Environment (UTM / Apple Silicon)"]
        WKS["<b>SOC-WKS01</b><br/>Windows 11 Workstation<br/>• Sysmon v15<br/>• LimaCharlie Agent<br/>• Azure Arc (AMA)"]
        MGMT["<b>SOC-MGMT01</b><br/>Windows Management<br/>• Azure Arc (AMA)"]
    end

    subgraph Adversary_Simulation ["Adversary Emulation Engine"]
        ART["<b>Atomic Red Team</b><br/>• T1053.005 / T1059.001 / T1548.002"]
    end

    subgraph EDR_and_SIEM ["Detection & SIEM Pipeline"]
        LC["<b>LimaCharlie EDR</b><br/>Real-Time D&R Rules & Telemetry"]
        MS["<b>Microsoft Sentinel</b><br/>Hybrid Azure Arc Ingestion + KQL"]
    end

    subgraph Automation_Layer ["SecOps Automation"]
        PY["<b>Python Automation</b><br/>alert_collector.py (REST API)"]
        CSV["Structured CSV Triage Report"]
    end

    ART --> WKS
    WKS --> LC
    WKS --> MS
    MGMT --> MS
    LC --> PY
    PY --> CSV
