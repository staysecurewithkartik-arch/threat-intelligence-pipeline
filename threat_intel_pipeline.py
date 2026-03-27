#!/usr/bin/env python3
"""
Threat Intelligence Pipeline
Ingests firewall logs, email headers, SIEM alerts → correlates IOCs → generates incident intelligence

Author: Your Name
Purpose: Automate threat detection, IOC correlation, and risk scoring
"""

import json
import re
from datetime import datetime
from collections import defaultdict
from anthropic import Anthropic
import hashlib

# Initialize Anthropic client
client = Anthropic()

# MITRE ATT&CK framework mapping (sample - can be expanded)
MITRE_MAPPING = {
    "spearphishing": "T1566.002",
    "malware": "T1566.001",
    "credential": "T1110",
    "lateral": "T1570",
    "exfil": "T1041",
    "c2": "T1071",
    "persistence": "T1547",
    "privilege": "T1548",
}

class ThreatIntelligencePipeline:
    """Main class for threat intelligence analysis"""
    
    def __init__(self):
        self.conversation_history = []
        self.iocs = defaultdict(list)  # IOC storage
        self.alerts = []
        self.incident_id = self._generate_incident_id()
    
    def _generate_incident_id(self):
        """Generate unique incident ID"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"INC-{timestamp}"
    
    def extract_iocs(self, data, source_type):
        """Extract indicators of compromise from raw data"""
        iocs_found = {
            'ips': set(),
            'domains': set(),
            'emails': set(),
            'hashes': set(),
            'urls': set()
        }
        
        # IP regex (IPv4)
        ip_pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
        iocs_found['ips'].update(re.findall(ip_pattern, data))
        
        # Domain regex
        domain_pattern = r'\b(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}\b'
        iocs_found['domains'].update(re.findall(domain_pattern, data, re.IGNORECASE))
        
        # Email regex
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        iocs_found['emails'].update(re.findall(email_pattern, data))
        
        # Hash regex (MD5, SHA1, SHA256)
        hash_pattern = r'\b(?:[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64})\b'
        iocs_found['hashes'].update(re.findall(hash_pattern, data))
        
        # URL regex
        url_pattern = r'https?://[^\s\)>\]]*'
        iocs_found['urls'].update(re.findall(url_pattern, data, re.IGNORECASE))
        
        # Store IOCs with source tracking
        for ioc_type, values in iocs_found.items():
            for value in values:
                self.iocs[ioc_type].append({
                    'value': value,
                    'source': source_type,
                    'timestamp': datetime.now().isoformat()
                })
        
        return iocs_found
    
    def correlate_iocs(self):
        """Find correlations between IOCs across sources"""
        correlations = defaultdict(list)
        
        # Find IOCs appearing in multiple sources
        for ioc_type, entries in self.iocs.items():
            ioc_values = defaultdict(int)
            for entry in entries:
                ioc_values[entry['value']] += 1
            
            for value, count in ioc_values.items():
                if count > 1:  # Appears in multiple sources
                    correlations[ioc_type].append({
                        'value': value,
                        'occurrences': count,
                        'risk_boost': count * 10  # Higher correlation = higher risk
                    })
        
        return correlations
    
    def chat_with_claude(self, user_message):
        """Send message to Claude for analysis"""
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        system_prompt = """You are a Cyber Threat Intelligence Analyst. Your role is to:
1. Analyze security alerts, firewall logs, and email headers
2. Identify indicators of compromise (IOCs)
3. Correlate patterns across data sources
4. Map tactics to MITRE ATT&CK framework
5. Assess threat severity and risk
6. Provide actionable intelligence

Always be precise, data-driven, and focus on threat actor tactics and objectives.
Structure your analysis clearly with sections for:
- Summary
- IOCs Identified
- Threat Actor Profile (if identifiable)
- MITRE ATT&CK Techniques
- Risk Assessment (0-100)
- Recommended Actions
"""
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2000,
            system=system_prompt,
            messages=self.conversation_history
        )
        
        assistant_message = response.content[0].text
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    def analyze_firewall_logs(self, log_data):
        """Analyze firewall logs through Claude"""
        print("\n[*] Analyzing firewall logs...")
        
        # Extract IOCs first
        iocs = self.extract_iocs(log_data, "firewall")
        print(f"    Found IOCs: {sum(len(v) for v in iocs.values())} indicators")
        
        # Send to Claude for analysis
        prompt = f"""Analyze these firewall logs and identify:
1. Blocked/suspicious connections
2. Attack patterns
3. Potential threat actors
4. Recommended firewall rules

Firewall Logs:
{log_data}

