# Windows Local Authentication Analysis (Event ID 4625 & 4624)

## Overview
Analyzed local Windows Security Event Logs on `SOC-MGMT01` via LimaCharlie EDR to verify local authentication auditing and track failed vs. successful logon events.

## Evidence & Telemetry Breakdown

### Failed Logon Attempt (Event ID 4625)
* **Target Account:** analyst1
* **Logon Type:** 2 (Interactive Local Logon)
* **Channel:** Security
* **Failure Cause:** Bad Password / Unknown Username

json:
{
  "EVENT": {
    "EventData": {
      "AuthenticationPackageName": "Negotiate",
      "FailureReason": "%%2313",
      "IpAddress": "127.0.0.1",
      "IpPort": "0",
      "KeyLength": "0",
      "LmPackageName": "-",
      "LogonProcessName": "User32",
      "LogonType": "2",
      "ProcessId": "0x47c",
      "ProcessName": "C:\\Windows\\System32\\svchost.exe",
      "Status": "0xc000006d",
      "SubStatus": "0xc000006a",
      "SubjectDomainName": "WORKGROUP",
      "SubjectLogonId": "0x3e7",
      "SubjectUserName": "WIN-P61U8FQLQQI$",
      "SubjectUserSid": "S-1-5-18",
      "TargetDomainName": "WIN-P61U8FQLQQI",
      "TargetUserName": "analyst1",
      "TargetUserSid": "S-1-0-0",
      "TransmittedServices": "-",
      "WorkstationName": "WIN-P61U8FQLQQI"
    },
    "System": {
      "Channel": "Security",
      "Computer": "WIN-P61U8FQLQQI",
      "Correlation": {
        "ActivityID": "{b457bce7-2471-0002-47bd-57b47124dd01}"
      },
      "EventID": "4625",
      "EventRecordID": "30916",
      "Execution": {
        "ProcessID": "856",
        "ThreadID": "7736"
      },
      "Keywords": "0x8010000000000000",
      "Level": "0",
      "Opcode": "0",
      "Provider": {
        "Guid": "{54849625-5478-4994-a5ba-3e3b0328c30d}",
        "Name": "Microsoft-Windows-Security-Auditing"
      },
      "Security": "",
      "Task": "12544",
      "TimeCreated": {
        "SystemTime": "2026-08-05T00:35:26.5988026Z"
      },
      "Version": "0",
      "_event_id": "4625"
    }
  }
}
