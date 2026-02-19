"""
Security Monitoring Backend API
Serves threat data and runs the security analysis pipeline
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from pathlib import Path
import subprocess
import sys

app = Flask(__name__)
CORS(app)

# Project paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data" / "scaled_logs"

# ==================== API Routes ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'message': 'Security Monitoring Backend is running'
    }), 200

@app.route('/api/data', methods=['GET'])
def get_data():
    """Get all security monitoring data"""
    try:
        data = {
            'threats': load_json_file(DATA_DIR / "detected_threats.json"),
            'incidents': load_json_file(DATA_DIR / "incidents.json"),
            'analyzed': load_json_file(DATA_DIR / "analyzed_logs.json"),
            'stats': {
                'scaled': count_lines(DATA_DIR / "scaled_logs.json"),
                'analyzed': count_lines(DATA_DIR / "analyzed_logs.json"),
                'detected': count_lines(DATA_DIR / "detected_threats.json"),
                'incidents': count_lines(DATA_DIR / "incidents.json")
            }
        }
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/threats', methods=['GET'])
def get_threats():
    """Get detected threats"""
    try:
        threats = load_json_file(DATA_DIR / "detected_threats.json")
        return jsonify({'threats': threats}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/incidents', methods=['GET'])
def get_incidents():
    """Get security incidents"""
    try:
        incidents = load_json_file(DATA_DIR / "incidents.json")
        return jsonify({'incidents': incidents}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/analyzed-logs', methods=['GET'])
def get_analyzed_logs():
    """Get analyzed logs"""
    try:
        logs = load_json_file(DATA_DIR / "analyzed_logs.json")
        return jsonify({'logs': logs}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/run-pipeline', methods=['POST'])
def run_pipeline():
    """Execute the security monitoring pipeline"""
    try:
        # Run the pipeline script
        venv_python = BASE_DIR / ".venv" / "Scripts" / "python.exe"
        pipeline_script = BASE_DIR / "run_pipeline.py"
        
        if sys.platform == "win32":
            # Windows
            result = subprocess.run(
                [str(venv_python), str(pipeline_script)],
                capture_output=True,
                text=True,
                timeout=60
            )
        else:
            # Linux/Mac
            venv_python = BASE_DIR / ".venv" / "bin" / "python"
            result = subprocess.run(
                [str(venv_python), str(pipeline_script)],
                capture_output=True,
                text=True,
                timeout=60
            )
        
        if result.returncode == 0:
            # Pipeline executed successfully, reload data
            data = {
                'status': 'success',
                'message': 'Pipeline executed successfully',
                'output': result.stdout,
                'data': {
                    'threats': load_json_file(DATA_DIR / "detected_threats.json"),
                    'incidents': load_json_file(DATA_DIR / "incidents.json"),
                    'stats': {
                        'scaled': count_lines(DATA_DIR / "scaled_logs.json"),
                        'analyzed': count_lines(DATA_DIR / "analyzed_logs.json"),
                        'detected': count_lines(DATA_DIR / "detected_threats.json"),
                        'incidents': count_lines(DATA_DIR / "incidents.json")
                    }
                }
            }
            return jsonify(data), 200
        else:
            return jsonify({
                'status': 'error',
                'message': 'Pipeline execution failed',
                'error': result.stderr
            }), 500
            
    except subprocess.TimeoutExpired:
        return jsonify({
            'status': 'error',
            'message': 'Pipeline execution timeout'
        }), 504
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get pipeline statistics"""
    try:
        stats = {
            'scaled': count_lines(DATA_DIR / "scaled_logs.json"),
            'analyzed': count_lines(DATA_DIR / "analyzed_logs.json"),
            'detected': count_lines(DATA_DIR / "detected_threats.json"),
            'incidents': count_lines(DATA_DIR / "incidents.json")
        }
        return jsonify(stats), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== Custom Data Injection (Dashboard) ====================

