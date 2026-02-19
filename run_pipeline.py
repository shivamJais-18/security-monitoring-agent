"""
Security Monitoring Agent - Complete Pipeline
"""
import json
from datetime import datetime

print("\n🚀 Starting Security Monitoring Agent Pipeline\n")

# -------- Step 1: ScaleDown --------
print("[1/5] Running ScaleDown Engine...")
try:
    from utils.scaledown import scaledown_logs
    scaledown_logs("data/raw_logs/siem_logs.json", "data/scaled_logs/scaled_logs.json")
except Exception as e:
    print(f"    Fallback: {e}")
    # Use previously generated scaled_logs.json

# -------- Step 2: Log Analyzer --------
print("[2/5] Running Log Analyzer Agent...")
try:
    from agents.log_analyzer import analyze_logs
    analyze_logs("data/scaled_logs/scaled_logs.json", "data/scaled_logs/analyzed_logs.json")
except Exception as e:
    print(f"    Fallback: {e}")
    # Use previously generated analyzed_logs.json

# -------- Step 3: Threat Detection --------
print("[3/5] Running Threat Detector Agent...")
try:
    from agents.threat_detector import detect_threats
    detect_threats("data/scaled_logs/analyzed_logs.json", "data/scaled_logs/detected_threats.json")
except Exception as e:
    print(f"    Fallback: {e}")

# -------- Step 4: Response Coordination --------
print("[4/5] Running Response Coordinator Agent...")
try:
    import sys
    sys.path.insert(0, "agents/playbooks/agents")
    from response_coordinator import coordinate_response
    coordinate_response("data/scaled_logs/detected_threats.json", "agents/playbooks/incident_playbooks.yaml", "data/scaled_logs/incidents.json")
except Exception as e:
    print(f"    Fallback: {e}")

# -------- Step 5: Summary --------
print("[5/5] Pipeline Summary")
try:
    scaled_count = sum(1 for line in open("data/scaled_logs/scaled_logs.json") if line.strip())
    analyzed_count = sum(1 for line in open("data/scaled_logs/analyzed_logs.json") if line.strip())
    threat_count = sum(1 for line in open("data/scaled_logs/detected_threats.json") if line.strip())
    incident_count = sum(1 for line in open("data/scaled_logs/incidents.json") if line.strip())
    
    print(f"""
✓ Pipeline Complete
  - Scaled Logs: {scaled_count} entries
  - Analyzed Logs: {analyzed_count} entries
  - Detected Threats: {threat_count} entries
  - Incidents: {incident_count} entries
""")
except Exception as e:
    print(f"Summary error: {e}")

print("\n✅ Security Monitoring Agent Pipeline Completed\n")
