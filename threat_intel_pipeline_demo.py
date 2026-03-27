#!/usr/bin/env python3
"""
Threat Intelligence Pipeline - DEMO VERSION
Shows expected output structure and functionality without requiring API key

Run this to see what the pipeline produces.
For production use, install with: pip install -r requirements.txt
"""

import json
from datetime import datetime
from collections import defaultdict

class ThreatIntelligencePipelineDemo:
    """Demo version showing pipeline output"""
    
    def __init__(self):
        self.incident_id = f"INC-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.iocs = defaultdict(list)
    
    def extract_iocs(self, data, source_type):
        """Demo IOC extraction"""
        iocs_found = {
            'ips': {'203.45.67.89', '210.12.34.56', '104.21.45.67'},
            'domains': {'malicious-c2.ru', 'office365-verify-real.ru', 'suspicious-domain.com'},
            'emails': {'attacker@malicious-c2.ru', 'fake-ceo@company-typo.com'},
            'hashes': {'a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6', 'b1d2e3f4a5c6d7e8f9a0b1c2d3e4f5a6'},
            'urls': {'http://office365-verify-real.ru/login', 'http://malware-distribution.ru/payload.exe'}
        }
        return iocs_found
    
    def generate_demo_report(self):
        """Generate realistic incident report"""
        report = {
            "incident_id": self.incident_id,
            "severity": "CRITICAL",
            "risk_score": 95,
            "timestamp": datetime.now().isoformat(),
            "summary": "Advanced Persistent Threat (APT28) campaign targeting financial data. Multiple attack vectors: credential harvesting (phishing emails), privilege escalation (Mimikatz), lateral movement across internal systems, and data exfiltration to external infrastructure.",
            "threat_actors": ["APT28", "Sofacy (Russian state-sponsored)"],
            "confidence_level": "VERY HIGH",
            "iocs": {
                "ips": [
                    {"value": "203.45.67.89", "type": "Command & Control", "occurrences": 4, "source": ["firewall", "email", "siem"]},
                    {"value": "210.12.34.56", "type": "Data Exfiltration", "occurrences": 1, "source": ["siem"]},
                    {"value": "104.21.45.67", "type": "Phishing/Credential Harvesting", "occurrences": 2, "source": ["firewall", "email"]}
                ],
                "domains": [
                    {"value": "malicious-c2.ru", "type": "APT28 C2 Infrastructure", "occurrences": 3, "source": ["firewall", "email", "siem"]},
                    {"value": "office365-verify-real.ru", "type": "Credential Harvesting", "occurrences": 2, "source": ["firewall", "email"]},
                    {"value": "suspicious-domain.com", "type": "Phishing", "occurrences": 1, "source": ["firewall"]}
                ],
                "hashes": [
                    {"value": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6", "type": "Mimikatz variant", "confidence": "HIGH"},
                    {"value": "b1d2e3f4a5c6d7e8f9a0b1c2d3e4f5a6", "type": "Sofacy trojan", "confidence": "HIGH"}
                ],
                "emails": [
                    {"value": "attacker@malicious-c2.ru", "type": "Attacker infrastructure"},
                    {"value": "fake-ceo@company-typo.com", "type": "Spoofed executive"}
                ]
            },
            "ttp_mapping": {
                "initial_access": "T1566.002 - Phishing: Spearphishing Link (CEO fraud + malware-laden emails)",
                "credential_access": "T1110.003 - Brute Force: Password Spraying (147 failed attempts on DC), T1555.003 - Credentials from Web Browsers",
                "execution": "T1059.001 - Command and Scripting Interpreter: PowerShell (with Base64-encoded payloads)",
                "persistence": "T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys",
                "privilege_escalation": "T1134 - Access Token Manipulation (token impersonation), T1134.003 - Make and Impersonate Token",
                "defense_evasion": "T1027 - Obfuscated Files or Information (Base64, encrypted payloads)",
                "lateral_movement": "T1570 - Lateral Tool Transfer (PsExec, SMB enumeration)",
                "collection": "T1557.002 - NTLM Relay (credential capture across network)",
                "exfiltration": "T1041 - Exfiltration Over C2 Channel (2.3 GB to 210.12.34.56)",
                "command_control": "T1071.001 - Application Layer Protocol (HTTPS to malicious-c2.ru port 443)"
            },
            "attack_chain": [
                {
                    "stage": 1,
                    "name": "Initial Compromise",
                    "description": "Phishing emails sent to finance@realcompany.com, marketing@realcompany.com",
                    "indicators": ["office365-verify-real.ru", "CEO fraud email", "suspicious attachments"],
                    "ttp": "T1566.002"
                },
                {
                    "stage": 2,
                    "name": "Credential Harvesting",
                    "description": "Users clicked phishing links, entered credentials on fake Office 365 page",
                    "indicators": ["office365-verify-real.ru login page", "credential capture"],
                    "ttp": "T1056.004"
                },
                {
                    "stage": 3,
                    "name": "Initial Access",
                    "description": "Attacker uses harvested credentials to access company network from 203.45.67.89",
                    "indicators": ["RDP login from 203.45.67.89", "admin_backup account compromised"],
                    "ttp": "T1021.001"
                },
                {
                    "stage": 4,
                    "name": "Privilege Escalation",
                    "description": "Mimikatz executed to dump domain credentials from LSASS",
                    "indicators": ["Mimikatz detection", "token impersonation", "LSASS access"],
                    "ttp": "T1134, T1134.003"
                },
                {
                    "stage": 5,
                    "name": "Lateral Movement",
                    "description": "Attacker uses compromised admin credentials to move laterally",
                    "indicators": ["SMB enumeration", "PsExec execution", "multiple RDP sessions"],
                    "ttp": "T1570"
                },
                {
                    "stage": 6,
                    "name": "Data Collection",
                    "description": "Large-scale file enumeration and collection from Finance share",
                    "indicators": ["2.3 GB data read from \\\\192.168.15.250\\Finance$"],
                    "ttp": "T1083"
                },
                {
                    "stage": 7,
                    "name": "Exfiltration",
                    "description": "Stolen data compressed and exfiltrated to external server",
                    "indicators": ["210.12.34.56 external IP", "HTTPS outbound to unusual port", "China geoip"],
                    "ttp": "T1041"
                }
            ],
            "timeline": [
                {"timestamp": "2024-03-20T14:15:00Z", "event": "Phishing emails delivered to 4 company users"},
                {"timestamp": "2024-03-20T14:22:00Z", "event": "User clicked phishing link to office365-verify-real.ru"},
                {"timestamp": "2024-03-20T14:25:00Z", "event": "Credentials harvested from credential harvesting page"},
                {"timestamp": "2024-03-20T14:32:45Z", "event": "RDP login from 203.45.67.89 using stolen admin_backup credentials"},
                {"timestamp": "2024-03-20T14:36:22Z", "event": "Network reconnaissance commands executed (net view, nslookup, ping sweep)"},
                {"timestamp": "2024-03-20T14:42:00Z", "event": "Brute force attack on Domain Controller (147 failed attempts, 1 successful)"},
                {"timestamp": "2024-03-20T14:45:12Z", "event": "Privilege escalation: Mimikatz executed, domain credentials dumped"},
                {"timestamp": "2024-03-20T14:55:22Z", "event": "Command & Control communication established with malicious-c2.ru"},
                {"timestamp": "2024-03-20T15:05:15Z", "event": "Suspicious PowerShell process tree with Base64-encoded payload"},
                {"timestamp": "2024-03-20T15:12:30Z", "event": "Lateral movement: SMB enumeration and RDP to multiple systems"},
                {"timestamp": "2024-03-20T15:18:45Z", "event": "Large data exfiltration: 2.3 GB stolen to 210.12.34.56"},
            ],
            "impact_assessment": {
                "data_compromised": "Financial data (invoices, contracts, agreements)",
                "scope": "Finance department and IT admin accounts",
                "estimated_data_volume": "2.3 GB",
                "affected_systems": ["192.168.15.45", "192.168.15.250", "Domain Controller"],
                "affected_users": 4,
                "business_impact": "SEVERE - Financial data breach, regulatory implications (GDPR, SOX)",
                "recovery_time_estimate": "72 hours minimum"
            },
            "recommended_actions": [
                "IMMEDIATE (0-2 hours):",
                "1. Isolate affected workstations (192.168.15.45, 192.168.15.250) from network immediately",
                "2. Kill all active sessions to 203.45.67.89 and 210.12.34.56",
                "3. Reset ALL domain administrator and sensitive account passwords (force change)",
                "4. Revoke security tokens and session keys for compromised accounts",
                "",
                "SHORT-TERM (2-24 hours):",
                "5. Block all malicious IOCs at perimeter (firewall, proxy, DNS):",
                "   - IPs: 203.45.67.89, 210.12.34.56, 104.21.45.67",
                "   - Domains: malicious-c2.ru, office365-verify-real.ru, suspicious-domain.com",
                "6. Enable enhanced logging on Domain Controllers",
                "7. Scan all domain computers for similar C2 beacons using yara/sigma rules",
                "8. Check for lateral movement indicators on all accessed systems",
                "9. Review VPN and remote access logs for suspicious activity",
                "10. Engage forensics team for disk imaging of compromised systems",
                "",
                "MEDIUM-TERM (24-72 hours):",
                "11. Conduct full domain compromise assessment",
                "12. Review Kerberos tickets and session logs for pass-the-ticket attacks",
                "13. Audit share permissions and access logs",
                "14. Notify incident response leadership and CEO",
                "15. Prepare data breach notification (GDPR/SOX implications)",
                "",
                "POST-INCIDENT:",
                "16. Implement multi-factor authentication (MFA) on all admin accounts",
                "17. Deploy EDR (Endpoint Detection & Response) if not already present",
                "18. Review email security controls (SPF/DKIM/DMARC/DMARC)",
                "19. Conduct tabletop exercises for future incident response",
                "20. File incident report with compliance/legal teams"
            ],
            "detection_evasion_observed": [
                "Use of legitimate tools (PsExec, Windows built-ins) - Living off the Land (LOLBAs)",
                "Base64 encoding of PowerShell payloads",
                "Use of HTTPS for C2 communication to blend with normal traffic",
                "Timing outside business hours (14:32 = 8:32 PM IST)",
                "Credential reuse from legitimate admin account (harder to detect)"
            ],
            "threat_actor_profile": {
                "attribution": "APT28 (Sofacy/Fancy Bear)",
                "country": "Russia",
                "motivation": "Cyber espionage / Economic espionage",
                "expertise_level": "EXPERT",
                "known_capabilities": [
                    "Advanced persistence mechanisms",
                    "Custom malware development (Sofacy trojan, implants)",
                    "Sophisticated social engineering",
                    "Network reconnaissance and lateral movement",
                    "Data exfiltration and staging"
                ],
                "previous_targets": "Government, defense contractors, financial institutions",
                "methodology": "Spear-phishing → credential theft → lateral movement → data theft"
            },
            "correlation_analysis": {
                "firewall_analysis": {
                    "alerts": 10,
                    "critical": 2,
                    "high": 4,
                    "iocs_extracted": 7
                },
                "email_analysis": {
                    "alerts": 3,
                    "critical": 2,
                    "high": 1,
                    "iocs_extracted": 5
                },
                "siem_analysis": {
                    "alerts": 8,
                    "critical": 4,
                    "high": 3,
                    "iocs_extracted": 6
                },
                "cross_source_correlations": [
                    "203.45.67.89 appears in: firewall (C2), email (origin), SIEM (RDP login)",
                    "malicious-c2.ru appears in: firewall (block), email (body), SIEM (C2 beacon)",
                    "admin_backup account appears in: firewall (source), SIEM (privilege escalation, lateral movement)"
                ]
            }
        }
        return report
    
    def save_report(self, report, format='json'):
        """Save demo report"""
        filename = f"{report['incident_id']}_report.{format}"
        
        if format == 'json':
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
        elif format == 'md':
            md = self._convert_to_markdown(report)
            with open(filename, 'w') as f:
                f.write(md)
        
        return filename
    
    def _convert_to_markdown(self, report):
        """Convert to markdown"""
        md = f"""# Incident Report: {report['incident_id']}

**Timestamp:** {report['timestamp']}
**Severity:** {report['severity']}
**Risk Score:** {report['risk_score']}/100
**Confidence Level:** {report['confidence_level']}

## Executive Summary

{report['summary']}

## Threat Actors

{', '.join(report['threat_actors'])}

## Impact Assessment

- **Data Compromised:** {report['impact_assessment']['data_compromised']}
- **Data Volume:** {report['impact_assessment']['estimated_data_volume']}
- **Affected Systems:** {len(report['impact_assessment']['affected_systems'])} systems
- **Affected Users:** {report['impact_assessment']['affected_users']} users
- **Business Impact:** {report['impact_assessment']['business_impact']}

## Indicators of Compromise (IOCs)

### IP Addresses
"""
        for ioc in report['iocs']['ips']:
            md += f"- **{ioc['value']}** ({ioc['type']}) - {ioc['occurrences']} occurrence(s)\n"
        
        md += "\n### Malicious Domains\n"
        for ioc in report['iocs']['domains']:
            md += f"- **{ioc['value']}** ({ioc['type']}) - {ioc['occurrences']} occurrence(s)\n"
        
        md += "\n### File Hashes\n"
        for ioc in report['iocs']['hashes']:
            md += f"- **{ioc['value']}** ({ioc['type']})\n"
        
        md += "\n## MITRE ATT&CK Techniques\n"
        for tactic, technique in report['ttp_mapping'].items():
            md += f"- **{tactic.title()}:** {technique}\n"
        
        md += "\n## Attack Timeline\n"
        for event in report['timeline']:
            md += f"- **{event['timestamp']}** - {event['event']}\n"
        
        md += "\n## Recommended Immediate Actions\n"
        for action in report['recommended_actions']:
            md += f"{action}\n"
        
        return md


def main():
    """Demo execution"""
    print("\n" + "="*60)
    print("THREAT INTELLIGENCE PIPELINE - DEMO")
    print("="*60)
    print("\n[*] This is a demonstration of the threat intelligence pipeline output")
    print("[*] For production use with real data, ensure ANTHROPIC_API_KEY is set")
    print("[*] See README.md for setup instructions\n")
    
    pipeline = ThreatIntelligencePipelineDemo()
    
    print("[*] Generating demo incident report...")
    report = pipeline.generate_demo_report()
    
    print(f"[*] Incident ID: {report['incident_id']}")
    print(f"[*] Severity: {report['severity']}")
    print(f"[*] Risk Score: {report['risk_score']}/100")
    
    # Save reports
    json_file = pipeline.save_report(report, format='json')
    md_file = pipeline.save_report(report, format='md')
    
    print(f"\n[+] JSON report saved: {json_file}")
    print(f"[+] Markdown report saved: {md_file}")
    
    # Print summary
    print(f"\n{'='*60}")
    print("INCIDENT SUMMARY")
    print(f"{'='*60}")
    print(f"ID: {report['incident_id']}")
    print(f"Threat Actors: {', '.join(report['threat_actors'])}")
    print(f"Data Compromised: {report['impact_assessment']['data_compromised']}")
    print(f"Volume: {report['impact_assessment']['estimated_data_volume']}")
    print(f"\nIOCs Found: {len(report['iocs']['ips'])} IPs, {len(report['iocs']['domains'])} domains, {len(report['iocs']['hashes'])} hashes")
    print(f"TTPs Mapped: {len(report['ttp_mapping'])} attack stages")
    print(f"Timeline Events: {len(report['timeline'])} events")
    print(f"\n[*] Full report available in generated files above")
    print(f"[*] Demo complete! Ready for production use with real data.\n")


if __name__ == "__main__":
    main()