Provide a structured threat assessment."""
        
        analysis = self.chat_with_claude(prompt)
        return analysis, iocs
    
    def analyze_email_headers(self, email_data):
        """Analyze email headers for phishing/spoofing"""
        print("\n[*] Analyzing email headers...")
        
        # Extract IOCs
        iocs = self.extract_iocs(email_data, "email")
        print(f"    Found IOCs: {sum(len(v) for v in iocs.values())} indicators")
        
        # Send to Claude for analysis
        prompt = f"""Analyze these email headers for security threats:
1. SPF/DKIM/DMARC authenticity
2. Phishing indicators
3. Malicious links/attachments
4. Spoofing attempts
5. Threat actor TTPs

Email Headers:
{email_data}

Assess phishing risk (0-100) and recommend actions."""
        
        analysis = self.chat_with_claude(prompt)
        return analysis, iocs
    
    def analyze_siem_alerts(self, alert_data):
        """Analyze SIEM/security alerts"""
        print("\n[*] Analyzing SIEM alerts...")
        
        # Extract IOCs
        iocs = self.extract_iocs(alert_data, "siem")
        print(f"    Found IOCs: {sum(len(v) for v in iocs.values())} indicators")
        
        # Send to Claude for analysis
        prompt = f"""Analyze these security alerts for incident investigation:
1. Root cause analysis
2. Potential breach indicators
3. Lateral movement signs
4. Data exfiltration attempts
5. Command & Control communication

Security Alerts:
{alert_data}

Provide incident severity (0-100) and response recommendations."""
        
        analysis = self.chat_with_claude(prompt)
        return analysis, iocs
    
    def correlate_and_score(self):
        """Find correlations and calculate risk score"""
        print("\n[*] Correlating IOCs across sources...")
        
        correlations = self.correlate_iocs()
        
        # Calculate risk score
        base_score = 0
        
        # More sources = higher risk
        for ioc_type, entries in correlations.items():
            for entry in entries:
                base_score += entry['risk_boost']
        
        # Cap at 100
        risk_score = min(base_score, 100)
        
        print(f"    Risk Score: {risk_score}/100")
        print(f"    Correlated IOCs: {sum(len(v) for v in correlations.values())}")
        
        return correlations, risk_score
    
    def generate_incident_report(self, analyses, correlations, risk_score):
        """Generate final incident intelligence report"""
        print("\n[*] Generating incident report...")
        
        # Ask Claude to synthesize all analyses
        synthesis_prompt = f"""Based on the threat intelligence analysis above, generate a comprehensive incident intelligence report in JSON format.

Include:
1. incident_id: {self.incident_id}
2. severity: (CRITICAL/HIGH/MEDIUM/LOW) based on risk_score: {risk_score}
3. summary: 2-3 sentence executive summary
4. threat_actors: list of suspected threat actors/groups
5. iocs: all indicators of compromise with types
6. ttp_mapping: MITRE ATT&CK techniques identified
7. timeline: events in chronological order
8. recommended_actions: immediate IR steps
9. detection_evasion: any evasion techniques observed
10. confidence_level: (HIGH/MEDIUM/LOW)

Format as valid JSON only."""
        
        json_response = self.chat_with_claude(synthesis_prompt)
        
        # Try to parse JSON, fallback to structured text
        try:
            incident_report = json.loads(json_response)
        except json.JSONDecodeError:
            # Fallback if Claude doesn't output pure JSON
            incident_report = {
                "incident_id": self.incident_id,
                "severity": "MEDIUM",
                "summary": "Multi-source threat intelligence analysis completed",
                "analysis": json_response,
                "risk_score": risk_score,
                "timestamp": datetime.now().isoformat()
            }
        
        incident_report['risk_score'] = risk_score
        incident_report['timestamp'] = datetime.now().isoformat()
        incident_report['incident_id'] = self.incident_id
        
        return incident_report
    
    def run_pipeline(self, firewall_logs=None, email_headers=None, siem_alerts=None):
        """Run complete threat intelligence pipeline"""
        print(f"\n{'='*60}")
        print(f"THREAT INTELLIGENCE PIPELINE - {self.incident_id}")
        print(f"{'='*60}")
        
        analyses = {}
        
        # Process each data source
        if firewall_logs:
            fw_analysis, fw_iocs = self.analyze_firewall_logs(firewall_logs)
            analyses['firewall'] = fw_analysis
        
        if email_headers:
            email_analysis, email_iocs = self.analyze_email_headers(email_headers)
            analyses['email'] = email_analysis
        
        if siem_alerts:
            siem_analysis, siem_iocs = self.analyze_siem_alerts(siem_alerts)
            analyses['siem'] = siem_analysis
        
        # Correlate and score
        correlations, risk_score = self.correlate_and_score()
        
        # Generate final report
        incident_report = self.generate_incident_report(analyses, correlations, risk_score)
        
        return incident_report
    
    def save_report(self, report, format='json'):
        """Save incident report to file"""
        filename = f"{self.incident_id}_report.{format}"
        
        if format == 'json':
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
        elif format == 'md':
            md_content = self._convert_to_markdown(report)
            with open(filename, 'w') as f:
                f.write(md_content)
        
        print(f"\n[+] Report saved: {filename}")
        return filename
    
    def _convert_to_markdown(self, report):
        """Convert incident report to markdown"""
        md = f"""# Incident Report: {report.get('incident_id')}

