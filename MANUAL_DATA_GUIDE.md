# Manual Data Injection Guide

## Overview

There are **three ways** to add manual test data to the security dashboard:

1. **CLI Tool** (Easiest) - Command-line data injector
2. **Direct File Editing** (Manual) - Edit JSON files directly
3. **API Endpoint** (Programmatic) - POST requests to backend

---

## Method 1: CLI Data Injector (Recommended)

### Installation
No installation needed - just run the Python script.

### Viewing Available Presets
```bash
cd d:\Coding\Pj
python data_injector.py presets
```

**Output shows:**
- sql_injection
- ddos_attack
- malware
- brute_force
- port_scan
- privilege_escalation
- data_exfiltration

### Adding Preset Threats

**Add a SQL Injection threat:**
```bash
python data_injector.py add-preset sql_injection
```

**Add a DDoS attack threat:**
```bash
python data_injector.py add-preset ddos_attack
```

**Add a Malware detection:**
```bash
python data_injector.py add-preset malware
```

**Add a Brute Force attack:**
```bash
python data_injector.py add-preset brute_force
```

### Adding Custom Threats

**Format:**
```bash
python data_injector.py add-threat <IP> <EVENT_TYPE> <RISK_SCORE> <THREAT_LEVEL>
```

**Examples:**
```bash
# Add custom threat from IP 192.168.1.50
python data_injector.py add-threat 192.168.1.50 MALWARE_ALERT 85 CRITICAL

# Add suspicious port scan activity
python data_injector.py add-threat 203.0.113.25 PORT_SCAN 70 HIGH

# Add failed auth attempts
python data_injector.py add-threat 192.168.1.100 AUTH_FAIL 55 MEDIUM
```

**Threat Levels:**
- `CRITICAL` - Risk score 80+
- `HIGH` - Risk score 65-79
- `MEDIUM` - Risk score 50-64

**Event Types:**
- PORT_SCAN
- SQL_INJECTION
- MALWARE_ALERT
- AUTH_FAIL
- DDoS_DETECTED
- PRIVILEGE_ESCALATION
- DATA_EXFILTRATION
- FIREWALL_BLOCK
- SUSPICIOUS_PROCESS
- NETWORK_ANOMALY

### Adding Incidents
```bash
python data_injector.py add-incident <INCIDENT_ID> <SOURCE_IP> <SEVERITY>
```

**Examples:**
```bash
# Create critical incident
python data_injector.py add-incident INC-001 192.168.1.50 CRITICAL

# Create high severity incident
python data_injector.py add-incident INC-002 203.0.113.10 HIGH

# Create medium severity incident
python data_injector.py add-incident INC-003 192.168.1.75 MEDIUM
```

### Viewing Current Data
```bash
python data_injector.py list
```

Shows last 5 threats and incidents currently in the dashboard.

### Clearing Data
```bash
# Clear all threats
python data_injector.py clear-threats

# Clear all incidents
python data_injector.py clear-incidents
```

### View Data Format Examples
```bash
python data_injector.py samples
```

---

## Method 2: Manual File Editing

### Location
```
d:\Coding\Pj\data\scaled_logs\
├── detected_threats.json
├── incidents.json
├── analyzed_logs.json
└── scaled_logs.json
```

### Threat Data Format
**File:** `detected_threats.json`

```json
{
  "source_ip": "192.168.1.100",
  "event_type": "SQL_INJECTION",
  "event_count": 5,
  "max_severity": 9,
  "is_bruteforce": false,
  "is_port_scan": false,
  "is_malware": false,
  "risk_score": 85,
  "label": "SUSPICIOUS",
  "anomaly_score": -0.5,
  "detection_reason": "RULE_BASED",
  "threat_level": "CRITICAL"
}
```

**To add manually:**
1. Open `data/scaled_logs/detected_threats.json` in a text editor
2. Go to the end of the file
3. Add a new line with your JSON threat data
4. Save the file
5. Refresh the dashboard in your browser

### Incident Data Format
**File:** `incidents.json`

```json
{
  "incident_id": "INC-CUSTOM-001",
  "source_ip": "192.168.1.50",
  "event_type": "SECURITY_INCIDENT",
  "severity": "CRITICAL",
  "actions_taken": ["block_ip", "isolate_system", "notify_soc", "generate_ticket"],
  "timestamp": "2026-02-19T12:34:56.789123"
}
```

