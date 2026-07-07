# Local Endpoint Network Isolation & Workgroup Alignment

## Project Overview
To optimize local system resources on an 8GB MacBook Air running a native UTM hypervisor, the local lab environment was engineered using a dual Windows 11 Workstation (`SOC-WKS01`) and Management Workstation (`SOC-MGMT01`) workgroup architecture. This peer-to-peer sandbox replaces a heavy centralized Active Directory Domain Controller topology, significantly lowering background memory allocation to a strict 2.3 GB per virtual machine while completely retaining high-fidelity local endpoint logging capabilities.

## Engineering & Implementation Steps
1. **Network Sandbox Isolation:** Switched the virtual network adapters for both endpoints inside UTM from Shared Network (NAT) to **Host-Only** mode, creating a closed sandbox layer cut off from home Wi-Fi interference.
2. **Static IP Assignment:** Manually overrode automatic DHCP assignments via administrative PowerShell cmdlets to establish a fixed local private subnet line (`192.168.100.0/24`), placing the primary workstation at `192.168.100.10` and the management console at `192.168.100.20`.
3. **Local Name Resolution Mapping:** Hardcoded explicit local routing rules within the Windows system hosts directories (`C:\Windows\System32\drivers\etc\hosts`) on both machines to ensure flawless host-to-IP resolution without requiring a dedicated DNS server.
4. **Firewall Modification:** Punched through the restrictive default Windows 11 Inbound Firewall profile by enabling the `FPS-ICMP4-ERQ-In` rule via PowerShell, establishing secure, multi-directional peer communication verified through active echo replies.

## Verification
Peer-to-peer network alignment was validated via terminal connectivity checks, successfully translating hostname lookups and logging clean local cross-workstation traffic profiles.
<img width="1439" height="900" alt="Screenshot 2026-07-07 at 3 16 00 PM" src="https://github.com/user-attachments/assets/6cd3946c-1535-49db-84c0-2e9c9406be74" />
