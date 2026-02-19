#!/usr/bin/env python3
"""
Manual Data Injector - Add custom test data to the dashboard
Allows you to manually inject threats, incidents, and logs for testing
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timedelta

# Data directory
DATA_DIR = Path("data/scaled_logs")
DATA_DIR.mkdir(parents=True, exist_ok=True)

# ==================== DATA TEMPLATES ====================

THREAT_TEMPLATE = {
    "source_ip": "192.168.1.100",
    "event_type": "SQL_INJECTION",
    "event_count": 5,
    "max_severity": 9,
    "is_bruteforce": False,
    "is_port_scan": False,
    "is_malware": False,
    "risk_score": 85,
    "label": "SUSPICIOUS",
    "anomaly_score": -0.5,
    "detection_reason": "RULE_BASED",
    "threat_level": "CRITICAL"
}

INCIDENT_TEMPLATE = {
    "incident_id": "INC-MANUAL-001",
    "source_ip": "192.168.1.100",
    "event_type": "SQL_INJECTION",
    "severity": "CRITICAL",
    "actions_taken": ["block_ip", "isolate_system", "notify_soc", "generate_ticket"],
    "timestamp": datetime.utcnow().isoformat()
}

ANALYZED_LOG_TEMPLATE = {
    "source_ip": "192.168.1.100",
    "event_type": "PORT_SCAN",
    "event_count": 15,
    "max_severity": 7,
    "is_bruteforce": False,
    "is_port_scan": True,
    "is_malware": False,
    "risk_score": 50,
    "label": "SUSPICIOUS"
}

# ==================== THREAT DATA PRESETS ====================

THREAT_PRESETS = {
    "sql_injection": {
        "source_ip": "203.0.113.42",
        "event_type": "SQL_INJECTION",
        "event_count": 8,
        "max_severity": 10,
        "is_bruteforce": False,
        "is_port_scan": False,
        "is_malware": False,
        "risk_score": 95,
        "label": "SUSPICIOUS",
        "anomaly_score": -0.8,
        "detection_reason": "RULE_BASED",
        "threat_level": "CRITICAL"
    },
    "ddos_attack": {
        "source_ip": "203.0.113.88",
        "event_type": "DDoS_DETECTED",
        "event_count": 50000,
        "max_severity": 10,
        "is_bruteforce": False,
        "is_port_scan": False,
        "is_malware": False,
        "risk_score": 100,
        "label": "SUSPICIOUS",
        "anomaly_score": -0.95,
        "detection_reason": "ML_ANOMALY",
        "threat_level": "CRITICAL"
    },
    "malware": {
        "source_ip": "192.168.1.150",
        "event_type": "MALWARE_ALERT",
        "event_count": 12,
        "max_severity": 10,
        "is_bruteforce": False,
        "is_port_scan": False,
        "is_malware": True,
        "risk_score": 90,
        "label": "SUSPICIOUS",
        "anomaly_score": -0.7,
        "detection_reason": "RULE_BASED",
        "threat_level": "CRITICAL"
    },
    "brute_force": {
        "source_ip": "203.0.113.15",
        "event_type": "AUTH_FAIL",
        "event_count": 100,
        "max_severity": 6,
        "is_bruteforce": True,
        "is_port_scan": False,
        "is_malware": False,
        "risk_score": 75,
        "label": "SUSPICIOUS",
        "anomaly_score": -0.6,
        "detection_reason": "RULE_BASED",
        "threat_level": "HIGH"
    },
    "port_scan": {
        "source_ip": "203.0.113.99",
        "event_type": "PORT_SCAN",
        "event_count": 50,
        "max_severity": 8,
        "is_bruteforce": False,
        "is_port_scan": True,
        "is_malware": False,
        "risk_score": 65,
        "label": "SUSPICIOUS",
        "anomaly_score": -0.4,
        "detection_reason": "RULE_BASED",
        "threat_level": "HIGH"
    },
    "privilege_escalation": {
        "source_ip": "192.168.1.75",
        "event_type": "PRIVILEGE_ESCALATION",
        "event_count": 3,
        "max_severity": 10,
        "is_bruteforce": False,
        "is_port_scan": False,
        "is_malware": False,
        "risk_score": 88,
        "label": "SUSPICIOUS",
        "anomaly_score": -0.7,
        "detection_reason": "ML_ANOMALY",
        "threat_level": "CRITICAL"
    },
    "data_exfiltration": {
        "source_ip": "192.168.1.200",
        "event_type": "DATA_EXFILTRATION",
        "event_count": 5,
        "max_severity": 10,
        "is_bruteforce": False,
        "is_port_scan": False,
        "is_malware": False,
        "risk_score": 98,
        "label": "SUSPICIOUS",
        "anomaly_score": -0.9,
        "detection_reason": "RULE_BASED",
        "threat_level": "CRITICAL"
    }
}

# ==================== UTILITY FUNCTIONS ====================

def append_to_json_file(filename, data):
    """Append a new JSON object to a line-delimited JSON file"""
    filepath = DATA_DIR / filename
    try:
        with open(filepath, "a") as f:
            f.write(json.dumps(data) + "\n")
        print(f"✓ Added to {filename}")
        return True
    except Exception as e:
        print(f"❌ Error adding to {filename}: {e}")
        return False

def load_json_lines(filename):
    """Load all entires from a line-delimited JSON file"""
    filepath = DATA_DIR / filename
    data = []
    try:
        with open(filepath, "r") as f:
            for line in f:
                if line.strip():
                    data.append(json.loads(line))
        return data
    except Exception as e:
        print(f"❌ Error loading {filename}: {e}")
        return []

def clear_file(filename):
    """Clear all contents of a file"""
    filepath = DATA_DIR / filename
    try:
        open(filepath, "w").close()
        print(f"✓ Cleared {filename}")
        return True
    except Exception as e:
        print(f"❌ Error clearing {filename}: {e}")
        return False

# ==================== MANUAL DATA INJECTION ====================

def add_custom_threat(source_ip, event_type, risk_score, threat_level):
    """Add a custom threat"""
    threat = {
        "source_ip": source_ip,
        "event_type": event_type,
        "event_count": 1,
        "max_severity": 10 if threat_level == "CRITICAL" else 7,
        "is_bruteforce": event_type == "AUTH_FAIL",
        "is_port_scan": event_type == "PORT_SCAN",
        "is_malware": event_type == "MALWARE_ALERT",
        "risk_score": risk_score,
        "label": "SUSPICIOUS",
        "anomaly_score": -0.5,
        "detection_reason": "RULE_BASED",
        "threat_level": threat_level
    }
    return append_to_json_file("detected_threats.json", threat)

def add_preset_threat(preset_name):
    """Add a predefined threat scenario"""
    if preset_name not in THREAT_PRESETS:
        print(f"❌ Unknown preset: {preset_name}")
        print(f"   Available: {', '.join(THREAT_PRESETS.keys())}")
        return False
    
    threat = THREAT_PRESETS[preset_name].copy()
    threat_name = preset_name.upper()
    return append_to_json_file("detected_threats.json", threat)

def add_incident(incident_id, source_ip, severity, actions):
    """Add a security incident"""
    incident = {
        "incident_id": incident_id,
        "source_ip": source_ip,
        "event_type": "SECURITY_INCIDENT",
        "severity": severity,
        "actions_taken": actions,
        "timestamp": datetime.utcnow().isoformat()
    }
    return append_to_json_file("incidents.json", incident)

def show_samples():
    """Show sample data formats"""
    print("\n" + "="*70)
    print("SAMPLE DATA FORMATS")
    print("="*70)
    
    print("\n📌 THREAT FORMAT:")
    print(json.dumps(THREAT_TEMPLATE, indent=2))
    
    print("\n📌 INCIDENT FORMAT:")
    print(json.dumps(INCIDENT_TEMPLATE, indent=2))
    
    print("\n📌 ANALYZED LOG FORMAT:")
    print(json.dumps(ANALYZED_LOG_TEMPLATE, indent=2))

def show_presets():
    """Show available threat presets"""
    print("\n" + "="*70)
    print("AVAILABLE THREAT PRESETS")
    print("="*70)
    
    for preset_name, preset_data in THREAT_PRESETS.items():
        print(f"\n🔴 {preset_name.upper()}")
        print(f"   Event Type: {preset_data['event_type']}")
        print(f"   Risk Score: {preset_data['risk_score']}")
        print(f"   Threat Level: {preset_data['threat_level']}")
        print(f"   Source IP: {preset_data['source_ip']}")

def list_current_data():
    """List current threats and incidents"""
    print("\n" + "="*70)
    print("CURRENT DATA IN DASHBOARD")
    print("="*70)
    
    threats = load_json_lines("detected_threats.json")
    print(f"\n📊 Threats ({len(threats)} total):")
    for i, threat in enumerate(threats[-5:], 1):  # Last 5
        print(f"   {i}. {threat['source_ip']} - {threat['event_type']} ({threat['threat_level']})")
    
    incidents = load_json_lines("incidents.json")
    print(f"\n📋 Incidents ({len(incidents)} total):")
    if incidents:
        for i, incident in enumerate(incidents[-5:], 1):  # Last 5
            print(f"   {i}. {incident['incident_id']} - {incident['severity']}")
    else:
        print("   (None)")

# ==================== CLI INTERFACE ====================

def main():
    if len(sys.argv) < 2:
        print("\n🔐 Manual Data Injector for Security Dashboard\n")
        print("Usage:")
        print("  python data_injector.py add-preset <name>              Add a preset threat")
        print("  python data_injector.py add-threat <ip> <type> <risk> <level>  Add custom threat")
        print("  python data_injector.py add-incident <id> <ip> <severity>      Add incident")
        print("  python data_injector.py presets                        Show available presets")
        print("  python data_injector.py samples                        Show data formats")
        print("  python data_injector.py list                           List current data")
        print("  python data_injector.py clear-threats                  Clear all threats")
        print("  python data_injector.py clear-incidents                Clear all incidents\n")
        print("Examples:")
        print("  python data_injector.py add-preset sql_injection")
        print("  python data_injector.py add-threat 192.168.1.50 MALWARE_ALERT 80 HIGH")
        print("  python data_injector.py add-incident INC-001 192.168.1.50 CRITICAL")
        print()
        return
    
    command = sys.argv[1].lower()
    
    if command == "add-preset":
        if len(sys.argv) < 3:
            print("❌ Please specify preset name")
            print(f"   Available: {', '.join(THREAT_PRESETS.keys())}")
            return
        add_preset_threat(sys.argv[2])
        print(f"✓ Preset threat added: {sys.argv[2]}")
        
    elif command == "add-threat":
        if len(sys.argv) < 6:
            print("❌ Format: add-threat <ip> <type> <risk_score> <level>")
            print("   Example: add-threat 192.168.1.50 MALWARE_ALERT 85 CRITICAL")
            return
        ip, event_type, risk_score, level = sys.argv[2], sys.argv[3], int(sys.argv[4]), sys.argv[5]
        add_custom_threat(ip, event_type, risk_score, level)
        
    elif command == "add-incident":
        if len(sys.argv) < 5:
            print("❌ Format: add-incident <id> <ip> <severity>")
            print("   Example: add-incident INC-001 192.168.1.50 CRITICAL")
            return
        incident_id, ip, severity = sys.argv[2], sys.argv[3], sys.argv[4]
        priority_actions = {
            "CRITICAL": ["block_ip", "isolate_system", "notify_soc", "generate_ticket"],
            "HIGH": ["block_ip", "notify_soc", "generate_ticket"],
            "MEDIUM": ["notify_soc", "log_event"]
        }
        actions = priority_actions.get(severity, ["log_event"])
        add_incident(incident_id, ip, severity, actions)
        
    elif command == "presets":
        show_presets()
        
    elif command == "samples":
        show_samples()
        
    elif command == "list":
        list_current_data()
        
    elif command == "clear-threats":
        clear_file("detected_threats.json")
        
    elif command == "clear-incidents":
        clear_file("incidents.json")
        
    else:
        print(f"❌ Unknown command: {command}")

if __name__ == "__main__":
    main()
