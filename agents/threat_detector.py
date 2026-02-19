import json
import numpy as np
from sklearn.ensemble import IsolationForest

# ==============================
# Configuration
# ==============================
ANOMALY_THRESHOLD = -0.15   # lower = more anomalous
MIN_RISK_SCORE = 50

# ==============================
# Load Analyzed Logs
# ==============================
def load_analyzed_logs(file_path):
    logs = []
    with open(file_path, "r") as f:
        for line in f:
            logs.append(json.loads(line))
    return logs

# ==============================
# Feature Vector Creation
# ==============================
def build_feature_vectors(logs):
    X = []
    for log in logs:
        X.append([
            log["event_count"],
            log["max_severity"],
            log["risk_score"],
            int(log["is_bruteforce"]),
            int(log["is_port_scan"]),
            int(log["is_malware"])
        ])
    return np.array(X)

# ==============================
# ML Anomaly Detection
# ==============================
def detect_anomalies(X):
    model = IsolationForest(
        n_estimators=150,
        contamination=0.05,
        random_state=42
    )
    model.fit(X)

    scores = model.decision_function(X)
    predictions = model.predict(X)

    return scores, predictions

# ==============================
# Hybrid Threat Decision Logic
# ==============================
def classify_threats(logs, scores, predictions):
    threats = []

    for log, score, pred in zip(logs, scores, predictions):
        is_ml_anomaly = pred == -1 and score < ANOMALY_THRESHOLD
        is_rule_threat = log["risk_score"] >= MIN_RISK_SCORE

        if is_ml_anomaly or is_rule_threat:
            threat = log.copy()

            threat["anomaly_score"] = float(score)
            threat["detection_reason"] = (
                "ML_ANOMALY" if is_ml_anomaly else "RULE_BASED"
            )

            # Severity classification
            if threat["risk_score"] >= 80:
                threat["threat_level"] = "CRITICAL"
            elif threat["risk_score"] >= 65:
                threat["threat_level"] = "HIGH"
            else:
                threat["threat_level"] = "MEDIUM"

            threats.append(threat)

    return threats

# ==============================
# Main Pipeline
# ==============================
def detect_threats(input_file, output_file):
    logs = load_analyzed_logs(input_file)
    X = build_feature_vectors(logs)

    scores, predictions = detect_anomalies(X)
    threats = classify_threats(logs, scores, predictions)

    with open(output_file, "w") as f:
        for threat in threats:
            f.write(json.dumps(threat) + "\n")

    print(f"[Threat Detector] Confirmed threats: {len(threats)}")
