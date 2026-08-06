# Detection Engineering: Custom D&R Rule for Persistence Detection

## Overview
Engineered, tested, and validated a custom Detect & Respond (D&R) rule within LimaCharlie EDR to detect unauthorized scheduled task creation (`schtasks.exe /create`) using normalized Sysmon Event ID 1 telemetry.

## Detection Logic (YAML)

```yaml
events:
  - WEL
op: and
rules:
  - op: contains
    path: event/EVENT/EventData/CommandLine
    value: schtasks
  - op: contains
    path: event/EVENT/EventData/CommandLine
    value: /create

- action: report
  name: Custom Detection - Scheduled Task Persistence Attempt
