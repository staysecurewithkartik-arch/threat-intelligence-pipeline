# Threat Intelligence Pipeline with Claude AI

**Automate SOC threat analysis → CTI intelligence reports**

A production-ready threat intelligence automation system that ingests firewall logs, email headers, and SIEM alerts, then uses Claude AI to correlate indicators of compromise (IOCs), map MITRE ATT&CK techniques, and generate structured incident intelligence reports.

---

## 🎯 Why This Project?

This pipeline bridges **SOC operations** (what you do today) and **CTI roles** (where you want to go). It demonstrates:

✅ **SOC Skills:** Log analysis, alert triage, incident response  
✅ **CTI Skills:** IOC correlation, threat actor profiling, intelligence reporting  
✅ **Automation:** Multi-source data orchestration  
✅ **AI Application:** Claude for intelligent threat analysis  
✅ **Security Thinking:** MITRE ATT&CK, risk scoring, threat modeling  

**For Interview Conversations:**
- "I built a tool that correlates IOCs across multiple sources-firewall, email, SIEM-and generates threat intelligence reports with MITRE ATT&CK mapping."
- Shows you can handle unstructured security data and turn it into actionable intelligence.
- Perfect for CTI, Security Engineering, and advanced SOC roles.

---

## 🏗️ Architecture

```
Raw Data Inputs
    ↓
    ├── Firewall Logs (Sophos, Palo Alto, etc.)
    ├── Email Headers (Phishing, spoofing detection)
    └── SIEM Alerts (Splunk, ELK, etc.)
    ↓
[Threat Intelligence Pipeline]
    ↓
    ├── IOC Extraction (IPs, domains, hashes, emails)
    ├── Claude Analysis (Multi-turn conversation chain)
    ├── IOC Correlation (Cross-source pattern detection)
    ├── Risk Scoring (0-100 scale)
    └── MITRE ATT&CK Mapping
    ↓
Intelligence Output
    ├── JSON Report (Structured data)
    └── Markdown Report (Human-readable)
```

---

## 📋 Features

### Data Ingestion
- **Firewall Logs**: Sophos XGS, Palo Alto, FortiGate, Cisco (adapts to format)
- **Email Headers**: SPF/DKIM/DMARC validation, phishing detection, credential harvesting
- **SIEM Alerts**: Splunk, ELK, Datadog, or any structured alert format

### IOC Extraction
Automatically extracts and catalogues:
- **IPv4 Addresses** (including C2, data exfil destinations)
- **Domains** (phishing, malware hosting, C2)
- **Email Addresses** (spoofed, compromised accounts)
- **File Hashes** (MD5, SHA1, SHA256 for malware identification)
- **URLs** (phishing links, malware download URLs)

### Analysis & Correlation
- **Multi-turn Claude Prompts**: Threat analyst conversation chain
- **IOC Correlation**: Finds IOCs appearing across multiple sources (higher risk)
- **Risk Scoring**: 0-100 scale based on correlation + Claude assessment
- **MITRE ATT&CK Mapping**: Automatically maps tactics to adversary techniques

### Intelligence Reporting
- **Incident ID**: Unique incident tracking (INC-YYYYMMDDHHMMSS)
- **Severity Classification**: CRITICAL, HIGH, MEDIUM, LOW
- **Threat Actor Profile**: Attribution (APT28, etc.) if identifiable
- **IOC Summary**: All indicators in one place
- **Timeline**: Chronological event sequence
- **Recommendations**: IR playbook steps

### Output Formats
- **JSON**: Machine-readable, integrates with other tools
- **Markdown**: Human-readable reports for sharing
- Both auto-generated from single analysis run

---

## 🚀 Quick Start

### 1. Installation

```bash
# Clone or download project
cd threat-intel-pipeline

# Install dependencies
pip install -r requirements.txt

# Set up API key
export ANTHROPIC_API_KEY="your-api-key-here"
```

### 2. Basic Usage

```python
from threat_intel_pipeline import ThreatIntelligencePipeline

# Initialize pipeline
pipeline = ThreatIntelligencePipeline()

# Load your data
with open("firewall_logs.txt") as f:
    firewall_logs = f.read()

with open("email_headers.txt") as f:
    email_headers = f.read()

with open("siem_alerts.txt") as f:
    siem_alerts = f.read()

# Run analysis
report = pipeline.run_pipeline(
    firewall_logs=firewall_logs,
    email_headers=email_headers,
    siem_alerts=siem_alerts
)

# Save reports
pipeline.save_report(report, format='json')  # INC-20240320143215_report.json
pipeline.save_report(report, format='md')    # INC-20240320143215_report.md

# Print summary
print(json.dumps(report, indent=2))
```

### 3. Command Line