@app.route('/api/add-threat', methods=['POST'])
def add_threat():
    """Add a custom threat to the dashboard"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['source_ip', 'event_type', 'risk_score', 'threat_level']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields: ' + ', '.join(required_fields)}), 400
        
        # Build threat object
        threat = {
            'source_ip': data.get('source_ip'),
            'event_type': data.get('event_type'),
            'event_count': data.get('event_count', 1),
            'max_severity': 10 if data.get('threat_level') == 'CRITICAL' else 7,
            'is_bruteforce': data.get('event_type') == 'AUTH_FAIL',
            'is_port_scan': data.get('event_type') == 'PORT_SCAN',
            'is_malware': data.get('event_type') == 'MALWARE_ALERT',
            'risk_score': int(data.get('risk_score', 50)),
            'label': 'SUSPICIOUS',
            'anomaly_score': -0.5,
            'detection_reason': data.get('detection_reason', 'MANUAL_INPUT'),
            'threat_level': data.get('threat_level', 'MEDIUM')
        }
        
        # Append to threats file
        threat_file = DATA_DIR / "detected_threats.json"
        with open(threat_file, 'a') as f:
            f.write(json.dumps(threat) + '\n')
        
        return jsonify({
            'status': 'success',
            'message': 'Threat added successfully',
            'threat': threat
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/add-incident', methods=['POST'])
def add_incident():
    """Add a security incident to the dashboard"""
    try:
        from datetime import datetime
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['source_ip', 'severity']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields: ' + ', '.join(required_fields)}), 400
        
        # Determine actions based on severity
        severity_actions = {
            'CRITICAL': ['block_ip', 'isolate_system', 'notify_soc', 'generate_ticket'],
            'HIGH': ['block_ip', 'notify_soc', 'generate_ticket'],
            'MEDIUM': ['notify_soc', 'log_event']
        }
        
        incident_id = f"INC-CUSTOM-{int(datetime.now().timestamp() * 1000)}"
        
        # Build incident object
        incident = {
            'incident_id': data.get('incident_id', incident_id),
            'source_ip': data.get('source_ip'),
            'event_type': data.get('event_type', 'SECURITY_INCIDENT'),
            'severity': data.get('severity', 'MEDIUM'),
            'actions_taken': data.get('actions_taken', severity_actions.get(data.get('severity', 'MEDIUM'), [])),
            'timestamp': datetime.now().isoformat(),
            'description': data.get('description', '')
        }
        
        # Append to incidents file
        incident_file = DATA_DIR / "incidents.json"
        with open(incident_file, 'a') as f:
            f.write(json.dumps(incident) + '\n')
        
        return jsonify({
            'status': 'success',
            'message': 'Incident created successfully',
            'incident': incident
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/delete-threat/<int:index>', methods=['DELETE'])
def delete_threat(index):
    """Delete a threat by index"""
    try:
        threat_file = DATA_DIR / "detected_threats.json"
        threats = load_json_file(threat_file)
        
        if index < 0 or index >= len(threats):
            return jsonify({'error': 'Invalid threat index'}), 400
        
        # Remove threat and rewrite file
        threats.pop(index)
        with open(threat_file, 'w') as f:
            for threat in threats:
                f.write(json.dumps(threat) + '\n')
        
        return jsonify({
            'status': 'success',
            'message': 'Threat deleted successfully'
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/clear-all-data', methods=['POST'])
def clear_all_data():
    """Clear all threats and incidents"""
    try:
        for filename in ['detected_threats.json', 'incidents.json']:
            filepath = DATA_DIR / filename
            filepath.write_text('')
        
        return jsonify({
            'status': 'success',
            'message': 'All data cleared'
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== Helper Functions ====================

def load_json_file(file_path):
    """Load JSONL file and return as list of objects"""
    if not file_path.exists():
        return []
    
    items = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    items.append(json.loads(line))
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
    
    return items

def count_lines(file_path):
    """Count non-empty lines in a file"""
    if not file_path.exists():
        return 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for line in f if line.strip())
    except Exception:
        return 0

# ==================== Error Handlers ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

# ==================== Main ====================

if __name__ == '__main__':
    print("\n🔒 Security Monitoring Backend API")
    print("=" * 50)
    print(f"📁 Data Directory: {DATA_DIR}")
    print(f"🌐 Starting server on http://localhost:8000")
    print("=" * 50)
    print("Available endpoints:")
    print("  GET  /api/health           - Health check")
    print("  GET  /api/data             - All data")
    print("  GET  /api/threats          - Detected threats")
    print("  GET  /api/incidents        - Security incidents")
    print("  GET  /api/analyzed-logs    - Analyzed logs")
    print("  GET  /api/stats            - Statistics")
    print("  POST /api/run-pipeline     - Run pipeline")
    print("  POST /api/add-threat       - Add custom threat")
    print("  POST /api/add-incident     - Add custom incident")
    print("  POST /api/clear-all-data   - Clear all data")
    print("=" * 50 + "\n")
    
    app.run(
        host='localhost',
        port=8000,
        debug=True,
        use_reloader=True
    )
