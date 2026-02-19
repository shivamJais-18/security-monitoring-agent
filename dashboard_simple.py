#!/usr/bin/env python3
"""
Simple HTTP Dashboard for Security Monitoring Agent
"""
import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime

class DashboardHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            # Load data
            threats = []
            incidents = []
            scaled = []
            analyzed = []
            
            try:
                with open("data/scaled_logs/detected_threats.json") as f:
                    threats = [json.loads(line) for line in f if line.strip()]
            except: pass
            
            try:
                with open("data/scaled_logs/incidents.json") as f:
                    incidents = [json.loads(line) for line in f if line.strip()]
            except: pass
            
            try:
                with open("data/scaled_logs/scaled_logs.json") as f:
                    scaled = [json.loads(line) for line in f if line.strip()]
            except: pass
            
            try:
                with open("data/scaled_logs/analyzed_logs.json") as f:
                    analyzed = [json.loads(line) for line in f if line.strip()]
            except: pass
            
            critical = len([t for t in threats if t.get("threat_level") == "CRITICAL"])
            high = len([t for t in threats if t.get("threat_level") == "HIGH"])
            medium = len([t for t in threats if t.get("threat_level") == "MEDIUM"])
            
            html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Security Monitoring Dashboard</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }}
        .header {{ background: #1a1a2e; color: white; padding: 20px; border-radius: 5px; }}
        .metrics {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin: 20px 0; }}
        .metric {{ background: white; padding: 20px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .metric h3 {{ margin: 0; color: #666; }}
        .metric .value {{ font-size: 32px; font-weight: bold; color: #1a1a2e; }}
        .critical {{ color: #d32f2f; }}
        .high {{ color: #f57c00; }}
        .medium {{ color: #fbc02d; }}
        .table {{ background: white; padding: 20px; border-radius: 5px; margin: 20px 0; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th {{ background: #1a1a2e; color: white; padding: 10px; text-align: left; }}
        td {{ padding: 10px; border-bottom: 1px solid #ddd; }}
        tr:hover {{ background: #f5f5f5; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🛡️ Security Monitoring Dashboard</h1>
        <p>Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    
    <div class="metrics">
        <div class="metric">
            <h3>Total Scaled Logs</h3>
            <div class="value">{len(scaled)}</div>
        </div>
        <div class="metric">
            <h3>Analyzed Events</h3>
            <div class="value">{len(analyzed)}</div>
        </div>
        <div class="metric">
            <h3>Detected Threats</h3>
            <div class="value">{len(threats)}</div>
        </div>
        <div class="metric">
            <h3>Incidents</h3>
            <div class="value">{len(incidents)}</div>
        </div>
    </div>
    
    <div class="metrics">
        <div class="metric">
            <h3>Critical Threats</h3>
            <div class="value critical">{critical}</div>
        </div>
        <div class="metric">
            <h3>High Threats</h3>
            <div class="value high">{high}</div>
        </div>
        <div class="metric">
            <h3>Medium Threats</h3>
            <div class="value medium">{medium}</div>
        </div>
        <div class="metric">
            <h3>Automated Responses</h3>
            <div class="value">{len(incidents)}</div>
        </div>
    </div>
    
    <div class="table">
        <h2>🚨 Recent Threats</h2>
        <table>
            <tr>
                <th>Source IP</th>
                <th>Event Type</th>
                <th>Risk Score</th>
                <th>Threat Level</th>
                <th>Detection Reason</th>
            </tr>
            {"".join(f'''<tr>
                <td>{t.get("source_ip", "N/A")}</td>
                <td>{t.get("event_type", "N/A")}</td>
                <td>{t.get("risk_score", "N/A")}</td>
                <td>{t.get("threat_level", "N/A")}</td>
                <td>{t.get("detection_reason", "N/A")}</td>
            </tr>''' for t in threats[:10])}
        </table>
    </div>
    
    <div class="table">
        <h2>📋 Incidents</h2>
        <table>
            <tr>
                <th>Incident ID</th>
                <th>Source IP</th>
                <th>Severity</th>
                <th>Actions Taken</th>
                <th>Timestamp</th>
            </tr>
            {"".join(f'''<tr>
                <td>{i.get("incident_id", "N/A")}</td>
                <td>{i.get("source_ip", "N/A")}</td>
                <td>{i.get("severity", "N/A")}</td>
                <td>{", ".join(i.get("actions_taken", []))}</td>
                <td>{i.get("timestamp", "N/A")}</td>
            </tr>''' for i in incidents[:10])}
        </table>
    </div>
</body>
</html>
"""
            self.wfile.write(html.encode())
        else:
            super().do_GET()

if __name__ == "__main__":
    PORT = 8000
    handler = DashboardHandler
    httpd = HTTPServer(("", PORT), handler)
    print(f"\n🚀 Dashboard running at http://localhost:{PORT}")
    print("Press Ctrl+C to stop\n")
    httpd.serve_forever()
