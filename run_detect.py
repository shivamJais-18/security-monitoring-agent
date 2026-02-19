try:
    from agents.threat_detector import detect_threats
    detect_threats(
        "data/scaled_logs/analyzed_logs.json",
        "data/scaled_logs/detected_threats.json"
    )
except Exception as e:
    print("Fallback: ML unavailable or error occurred:", e)
    import json

    # If analyzed file missing, perform a lightweight analysis from scaled logs
    scaled_path = "data/scaled_logs/scaled_logs.json"
    analyzed_path = "data/scaled_logs/analyzed_logs.json"
    outpath = "data/scaled_logs/detected_threats.json"

    # Basic analyzer (replicates agents.log_analyzer behavior)
    def calculate_risk_score(feature):
        score = 0
        if feature.get("is_bruteforce"):
            score += 30
        if feature.get("is_port_scan"):
            score += 25
        if feature.get("is_malware"):
            score += 40
        score += feature.get("max_severity", 0) * 2
        score += min(feature.get("event_count", 0), 20)
        return score

    # Ensure analyzed logs exist
    try:
        with open(analyzed_path, "r") as f:
            analyzed_logs = [json.loads(l) for l in f]
    except FileNotFoundError:
        analyzed_logs = []
        with open(scaled_path, "r") as f:
            for line in f:
                log = json.loads(line)
                feature = {
                    "source_ip": log["source_ip"],
                    "event_type": log["event_type"],
                    "event_count": log["event_count"],
                    "max_severity": log["max_severity"],
                    "is_bruteforce": log["event_type"] == "AUTH_FAIL" and log["event_count"] > 5,
                    "is_port_scan": log["event_type"] == "PORT_SCAN" and log["event_count"] > 10,
                    "is_malware": log["event_type"] == "MALWARE_ALERT",
                }
                feature["risk_score"] = calculate_risk_score(feature)
                feature["label"] = "SUSPICIOUS" if feature["risk_score"] >= 40 else "NORMAL"
                analyzed_logs.append(feature)
        with open(analyzed_path, "w") as f:
            for ev in analyzed_logs:
                f.write(json.dumps(ev) + "\n")

    # Simple rule-based threat confirmation (no ML)
    MIN_RISK = 50
    threats = []
    for log in analyzed_logs:
        if log.get("risk_score", 0) >= MIN_RISK:
            t = log.copy()
            t["anomaly_score"] = None
            t["detection_reason"] = "RULE_BASED"
            if t["risk_score"] >= 80:
                t["threat_level"] = "CRITICAL"
            elif t["risk_score"] >= 65:
                t["threat_level"] = "HIGH"
            else:
                t["threat_level"] = "MEDIUM"
            threats.append(t)

    with open(outpath, "w") as f:
        for t in threats:
            f.write(json.dumps(t) + "\n")

    print(f"[Threat Detector - fallback] Confirmed threats: {len(threats)}")