```bash
python threat_intel_pipeline.py
```

By default, runs with sample data included. Customize by editing `main()` function.

---

## 📊 Example Report Output

### JSON Output
```json
{
  "incident_id": "INC-20240320143215",
  "severity": "CRITICAL",
  "risk_score": 95,
  "summary": "APT28 attack targeting financial data. Multiple vectors: credential theft, lateral movement, data exfiltration.",
  "threat_actors": ["APT28", "Sofacy"],
  "iocs": {
    "ips": [
      {"value": "203.45.67.89", "type": "C2", "occurrences": 4},
      {"value": "210.12.34.56", "type": "data_exfil", "occurrences": 1}
    ],
    "domains": [
      {"value": "malicious-c2.ru", "occurrences": 3},
      {"value": "office365-verify-real.ru", "occurrences": 2}
    ]
  },
  "ttp_mapping": {
    "initial_access": "T1566.002 - Phishing: Spearphishing Link",
    "credential_access": "T1110.003 - Brute Force: Password Spraying",
    "lateral_movement": "T1570 - Lateral Tool Transfer",
    "exfiltration": "T1041 - Exfiltration Over C2 Channel"
  },
  "timeline": [
    "2024-03-20 14:32 - Suspicious RDP from 203.45.67.89",
    "2024-03-20 14:45 - Privilege escalation (Mimikatz)",
    "2024-03-20 15:12 - Lateral movement to file server",
    "2024-03-20 15:18 - Data exfiltration (2.3 GB)"
  ],
  "recommended_actions": [
    "Isolate affected workstations immediately",
    "Reset all administrative credentials",
    "Block IOCs at perimeter (firewall, proxy, DNS)",
    "Hunt for lateral movement indicators",
    "Preserve forensic evidence"
  ],
  "timestamp": "2024-03-20T15:25:00",
  "confidence_level": "HIGH"
}
```

### Markdown Output
```markdown
# Incident Report: INC-20240320143215

**Timestamp:** 2024-03-20T15:25:00
**Severity:** CRITICAL
**Risk Score:** 95/100

## Summary
APT28 attack targeting financial data. Multiple vectors including credential theft, lateral movement, and data exfiltration.

## Threat Actors
APT28, Sofacy

## IOCs
### IPs
- 203.45.67.89 (C2 - seen 4 times)
- 210.12.34.56 (Data exfil - seen 1 time)

### Domains
- malicious-c2.ru (seen 3 times)
- office365-verify-real.ru (seen 2 times)

## MITRE ATT&CK Techniques
- **Initial Access:** T1566.002 - Phishing: Spearphishing Link
- **Credential Access:** T1110.003 - Brute Force: Password Spraying
- **Lateral Movement:** T1570 - Lateral Tool Transfer
- **Exfiltration:** T1041 - Exfiltration Over C2 Channel

## Timeline
- 2024-03-20 14:32 - Suspicious RDP from 203.45.67.89
- 2024-03-20 14:45 - Privilege escalation (Mimikatz)
- 2024-03-20 15:12 - Lateral movement to file server
- 2024-03-20 15:18 - Data exfiltration (2.3 GB)

## Recommended Actions
1. Isolate affected workstations immediately
2. Reset all administrative credentials
3. Block IOCs at perimeter (firewall, proxy, DNS)
4. Hunt for lateral movement indicators
5. Preserve forensic evidence
```

---

## 🔧 How It Works

### Phase 1: IOC Extraction
```python
iocs = pipeline.extract_iocs(raw_data, source_type="firewall")
# Returns: {
#   'ips': ['203.45.67.89', '210.12.34.56'],
#   'domains': ['malicious-c2.ru'],
#   'hashes': ['a1b2c3d4e5f6...'],
#   ...
# }
```

### Phase 2: Claude Analysis (Multi-turn)
```
User: "Analyze these firewall logs..."
Claude: "I've identified C2 communication from 203.45.67.89 to malicious-c2.ru..."

User: "Analyze these email headers..."
Claude: "CEO fraud attempt with spoofed domain..."

User: "Analyze these SIEM alerts..."
Claude: "Privilege escalation detected (Mimikatz), lateral movement initiated..."
```

### Phase 3: Correlation
```python
correlations = pipeline.correlate_iocs()
# Finds: 203.45.67.89 appears in firewall AND email AND SIEM
#        = HIGHER CONFIDENCE = HIGHER RISK SCORE
```

### Phase 4: Risk Scoring
```
Base Risk Score: 0
+ Firewall blocks (5 critical): +40
+ Email phishing (2 critical): +30
+ SIEM alerts (5 critical): +25
= 95/100 (CRITICAL)
```

### Phase 5: Report Generation
Claude synthesizes all analysis into structured JSON + markdown report.

