import json
import random
from datetime import datetime, timedelta

"""
Extended Dataset Generator
Creates multiple specialized datasets for different security scenarios
"""

# ==================== DATA DEFINITIONS ====================
COMMON_EVENTS = ["AUTH_FAIL", "AUTH_SUCCESS", "FILE_ACCESS", "FIREWALL_BLOCK"]
ATTACK_EVENTS = ["PORT_SCAN", "SQL_INJECTION", "PRIVILEGE_ESCALATION", "DATA_EXFILTRATION"]
CRITICAL_EVENTS = ["MALWARE_ALERT", "DDoS_DETECTED", "SUSPICIOUS_PROCESS"]

IPS_INTERNAL = [f"192.168.1.{i}" for i in range(1, 255)]
IPS_EXTERNAL = [f"203.0.113.{i}" for i in range(1, 100)]

USERS = [f"user{i}" for i in range(1, 500)] + ["admin", "root", "service", "guest"]
SERVICES = ["SSH", "HTTP", "HTTPS", "FTP", "SMB", "DNS", "LDAP", "SMTP", "RDP"]
COUNTRIES = ["US", "CN", "RU", "BR", "IN", "DE", "GB", "JP", "KR", "AU", "CA", "FR", "IL", "NK"]
DEPARTMENTS = ["IT", "Finance", "HR", "Engineering", "Sales", "Operations", "Security"]


def generate_normal_activity_log():
    """Normal business operations"""
    return {
        "timestamp": (datetime.utcnow() - timedelta(seconds=random.randint(0, 86400))).isoformat(),
        "source_ip": random.choice(IPS_INTERNAL),
        "dest_ip": random.choice(IPS_INTERNAL),
        "event_type": random.choice(COMMON_EVENTS),
        "severity": random.randint(1, 3),
        "system": f"server-{random.randint(1, 1000)}",
        "service": random.choice(SERVICES),
        "user": random.choice(USERS),
        "department": random.choice(DEPARTMENTS),
        "action": random.choice(["LOGIN", "LOGOUT", "READ", "WRITE"]),
        "status_code": random.choice([200, 201, 304]),
        "bytes_transferred": random.randint(100, 50000),
        "response_time_ms": random.randint(10, 500)
    }


def generate_intrusion_detection_log():
    """Network intrusion attempts"""
    return {
        "timestamp": (datetime.utcnow() - timedelta(seconds=random.randint(0, 86400))).isoformat(),
        "source_ip": random.choice(IPS_EXTERNAL),
        "dest_ip": random.choice(IPS_INTERNAL),
        "event_type": random.choice(ATTACK_EVENTS),
        "severity": random.randint(6, 9),
        "system": f"server-{random.randint(1, 200)}",
        "service": random.choice(SERVICES),
        "user": f"attacker-{random.randint(1, 100)}",
        "country": random.choice(COUNTRIES),
        "protocol": random.choice(["TCP", "UDP", "HTTP", "HTTPS"]),
        "port": random.choice([22, 80, 443, 3389, 445, 21, 5900]),
        "attack_type": random.choice(["brute_force", "sql_injection", "xss", "privilege_escalation"]),
        "payload": "malicious_payload",
        "status_code": random.choice([401, 403, 500]),
        "bytes_transferred": random.randint(1000, 100000),
        "response_time_ms": random.randint(100, 5000)
    }


def generate_malware_detection_log():
    """Malware and suspicious process detection"""
    return {
        "timestamp": (datetime.utcnow() - timedelta(seconds=random.randint(0, 86400))).isoformat(),
        "source_ip": random.choice(IPS_INTERNAL),
        "dest_ip": random.choice(IPS_INTERNAL),
        "event_type": random.choice(CRITICAL_EVENTS),
        "severity": random.randint(8, 10),
        "system": f"workstation-{random.randint(1, 500)}",
        "service": random.choice(SERVICES),
        "user": random.choice(USERS),
        "malware_name": random.choice(["Trojan.Win32.Zeus", "Ransomware.Wannacry", "Worm.Mirai"]),
        "process_id": random.randint(100, 9999),
        "file_path": random.choice(["C:\\Windows\\System32\\svchost.exe", "/usr/bin/bash", "/tmp/malware"]),
        "action": "QUARANTINE",
        "bytes_transferred": random.randint(10000, 1000000),
        "response_time_ms": random.randint(500, 10000)
    }


def generate_data_exfiltration_log():
    """Data theft and exfiltration attempts"""
    return {
        "timestamp": (datetime.utcnow() - timedelta(seconds=random.randint(0, 86400))).isoformat(),
        "source_ip": random.choice(IPS_INTERNAL),
        "dest_ip": random.choice(IPS_EXTERNAL),
        "event_type": "DATA_EXFILTRATION",
        "severity": 10,
        "system": f"server-{random.randint(1, 500)}",
        "service": "HTTPS",
        "user": random.choice(USERS),
        "country": random.choice(COUNTRIES),
        "file": random.choice(["passwords.csv", "customer_data.xlsx", "financial_records.db", "secrets.env"]),
        "file_size_mb": random.randint(1, 5000),
        "destination_domain": random.choice(["attacker.com", "c2.malware.net", "data-theft.io"]),
        "action": "FILE_TRANSFER",
        "bytes_transferred": random.randint(1000000, 10000000),
        "response_time_ms": random.randint(1000, 30000)
    }


