from utils.scaledown import scaledown_logs

scaledown_logs(
    "data/raw_logs/siem_logs.json",
    "data/scaled_logs/scaled_logs.json",
)
print("scaledown_logs finished")