---

## 📁 File Structure

```
threat-intel-pipeline/
├── threat_intel_pipeline.py         # Main pipeline class
├── requirements.txt                 # Python dependencies
├── sample_firewall_logs.txt         # Sophos example data
├── sample_email_headers.txt         # Phishing example data
├── sample_siem_alerts.txt           # Incident example data
└── README.md                        # This file

# After running:
├── INC-20240320143215_report.json   # Generated
└── INC-20240320143215_report.md     # Generated
```

---

## 🛠️ Customization

### Add Your Own Data
```python
# Read real data
with open("your_firewall.log") as f:
    real_logs = f.read()

# Run pipeline
report = pipeline.run_pipeline(firewall_logs=real_logs)
```

### Customize IOC Patterns
Edit `extract_iocs()` method to add:
- File paths
- Registry keys
- SSL certificate thumbprints
- Custom indicators

### Enhance MITRE Mapping
Add more techniques to `MITRE_MAPPING` dictionary:
```python
MITRE_MAPPING = {
    "reconnaissance": "T1592",
    "resource_dev": "T1583",
    "initial_access": "T1566.002",
    ...
}
```

### Integrate Real SIEM/Firewall APIs
```python
# Example: Query Splunk directly
import splunklib.client as client

def get_splunk_alerts():
    siem = client.connect(host="splunk.corp.com", ...)
    results = siem.service.search("index=main severity=HIGH").results()
    return json.dumps(results)

alerts = get_splunk_alerts()
report = pipeline.run_pipeline(siem_alerts=alerts)
```

---

## 🎓 CTI Learning Path

This project teaches:

1. **Week 1**: IOC extraction and regex patterns
2. **Week 2**: IOC correlation and risk scoring
3. **Week 3**: MITRE ATT&CK framework mapping
4. **Week 4**: Threat actor attribution
5. **Week 5**: Multi-source intelligence fusion

Expand to:
- Integrate with VirusTotal API for hash reputation
- Connect to AlienVault OTX for threat feed data
- Build threat actor profiles from historical incidents
- Develop custom detection rules (Yara, Sigma)

---

## 🔐 Security Notes

- **API Key**: Store in `.env` file (never hardcode)
- **Data Sanitization**: Remove real IPs/domains before committing
- **Log Retention**: Follow company data governance policies
- **Access Control**: Restrict report access (contains sensitive IOCs)

```bash
# .env file (add to .gitignore)
ANTHROPIC_API_KEY=sk-ant-...
```

---

## 📚 Resources

**MITRE ATT&CK:**
- https://attack.mitre.org/

**Threat Intelligence Platforms:**
- VirusTotal: https://virustotal.com
- AlienVault OTX: https://otx.alienvault.com
- Shodan: https://shodan.io

**Incident Response Frameworks:**
- NIST Cybersecurity Framework
- SANS Incident Handler's Handbook
- MITRE Cyber Threat Intel Sharing Framework

---

## 💡 Interview Talking Points

**"What made you build this?"**
> I wanted to bridge the gap between SOC operations (where I am now) and CTI roles (where I want to go). This pipeline automates the tedious parts of threat analysis so analysts can focus on intelligence-profiling actors, predicting attacks, and building organizational resilience.

**"How does it work?"**
> It ingests multiple data sources-firewall logs, email headers, SIEM alerts-extracts IOCs (IPs, domains, hashes), correlates them across sources, and uses Claude AI to analyze patterns and map them to MITRE ATT&CK. Outputs a structured incident report with threat actor profile and risk score.

**"What's the security value?"**
> Reduces mean time to detect (MTTD) by automating correlation. A human analyst might take 2 hours to correlate IOCs across 3 systems; this does it in minutes. Also catches patterns humans might miss-same IP appearing in firewall, email, and SIEM = much higher confidence.

**"How would you use it in a real CTI team?"**
> Feed it daily alerts, aggregate reports by week, track threat actor campaigns over time, build threat intelligence feeds, and share IOCs with other organizations.

---

## 🚀 Next Steps

1. **Test it**: Run with sample data provided
2. **Customize it**: Add your real Sophos logs
3. **Deploy it**: Automate on schedule (cron, Lambda, etc.)
4. **Enhance it**: Add API integrations (VirusTotal, Slack alerts, MISP)
5. **Share it**: GitHub repo for portfolio

---

## 📞 Support

Questions or issues?
- Check sample data for format examples
- Review Claude documentation for prompt engineering
- Expand MITRE mapping for your threat landscape

---

**Built for: Cybersecurity Analysts, CTI Practitioners, Security Engineers**

**Use case: SOC → CTI Transition | Threat Intelligence Automation | Incident Response**

**Status: Production-Ready | Extensible | Open for Customization**
