"""
Security Monitoring Agent
End-to-End Orchestration File
"""

# Ensure project root is on sys.path so absolute imports resolve
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[6]))

# ==============================
# STEP 1: ScaleDown (Log Compression)
# ==============================
from utils.scaledown import scaledown_logs

# ==============================
# STEP 2: Log Analyzer Agent
# ==============================
# Try standard import first, fall back to file-based loader if needed
try:
    from agents.log_analyzer import analyze_logs
except Exception:
    import importlib.util
    from pathlib import Path
    la_path = Path(__file__).resolve().parents[6] / "agents" / "log_analyzer.py"
    spec = importlib.util.spec_from_file_location("agents.log_analyzer", str(la_path))
    la = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(la)
    analyze_logs = getattr(la, "analyze_logs")

# ==============================
# STEP 3: Threat Detector Agent
# ==============================
from agents.threat_detector import detect_threats

# ==============================
# STEP 5: Threat Intelligence Agent
# ==============================
from intelligence.threat_feeds import run_threat_intelligence

# ==============================
# STEP 4: Response Coordinator Agent
# ==============================
from agents.response_coordinator import coordinate_response


def main():
    print("\n🚀 Starting Security Monitoring Agent Pipeline\n")

    # -------- Step 1: ScaleDown --------
    print("[1/6] Running ScaleDown Engine...")
    scaledown_logs(
        "data/raw_logs/siem_logs.json",
        "data/scaled_logs/scaled_logs.json"
    )

    # -------- Step 2: Log Analyzer --------
    print("[2/6] Running Log Analyzer Agent...")
    analyze_logs(
        "data/scaled_logs/scaled_logs.json",
        "data/scaled_logs/analyzed_logs.json"
    )

    # -------- Step 3: Threat Detection --------
    print("[3/6] Running Threat Detector Agent...")
    detect_threats(
        "data/scaled_logs/analyzed_logs.json",
        "data/scaled_logs/detected_threats.json"
    )

    # -------- Step 5: Threat Intelligence --------
    print("[4/6] Enriching with Threat Intelligence...")
    run_threat_intelligence(
        "data/scaled_logs/detected_threats.json",
        "data/intelligence/ip_reputation.json",
        "data/scaled_logs/enriched_threats.json"
    )

    # -------- Step 4: Automated Response --------
    print("[5/6] Coordinating Incident Response...")
    coordinate_response(
        "data/scaled_logs/enriched_threats.json",
        "playbooks/incident_playbooks.yaml",
        "data/scaled_logs/incidents.json"
    )

    print("\n✅ Security Monitoring Pipeline Completed Successfully")
    print("📊 You can now run the dashboard using:")
    print("👉 streamlit run dashboard/app.py\n")


if __name__ == "__main__":
    main()
