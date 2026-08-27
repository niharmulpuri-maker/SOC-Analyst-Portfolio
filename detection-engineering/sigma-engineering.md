# Detection Engineering: Generic Sigma to EDR Rule Translation

## Overview
Engineered an industry-standard Sigma rule targeting adversary execution obfuscation (PowerShell invoked via CMD with `-EncodedCommand` flags) and translated the logic into a production LimaCharlie Detect & Respond (D&R) rule.

## MITRE ATT&CK Mapping
* **Tactic:** Execution (TA0002), Defense Evasion (TA0005)
* **Technique:** Command and Scripting Interpreter: PowerShell (T1059.001) / Obfuscated Files or Information (T1027)

## Sigma Rule Specification
Refer to `detection-engineering/custom-sigma-rules.yml` for the standard Sigma definition.

## LimaCharlie D&R Translation Logic
```yaml
events:
  - WEL
op: and
rules:
  - op: contains
    path: event/EVENT/EventData/ParentImage
    value: cmd.exe
  - op: contains
    path: event/EVENT/EventData/Image
    value: powershell.exe
  - op: or
    rules:
      - op: contains
        path: event/EVENT/EventData/CommandLine
        value: -enc
      - op: contains
        path: event/EVENT/EventData/CommandLine
        value: -EncodedCommand
      - op: contains
        path: event/EVENT/EventData/CommandLine
        value: -e
