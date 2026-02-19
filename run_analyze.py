from agents.log_analyzer import analyze_logs

analyze_logs(
    "data/scaled_logs/scaled_logs.json",
    "data/scaled_logs/analyzed_logs.json"
)
print("analyze_logs finished")