**Timestamp:** {report.get('timestamp')}
**Severity:** {report.get('severity')}
**Risk Score:** {report.get('risk_score')}/100

## Summary
{report.get('summary', 'N/A')}

## Threat Actors
{', '.join(report.get('threat_actors', ['Unknown'])) if isinstance(report.get('threat_actors'), list) else report.get('threat_actors')}

## Indicators of Compromise
"""
        if 'iocs' in report and isinstance(report['iocs'], dict):
            for ioc_type, iocs_list in report['iocs'].items():
                md += f"\n### {ioc_type.upper()}\n"
                if isinstance(iocs_list, list):
                    for ioc in iocs_list:
                        md += f"- {ioc}\n"
                else:
                    md += f"- {iocs_list}\n"
        
        ## MITRE ATT&CK
        if 'ttp_mapping' in report:
            md += "\n## MITRE ATT&CK Techniques\n"
            ttps = report['ttp_mapping']
            if isinstance(ttps, dict):
                for phase, technique in ttps.items():
                    md += f"- **{phase}:** {technique}\n"
            else:
                md += f"{ttps}\n"
        
        ## Timeline
        if 'timeline' in report:
            md += "\n## Timeline\n"
            timeline = report['timeline']
            if isinstance(timeline, list):
                for event in timeline:
                    md += f"- {event}\n"
            else:
                md += f"{timeline}\n"
        
        ## Recommended Actions
        if 'recommended_actions' in report:
            md += "\n## Recommended Actions\n"
            actions = report['recommended_actions']
            if isinstance(actions, list):
                for i, action in enumerate(actions, 1):
                    md += f"{i}. {action}\n"
            else:
                md += f"{actions}\n"
        
        return md


def main():
    """Example usage"""
    pipeline = ThreatIntelligencePipeline()
    
    # Example data (replace with your actual data)
    firewall_logs = """
    2024-03-20 14:32:15 192.168.1.50 -> 203.45.67.89:4444 BLOCKED [Malicious C2 IP - known APT28]
    2024-03-20 14:35:22 192.168.1.105 -> malicious-c2.ru:443 BLOCKED [High risk domain]
    2024-03-20 14:40:18 192.168.1.50 -> 210.12.34.56:8080 BLOCKED [Port scan detected]
    2024-03-20 15:12:03 192.168.1.200 -> suspicious-domain.com:443 BLOCKED [Known phishing domain]
    """
    
    email_headers = """
    From: ceo@company-typo.com
    To: finance@realcompany.com
    Subject: Urgent: Wire Transfer Request
    Date: Wed, 20 Mar 2024 14:15:00 +0000
    
    Authentication-Results: SPF:FAIL DKIM:FAIL DMARC:FAIL
    Return-Path: <noreply@suspicious-mail.ru>
    X-Originating-IP: [203.45.67.89]
    X-Mailer: Unknown
    
    Body contains: credential_theft_link.ru, suspicious_attachment.exe
    """
    
    siem_alerts = """
    Alert 1: Unusual Login from 203.45.67.89
    Alert 2: Elevated Privileges Granted to admin_backup account
    Alert 3: Large Data Transfer to External IP 210.12.34.56
    Alert 4: Suspicious Process: powershell.exe spawning cmd.exe with Base64 encoding
    Alert 5: Lateral Movement: admin_backup accessing file servers from unusual workstation
    """
    
    # Run the pipeline
    report = pipeline.run_pipeline(
        firewall_logs=firewall_logs,
        email_headers=email_headers,
        siem_alerts=siem_alerts
    )
    
    # Save reports
    pipeline.save_report(report, format='json')
    pipeline.save_report(report, format='md')
    
    # Print summary
    print(f"\n{'='*60}")
    print("INCIDENT SUMMARY")
    print(f"{'='*60}")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
