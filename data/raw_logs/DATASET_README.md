# Dataset Generation Guide

## Overview

This directory contains tools to generate security log datasets for testing the threat detection pipeline.

## Dataset Generators

### 1. **generate_logs.py** (Main Generator - Enhanced)
The primary dataset generator that creates a comprehensive 50,000 log file with realistic security events.

**Features:**
- 12 different event types (AUTH_FAIL, AUTH_SUCCESS, PORT_SCAN, MALWARE_ALERT, SQL_INJECTION, DDoS_DETECTED, FILE_ACCESS, PRIVILEGE_ESCALATION, DATA_EXFILTRATION, FIREWALL_BLOCK, SUSPICIOUS_PROCESS, NETWORK_ANOMALY)
- 3 log categories:
  - **Normal Operations** (70%): 35,000 logs of typical business activities
  - **Attack Scenarios** (20%): 11,500 logs of intrusion attempts
  - **Anomalies** (10%): 5,000 logs of suspicious behavior
- Rich log fields: user, service, protocol, port, country, file access, etc.
- Event-specific attributes and payload data

**Run:**
```bash
python generate_logs.py
```

**Output:** `siem_logs.json` (50,000 entries)

---

### 2. **generate_extended_datasets.py** (Advanced Generator)
Creates multiple specialized datasets for different security scenarios.

**Datasets Generated:**

| Dataset | Count | Focus |
|---------|-------|-------|
| `siem_logs_normal.json` | 20,000 | Normal business operations |
| `siem_logs_attacks.json` | 10,000 | Network intrusions & attacks |
| `siem_logs_malware.json` | 5,000 | Malware & suspicious processes |
| `siem_logs_exfiltration.json` | 2,000 | Data theft attempts |
| `siem_logs_ddos.json` | 3,000 | DDoS attack patterns |
| `siem_logs_privilege.json` | 2,000 | Privilege escalation attempts |
| `siem_logs_combined.json` | 42,000 | Master file with all logs |

**Run:**
```bash
python generate_extended_datasets.py
```

---

## Log Entry Structure

### Standard Fields (All Logs)
```json
{
  "timestamp": "2026-02-19T12:34:56.789123",
  "source_ip": "192.168.1.45",
  "dest_ip": "192.168.1.100",
  "event_type": "AUTH_FAIL",
  "severity": 5,
  "system": "server-42",
  "service": "SSH",
  "user": "user123",
  "status_code": 401,
  "bytes_transferred": 1024,
  "response_time_ms": 250
}
```

### Event-Specific Fields

**AUTH_FAIL/AUTH_SUCCESS:**
- `user`: Username attempting login
- `service`: SSH, RDP, LDAP, etc.

**PORT_SCAN/NETWORK_ANOMALY:**
- `protocol`: TCP, UDP, ICMP
- `port`: Target port number
- `country`: Source country code

**SQL_INJECTION:**
- `query`: SQL query attempted
- `payload`: Injection payload
- `severity`: Always 9-10

**DDoS_DETECTED:**
- `packets_per_second`: Attack volume
- `requests_per_second`: Request rate
- `attack_type`: volumetric, protocol, application

**DATA_EXFILTRATION:**
- `file`: Name of file being transferred
- `file_size_mb`: File size
- `destination_domain`: Where data is going

**PRIVILEGE_ESCALATION:**
- `escalation_method`: How privilege was escalated
- `command`: Executed privileged command

**MALWARE_ALERT:**
- `malware_name`: Malware family name
- `process_id`: Process ID
- `file_path`: Location of malware

---

## IP Address Ranges

**Internal Network:**
- `192.168.1.1` - `192.168.1.254` (254 hosts)

**External/Attacker IPs:**
- `203.0.113.1` - `203.0.113.99` (100 hosts)

---

## Log Volume Scenarios

| Scenario | Total Logs | Use Case |
|----------|-----------|----------|
| **Baseline** | 50,000 | Standard testing |
| **High-Volume** | 42,000+ | Performance testing |
| **Scenario Testing** | Variable | Testing specific threats |

---

## Processing Pipeline

Generated logs flow through:

```
Raw Logs (siem_logs.json)
    ↓
ScaleDown Engine (aggregation by IP+event type)
    ↓
Log Analyzer Agent (feature extraction & risk scoring)
    ↓
Threat Detector Agent (ML anomaly detection)
    ↓
Response Coordinator (incident classification)
    ↓
Dashboard (visualization)
```

---

## Custom Dataset Creation

To create your own dataset, modify `generate_extended_datasets.py`:

```python
def generate_custom_dataset(filename, count=5000):
    print(f"Generating custom dataset...")
    with open(filename, "w") as f:
        for _ in range(count):
            log = {
                "timestamp": datetime.utcnow().isoformat(),
                "source_ip": "192.168.1.100",
                "event_type": "YOUR_EVENT_TYPE",
                "severity": 5,
                # ... more fields
            }
            f.write(json.dumps(log) + "\n")
```

---

## Tips for Testing

1. **Generate baseline** with `generate_logs.py` first
2. **Use specialized datasets** for specific threat testing
3. **Combine datasets** to test mixed scenarios
4. **Monitor sensitivity** of threat detector with different log volumes
5. **Compare detection rates** across different dataset compositions

