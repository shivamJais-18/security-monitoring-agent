import json
from datetime import datetime
import sys
sys.path.insert(0, "agents/playbooks/agents")

try:
    import yaml
except ImportError:
    print("[Warning] PyYAML not available, using fallback parser")
    yaml = None

try:
    from response_coordinator import coordinate_response
    coordinate_response(
        "data/scaled_logs/detected_threats.json",
        "agents/playbooks/incident_playbooks.yaml",
        "data/scaled_logs/incidents.json"
    )
except Exception as e:
    print(f"[Fallback] Import failed: {e}")
    
    # Simple YAML parser for incident_playbooks
    def parse_playbooks_yaml(filepath):
        playbooks = {}
        current_level = None
        with open(filepath, "r") as f:
            for line in f:
                line = line.rstrip()
                if not line or line.startswith("#"):
                    continue
                if line.endswith(":") and not line.startswith(" "):
                    current_level = line[:-1]
                    playbooks[current_level] = {"actions": []}
                elif line.strip().startswith("- "):
                    action = line.strip()[2:]
                    if current_level:
                        playbooks[current_level]["actions"].append(action)
        return playbooks
    
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

    threat_file = "data/scaled_logs/detected_threats.json"
    playbook_file = "agents/playbooks/incident_playbooks.yaml"
    output_file = "data/scaled_logs/incidents.json"
    
    # Load threats
    threats = []
    try:
        with open(threat_file, "r") as f:
            for line in f:
                if line.strip():
                    threats.append(json.loads(line))
    except FileNotFoundError:
        threats = []
    
    # Load playbooks
    if yaml:
        with open(playbook_file, "r") as f:
            playbooks = yaml.safe_load(f)
    else:
        playbooks = parse_playbooks_yaml(playbook_file)
    
    # Process incidents
    incidents = []
    for threat in threats:
        severity = threat.get("threat_level", "MEDIUM")
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
    
    # Write output
    with open(output_file, "w") as f:
        for incident in incidents:
            f.write(json.dumps(incident) + "\n")
    
    print(f"[Response Coordinator - Fallback] Incidents handled: {len(incidents)}")
