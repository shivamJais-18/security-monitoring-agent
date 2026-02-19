import json

# ==============================
# Load Threat Intelligence
# ==============================
def load_ip_reputation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# ==============================
# Load Detected Threats
# ==============================
def load_threats(file_path):
    threats = []
    with open(file_path, "r") as f:
        for line in f:
            threats.append(json.loads(line))
    return threats

# ==============================
# Enrichment Logic
# ==============================
def enrich_threats(threats, ip_reputation):
    enriched = []

    for threat in threats:
        ip = threat["source_ip"]

        intel = ip_reputation.get(ip)
        if intel:
            threat["threat_intel"] = intel
            threat["intel_match"] = True

            # Escalate severity if confirmed malicious
            if intel["reputation"] == "malicious":
                threat["threat_level"] = "CRITICAL"

        else:
            threat["threat_intel"] = None
            threat["intel_match"] = False

        enriched.append(threat)

    return enriched

# ==============================
# Main Pipeline
# ==============================
def run_threat_intelligence(
    threat_file,
    intel_file,
    output_file
):
    threats = load_threats(threat_file)
    ip_reputation = load_ip_reputation(intel_file)

    enriched = enrich_threats(threats, ip_reputation)

    with open(output_file, "w") as f:
        for threat in enriched:
            f.write(json.dumps(threat) + "\n")

    print(f"[Threat Intel] Enriched threats: {len(enriched)}")
