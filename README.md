# Threat Intelligence Pipeline

Automates threat analysis by ingesting firewall logs, email headers, and SIEM alerts to extract and correlate Indicators of Compromise (IOCs), map them to MITRE ATT&CK techniques, and generate structured threat intelligence reports.

---

## Key Features

* IOC extraction (IPs, domains, hashes, URLs)
* Cross-source correlation (Firewall, Email, SIEM)
* MITRE ATT&CK mapping
* Risk scoring and threat identification
* Automated report generation (JSON and Markdown)

---

## Sample Output

Example of generated incident report:

Incident ID: INC-20260323072520
Severity: CRITICAL
Risk Score: 95

Summary:
Advanced Persistent Threat (APT28) campaign involving phishing, credential theft, lateral movement, and data exfiltration.

IOCs:

* IP: 203.45.67.89 (C2)
* Domain: malicious-c2.ru
* Hash: a1b2c3d4e5f6...

MITRE Techniques:

* T1566.002 (Phishing)
* T1059 (Command Execution)
* T1570 (Lateral Movement)

---

## How It Works

1. Ingests raw security data from multiple sources
2. Extracts IOCs using pattern matching (regex)
3. Correlates indicators across sources
4. Maps activity to MITRE ATT&CK techniques
5. Generates structured threat intelligence reports

---

## Tech Stack

* Python
* Regex-based IOC extraction
* MITRE ATT&CK Framework
* AI-assisted analysis (Claude API)

---

## Quick Start

```bash
pip install -r requirements.txt
python threat_intel_pipeline_demo.py
```

---

## Use Case

Designed to automate SOC workflows and support transition into Cyber Threat Intelligence (CTI) roles by reducing manual analysis effort and improving detection accuracy.

---

## Author

Kartik Sawant
Cyber Security Analyst | SOC → CTI | Threat Intelligence

---

## Project Status

Completed and used for portfolio demonstration.
