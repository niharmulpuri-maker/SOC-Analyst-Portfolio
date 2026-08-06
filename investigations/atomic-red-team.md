# Adversary Emulation & Detection Verification (Atomic Red Team)

## Overview
Executed controlled adversary emulation tests using the Atomic Red Team framework on `SOC-WKS01` to validate LimaCharlie EDR and Sysmon process creation telemetry against MITRE ATTACK techniques.

## Tested MITRE ATT&CK Techniques

### 1. Persistence via Scheduled Task (T1053.005)
* **Execution Command:** `Invoke-AtomicTest T1053.005 -TestNumbers 1`
* **Telemetry Event:** Sysmon Event ID 1 (Process Creation)
* **Image:** `C:\Windows\System32\schtasks.exe`

```json
{
  "EVENT": {
    "EventData": {
      "CommandLine": "schtasks  /create /tn \"T1053_005_OnLogon\" /sc onlogon /tr \"cmd.exe /c calc.exe\"",
      "Company": "Microsoft Corporation",
      "CurrentDirectory": "C:\\Users\\Nihar\\AppData\\Local\\Temp\\",
      "Description": "Task Scheduler Configuration Tool",
      "FileVersion": "10.0.26100.6725 (WinBuild.160101.0800)",
      "Hashes": "MD5=07EB834C69F8557F33A066051D298BF2,SHA256=8FDBF674FCF218E6C9B0F8B61AE5583E7D061643760090D4E210AA2A2E25773B,IMPHASH=15B98131447F3FE7853021D3B8BDBE26",
      "Image": "C:\\Windows\\System32\\schtasks.exe",
      "IntegrityLevel": "High",
      "LogonGuid": "{001a6485-ccb0-6a73-4f8a-260000000000}",
      "LogonId": "0x268a4f",
      "OriginalFileName": "schtasks.exe",
      "ParentCommandLine": "\"cmd.exe\" /c schtasks /create /tn \"T1053_005_OnLogon\" /sc onlogon /tr \"cmd.exe /c calc.exe\" & schtasks /create /tn \"T1053_005_OnStartup\" /sc onstart /ru system /tr \"cmd.exe /c calc.exe\"",
      "ParentImage": "C:\\Windows\\System32\\cmd.exe",
      "ParentProcessGuid": "{001a6485-d199-6a73-f901-000000000b00}",
      "ParentProcessId": "4088",
      "ParentUser": "WIN-U943MVP54NP\\Nihar",
      "ProcessGuid": "{001a6485-d19a-6a73-fb01-000000000b00}",
      "ProcessId": "5696",
      "Product": "Microsoft® Windows® Operating System",
      "RuleName": "-",
      "TerminalSessionId": "1",
      "User": "WIN-U943MVP54NP\\Nihar",
      "UtcTime": "2026-08-06 00:13:14.131"
    },
    "System": {
      "Channel": "Microsoft-Windows-Sysmon/Operational",
      "Computer": "WIN-U943MVP54NP",
      "Correlation": "",
      "EventID": "1",
      "EventRecordID": "2902",
      "Execution": {
        "ProcessID": "3076",
        "ThreadID": "3768"
      },
      "Keywords": "0x8000000000000000",
      "Level": "4",
      "Opcode": "0",
      "Provider": {
        "Guid": "{5770385f-c22a-43e0-bf4c-06f5698ffbd9}",
        "Name": "Microsoft-Windows-Sysmon"
      },
      "Security": {
        "UserID": "S-1-5-18"
      },
      "Task": "1",
      "TimeCreated": {
        "SystemTime": "2026-08-06T00:13:14.1435484Z"
      },
      "Version": "5",
      "_event_id": "1"
    }
  }
}