def generate_ddos_log():
    """Distributed Denial of Service attack logs"""
    return {
        "timestamp": (datetime.utcnow() - timedelta(seconds=random.randint(0, 86400))).isoformat(),
        "source_ip": random.choice(IPS_EXTERNAL),
        "dest_ip": random.choice(IPS_INTERNAL),
        "event_type": "DDoS_DETECTED",
        "severity": 10,
        "system": "load-balancer-1",
        "service": random.choice(["HTTP", "HTTPS", "DNS"]),
        "protocol": random.choice(["TCP", "UDP"]),
        "port": random.choice([80, 443, 53]),
        "packets_per_second": random.randint(10000, 1000000),
        "requests_per_second": random.randint(1000, 100000),
        "attack_type": random.choice(["volumetric", "protocol", "application"]),
        "country": random.choice(COUNTRIES),
        "response_time_ms": random.randint(5000, 30000)
    }


def generate_privilege_abuse_log():
    """Unauthorized privilege escalation and abuse"""
    return {
        "timestamp": (datetime.utcnow() - timedelta(seconds=random.randint(0, 86400))).isoformat(),
        "source_ip": random.choice(IPS_INTERNAL),
        "dest_ip": random.choice(IPS_INTERNAL),
        "event_type": "PRIVILEGE_ESCALATION",
        "severity": random.randint(7, 10),
        "system": f"server-{random.randint(1, 1000)}",
        "service": random.choice(["SSH", "RDP", "LDAP"]),
        "user": random.choice(USERS),
        "escalation_method": random.choice(["sudo_abuse", "privesc_exploit", "credential_theft"]),
        "action": "EXECUTE_PRIVILEGED",
        "command": random.choice(["rm -rf /", "del /s /q C:\\", "chmod 777 *"]),
        "status_code": random.choice([200, 401, 403]),
        "response_time_ms": random.randint(100, 2000)
    }


# ==================== GENERATE MULTIPLE DATASETS ====================

def generate_dataset_normal(filename, count=20000):
    """Normal business operations dataset"""
    print(f"Generating {count} normal activity logs to {filename}...")
    with open(filename, "w") as f:
        for _ in range(count):
            f.write(json.dumps(generate_normal_activity_log()) + "\n")
    print(f"✓ {filename} created")


def generate_dataset_attacks(filename, count=10000):
    """Network attacks dataset"""
    print(f"Generating {count} network attack logs to {filename}...")
    with open(filename, "w") as f:
        for _ in range(count):
            f.write(json.dumps(generate_intrusion_detection_log()) + "\n")
    print(f"✓ {filename} created")


def generate_dataset_malware(filename, count=5000):
    """Malware detection dataset"""
    print(f"Generating {count} malware detection logs to {filename}...")
    with open(filename, "w") as f:
        for _ in range(count):
            f.write(json.dumps(generate_malware_detection_log()) + "\n")
    print(f"✓ {filename} created")


def generate_dataset_exfiltration(filename, count=2000):
    """Data exfiltration dataset"""
    print(f"Generating {count} data exfiltration logs to {filename}...")
    with open(filename, "w") as f:
        for _ in range(count):
            f.write(json.dumps(generate_data_exfiltration_log()) + "\n")
    print(f"✓ {filename} created")


def generate_dataset_ddos(filename, count=3000):
    """DDoS attack dataset"""
    print(f"Generating {count} DDoS attack logs to {filename}...")
    with open(filename, "w") as f:
        for _ in range(count):
            f.write(json.dumps(generate_ddos_log()) + "\n")
    print(f"✓ {filename} created")


def generate_dataset_privilege(filename, count=2000):
    """Privilege escalation dataset"""
    print(f"Generating {count} privilege escalation logs to {filename}...")
    with open(filename, "w") as f:
        for _ in range(count):
            f.write(json.dumps(generate_privilege_abuse_log()) + "\n")
    print(f"✓ {filename} created")


# ==================== MAIN EXECUTION ====================

if __name__ == "__main__":
    print("\n🔐 Security Dataset Generator - Extended\n")
    
    # Generate individual datasets
    generate_dataset_normal("siem_logs_normal.json", 20000)
    generate_dataset_attacks("siem_logs_attacks.json", 10000)
    generate_dataset_malware("siem_logs_malware.json", 5000)
    generate_dataset_exfiltration("siem_logs_exfiltration.json", 2000)
    generate_dataset_ddos("siem_logs_ddos.json", 3000)
    generate_dataset_privilege("siem_logs_privilege.json", 2000)
    
    # Combine all datasets into one master log file
    print("\nCombining datasets into master log file...")
    with open("siem_logs_combined.json", "w") as outfile:
        for filename in ["siem_logs_normal.json", "siem_logs_attacks.json", "siem_logs_malware.json",
                        "siem_logs_exfiltration.json", "siem_logs_ddos.json", "siem_logs_privilege.json"]:
            with open(filename, "r") as infile:
                for line in infile:
                    outfile.write(line)
    
    total_logs = 20000 + 10000 + 5000 + 2000 + 3000 + 2000
    print(f"\n✅ Dataset generation complete!")
    print(f"   Total logs generated: {total_logs:,}")
    print(f"   Files created:")
    print(f"   - siem_logs_normal.json (20,000 logs)")
    print(f"   - siem_logs_attacks.json (10,000 logs)")
    print(f"   - siem_logs_malware.json (5,000 logs)")
    print(f"   - siem_logs_exfiltration.json (2,000 logs)")
    print(f"   - siem_logs_ddos.json (3,000 logs)")
    print(f"   - siem_logs_privilege.json (2,000 logs)")
    print(f"   - siem_logs_combined.json ({total_logs:,} logs)\n")