**To add manually:**
1. Open `data/scaled_logs/incidents.json`
2. Add your incident JSON at the end
3. Save and refresh dashboard

### Analyzed Log Format
**File:** `analyzed_logs.json`

```json
{
  "source_ip": "192.168.1.100",
  "event_type": "PORT_SCAN",
  "event_count": 15,
  "max_severity": 7,
  "is_bruteforce": false,
  "is_port_scan": true,
  "is_malware": false,
  "risk_score": 50,
  "label": "SUSPICIOUS"
}
```

---

## Method 3: Using the API Endpoint

### Run Pipeline Endpoint
```bash
curl -X POST http://localhost:5000/api/run-pipeline
```

This re-runs the entire security pipeline, which will:
1. Generate new log data
2. Scale down logs
3. Analyze logs
4. Detect threats
5. Create incidents

### Response
```json
{
  "status": "success",
  "message": "Pipeline executed successfully",
  "data": {
    "threats": [...],
    "incidents": [...]
  }
}
```

---

## Quick Test Scenarios

### Scenario 1: Add Multiple Critical Threats
```bash
python data_injector.py add-preset sql_injection
python data_injector.py add-preset ddos_attack
python data_injector.py add-preset malware
python data_injector.py add-preset privilege_escalation
```

### Scenario 2: Simulate Attack Chain
```bash
# 1. Port scan reconnaissance
python data_injector.py add-preset port_scan

# 2. Brute force login attempt
python data_injector.py add-preset brute_force

# 3. Privilege escalation
python data_injector.py add-preset privilege_escalation

# 4. Data exfiltration
python data_injector.py add-preset data_exfiltration

# 5. Create incident
python data_injector.py add-incident INC-ATTACK-001 203.0.113.42 CRITICAL
```

### Scenario 3: Test Dashboard Responsiveness
```bash
# Add 10 different threats
for i in {1..10}; do
  python data_injector.py add-threat 203.0.113.$i MALWARE_ALERT 80 CRITICAL
done
```

---

## Validation Checklist

After adding data:

✓ **Check Terminal 1 (API Server)** - Look for any errors
✓ **Refresh Dashboard** - `http://localhost:5174/`
✓ **Check Threats Panel** - New threats should appear
✓ **Check Incidents Panel** - New incidents should appear
✓ **Check KPI Cards** - Counts should update

---

## Troubleshooting

### Data Not Appearing in Dashboard
1. **Clear browser cache** (Ctrl+Shift+Del)
2. **Hard refresh** the dashboard (Ctrl+F5)
3. **Check the API** - Browse to `http://localhost:5000/api/data`
4. **Verify file format** - Ensure valid JSON (no trailing commas)

### Invalid JSON Error
The JSON format must be valid. Check:
- All strings are in double quotes
- No trailing commas
- Boolean values are lowercase: `true`, `false`
- Each entry on its own line (for JSONL format)

### File Not Found Error
Ensure the `data/scaled_logs/` directory exists:
```bash
mkdir data\scaled_logs
```

---

## Example Full Workflow

```bash
# 1. Start with fresh data
python data_injector.py clear-threats
python data_injector.py clear-incidents

# 2. Add preset threats
python data_injector.py add-preset sql_injection
python data_injector.py add-preset ddos_attack
python data_injector.py add-preset malware

# 3. Add custom threats
python data_injector.py add-threat 192.168.1.75 AUTH_FAIL 60 HIGH
python data_injector.py add-threat 203.0.113.99 PORT_SCAN 70 HIGH

# 4. Create incidents
python data_injector.py add-incident INC-001 192.168.1.100 CRITICAL
python data_injector.py add-incident INC-002 203.0.113.42 HIGH

# 5. View what was added
python data_injector.py list

# 6. Refresh dashboard browser and verify
```

---

## Dashboard Data Flow

```
Manual Data Entry
       ↓
detected_threats.json ─┐
incidents.json ────────┤
analyzed_logs.json ────┤
                       ↓
                  api_server.py
                       ↓
                  Dashboard (http://localhost:5174/)
```

Data is read from JSON files on every API request, so changes appear immediately after refresh!

