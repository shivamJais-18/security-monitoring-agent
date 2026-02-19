import json
import yaml
from datetime import datetime

# ==============================
# Load Playbooks
# ==============================
def load_playbooks(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

# ==============================
# Load Threats
# ==============================
def load_threats(file_path):
    threats = []
    with open(file_path, "r") as f:
        for line in f:
            threats.append(json.loads(line))
    return threats

# ==============================
# Simulated Response Actions
# ==============================
def execute_action(action, threat):
    if action == "block_ip":
        print(f"[ACTION] Blocking IP {threat['source_ip']}")

    elif action == "isolate_system":
        print(f"[ACTION] Isolating affected system")

    elif action == "notify_soc":
        print(f"[ACTION] Notifying SOC team")

    elif action == "generate_ticket":
        print(f"[ACTION] Creating incident ticket")

    elif action == "log_event":
        print(f"[ACTION] Logging event for review")

# ==============================
# Incident Processing
# ==============================
def process_incidents(threats, playbooks):
    incidents = []

    for threat in threats:
        severity = threat["threat_level"]
        actions = playbooks.get(severity, {}).get("actions", [])

        for action in actions:
            execute_action(action, threat)

        incident = {
            "incident_id": f"INC-{datetime.utcnow().timestamp()}",
            "source_ip": threat["source_ip"],
            "event_type": threat["event_type"],
            "severity": severity,
            "actions_taken": actions,
            "timestamp": datetime.utcnow().isoformat()
        }

        incidents.append(incident)

    return incidents

# ==============================
# Main Pipeline
# ==============================
def coordinate_response(threat_file, playbook_file, output_file):
    threats = load_threats(threat_file)
    playbooks = load_playbooks(playbook_file)

    incidents = process_incidents(threats, playbooks)

    with open(output_file, "w") as f:
        for incident in incidents:
            f.write(json.dumps(incident) + "\n")

    print(f"[Response Coordinator] Incidents handled: {len(incidents)}")
