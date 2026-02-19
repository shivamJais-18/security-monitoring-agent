import json
import random
from datetime import datetime, timedelta

# ==================== EXTENDED LOG TYPES ====================
LOG_TYPES = [
    "AUTH_FAIL",
    "AUTH_SUCCESS",
    "PORT_SCAN",
    "MALWARE_ALERT",
    "SQL_INJECTION",
    "DDoS_DETECTED",
    "FILE_ACCESS",
    "PRIVILEGE_ESCALATION",
    "DATA_EXFILTRATION",
    "FIREWALL_BLOCK",
    "SUSPICIOUS_PROCESS",
    "NETWORK_ANOMALY"
]

# ==================== EXTENDED DATA ====================
IPS = [f"192.168.1.{i}" for i in range(1, 255)]
EXTERNAL_IPS = [f"203.0.113.{i}" for i in range(1, 100)]
USERS = [f"user{i}" for i in range(1, 500)] + ["admin", "root", "service"]
SERVICES = ["SSH", "HTTP", "HTTPS", "FTP", "SMB", "DNS", "LDAP", "SMTP", "RDP"]
PROTOCOLS = ["TCP", "UDP", "ICMP", "HTTP", "HTTPS", "SSH", "TLS"]
PORTS = [22, 80, 443, 3389, 445, 21, 25, 53, 389, 5432, 3306, 27017, 5900, 8080]
ACTIONS = ["LOGIN", "LOGOUT", "CREATE", "DELETE", "MODIFY", "READ", "EXECUTE", "TRANSFER"]
FILES = ["config.json", "password.txt", "database.sql", "creds.xlsx", "secrets.env", "payroll.csv"]
COUNTRIES = ["US", "CN", "RU", "BR", "IN", "DE", "GB", "JP", "KR", "AU", "CA", "FR"]

# ==================== REALISTIC LOG GENERATOR ====================
def generate_log():
    event_type = random.choice(LOG_TYPES)
    severity = random.randint(1, 10)
    
    # Adjust severity based on event type
    severity_map = {
        "AUTH_FAIL": random.randint(2, 5),
        "AUTH_SUCCESS": random.randint(1, 2),
        "PORT_SCAN": random.randint(6, 9),
        "MALWARE_ALERT": random.randint(8, 10),
        "SQL_INJECTION": random.randint(7, 10),
        "DDoS_DETECTED": random.randint(8, 10),
        "FILE_ACCESS": random.randint(2, 4),
        "PRIVILEGE_ESCALATION": random.randint(7, 10),
        "DATA_EXFILTRATION": random.randint(8, 10),
        "FIREWALL_BLOCK": random.randint(3, 6),
        "SUSPICIOUS_PROCESS": random.randint(6, 9),
        "NETWORK_ANOMALY": random.randint(5, 8)
    }
    severity = severity_map.get(event_type, severity)
    
    log = {
        "timestamp": (datetime.utcnow() - timedelta(seconds=random.randint(0, 86400))).isoformat(),
        "source_ip": random.choice(IPS + EXTERNAL_IPS),
        "dest_ip": random.choice(IPS),
        "event_type": event_type,
        "severity": severity,
        "system": f"server-{random.randint(1, 1000)}",
        "service": random.choice(SERVICES),
        "protocol": random.choice(PROTOCOLS),
        "port": random.choice(PORTS),
        "user": random.choice(USERS),
        "action": random.choice(ACTIONS),
        "country": random.choice(COUNTRIES),
        "status_code": random.choice([200, 401, 403, 404, 500, 502, 503]),
        "bytes_transferred": random.randint(100, 1000000),
        "response_time_ms": random.randint(1, 5000)
    }
    
    # Add event-specific fields
    if event_type in ["FILE_ACCESS", "DATA_EXFILTRATION"]:
        log["file"] = random.choice(FILES)
    
    if event_type == "DDoS_DETECTED":
        log["packets_per_second"] = random.randint(1000, 100000)
        
    if event_type == "SQL_INJECTION":
        log["query"] = "SELECT * FROM users WHERE id=1 OR 1=1"
        log["payload"] = "1' OR '1'='1"
    
    return log

# ==================== GENERATE MULTIPLE DATASETS ====================

# Dataset 1: Normal Operations (70% of logs)
print("Generating normal operation logs...")
with open("siem_logs.json", "w") as f:
    for _ in range(35000):
        log = generate_log()
        # Weight towards normal events
        log["event_type"] = random.choice(["AUTH_SUCCESS", "FILE_ACCESS", "AUTH_FAIL", "FIREWALL_BLOCK"])
        log["severity"] = random.randint(1, 4)
        f.write(json.dumps(log) + "\n")


# Dataset 2: Attack Scenarios (20% of logs)
print("Generating attack scenario logs...")
with open("siem_logs.json", "a") as f:
    attack_patterns = [
        {"event_type": "AUTH_FAIL", "severity": 5, "count": 3000},
        {"event_type": "PORT_SCAN", "severity": 7, "count": 2000},
        {"event_type": "SQL_INJECTION", "severity": 9, "count": 1500},
        {"event_type": "DDoS_DETECTED", "severity": 10, "count": 2500},
        {"event_type": "PRIVILEGE_ESCALATION", "severity": 9, "count": 1000},
        {"event_type": "DATA_EXFILTRATION", "severity": 10, "count": 1500},
    ]
    
    for pattern in attack_patterns:
        for _ in range(pattern["count"]):
            log = generate_log()
            log["event_type"] = pattern["event_type"]
            log["severity"] = pattern["severity"]
            f.write(json.dumps(log) + "\n")

# Dataset 3: Anomalies (10% of logs)
print("Generating anomalous behavior logs...")
with open("siem_logs.json", "a") as f:
    for _ in range(5000):
        log = generate_log()
        log["event_type"] = random.choice(["SUSPICIOUS_PROCESS", "NETWORK_ANOMALY", "MALWARE_ALERT"])
        log["severity"] = random.randint(6, 10)
        f.write(json.dumps(log) + "\n")

print("✓ Dataset generation complete: 50,000 logs with ~12 event types")
print("  - Normal operations: 35,000 logs")
print("  - Attack scenarios: 11,500 logs")
print("  - Anomalies: 5,000 logs")
