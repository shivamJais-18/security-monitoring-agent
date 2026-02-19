import json
from collections import defaultdict

def scaledown_logs(input_file, output_file):
    summary = defaultdict(lambda: {
        "count": 0,
        "max_severity": 0
    })

    with open(input_file) as f:
        for line in f:
            log = json.loads(line)
            key = (log["source_ip"], log["event_type"])

            summary[key]["count"] += 1
            summary[key]["max_severity"] = max(
                summary[key]["max_severity"],
                log["severity"]
            )

    with open(output_file, "w") as f:
        for (ip, event), data in summary.items():
            f.write(json.dumps({
                "source_ip": ip,
                "event_type": event,
                "event_count": data["count"],
                "max_severity": data["max_severity"]
            }) + "\n")

import json
from collections import defaultdict

def scaledown_logs(input_file, output_file):
    summary = defaultdict(lambda: {
        "count": 0,
        "max_severity": 0
    })

    with open(input_file) as f:
        for line in f:
            log = json.loads(line)
            key = (log["source_ip"], log["event_type"])

            summary[key]["count"] += 1
            summary[key]["max_severity"] = max(
                summary[key]["max_severity"],
                log["severity"]
            )

    with open(output_file, "w") as f:
        for (ip, event), data in summary.items():
            f.write(json.dumps({
                "source_ip": ip,
                "event_type": event,
                "event_count": data["count"],
                "max_severity": data["max_severity"]
            }) + "\n")
