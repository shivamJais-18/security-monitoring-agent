# 🔐 Security Monitoring Platform

A comprehensive security monitoring and threat detection system with real-time dashboard, automated threat analysis, and incident response orchestration.

---

## 👋 **NEW USER?** 

### ⭐ **Start here: [START_HERE.md](START_HERE.md)** ⭐
**3-step guide to get up and running in 5-15 minutes**

## 📊 Overview

This platform provides:
- **Real-time threat detection** using ML-based anomaly detection
- **Automated log analysis** with risk scoring
- **Security incident management** with playbook-based responses
- **Live dashboard** for security monitoring
- **Custom data injection** for testing and validation

## 🏗️ Architecture

```
Raw Security Logs (50,000+)
        ↓
   ScaleDown Engine (Aggregation)
        ↓
   Log Analyzer Agent (Feature Extraction & Risk Scoring)
        ↓
   Threat Detector Agent (ML Anomaly + Rule-Based Detection)
        ↓
   Response Coordinator (Incident Classification & Actions)
        ↓
   Flask API Backend
        ↓
   Vue.js Dashboard (Real-time Visualization)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/security-monitoring-platform.git
cd security-monitoring-platform
```

2. **Set up Python virtual environment**
```bash
python -m venv .venv

# On Windows:
.\.venv\Scripts\Activate.ps1

# On macOS/Linux:
source .venv/bin/activate
```

3. **Install Python dependencies**
```bash
pip install flask flask-cors scikit-learn numpy pyyaml
```

4. **Install Node.js dependencies**
```bash
cd security-ui
npm install
cd ..
```

5. **Generate initial dataset**
```bash
python data/raw_logs/generate_logs.py
```

6. **Run the security pipeline**
```bash
python run_pipeline.py
```

7. **Start the backend server**
```bash
python api_server.py
```

8. **Start the frontend development server**
```bash
cd security-ui
npm run dev
```

9. **Access the dashboard**
   - Frontend: `http://localhost:5174/`
   - Backend API: `http://localhost:8000/api/health`

## 📁 Project Structure

```
security-monitoring-platform/
├── api_server.py                 # Flask backend API
├── run_pipeline.py              # Main security pipeline orchestrator
├── data_injector.py             # CLI tool for manual data injection
│
├── agents/                      # Security analysis agents
│   ├── log_analyzer.py          # Log analysis & risk scoring
│   ├── threat_detector.py       # ML-based threat detection
│   └── playbooks/               # Incident response playbooks
│
├── data/
│   ├── raw_logs/               # SIEM logs
│   │   ├── generate_logs.py     # Dataset generator
│   │   └── siem_logs.json       # Raw security logs
│   └── scaled_logs/            # Processed data
│       ├── scaled_logs.json
│       ├── analyzed_logs.json
│       ├── detected_threats.json
│       └── incidents.json
│
├── security-ui/                # Vue.js frontend dashboard
│   ├── src/
│   │   ├── App.vue            # Main app component
│   │   ├── components/         # Dashboard components
│   │   └── views/              # Different dashboard views
│   └── package.json
│
└── utils/
    └── scaledown.py           # Log aggregation utilities
```

## 🎯 Key Features

### 1. **Threat Detection System**
- ML-based anomaly detection (Isolation Forest)
- Rule-based threat classification
- 12 event types (AUTH_FAIL, MALWARE_ALERT, SQL_INJECTION, DDoS_DETECTED, etc.)
- Risk scoring (0-100) with threat level classification

### 2. **Log Analysis Pipeline**
- Behavioral feature extraction
- Risk score calculation
- Pattern recognition for:
  - Brute force attacks
  - Port scans
  - Malware detection
  - Privilege escalation
  - Data exfiltration

### 3. **Automated Response**
- Playbook-based incident response
- Automatic action assignment based on severity:
  - **CRITICAL**: Block IP → Isolate System → Notify SOC → Generate Ticket
  - **HIGH**: Block IP → Notify SOC → Generate Ticket
  - **MEDIUM**: Notify SOC → Log Event

### 4. **Real-Time Dashboard**
- Live threat monitoring
- Incident tracking
- System health metrics
- Threat intelligence feeds
- Custom data injection interface

### 5. **Custom Data Management**
- Add custom threats via dashboard UI
- Create security incidents
- Real-time data monitoring
- Live auto-refresh (5-second intervals)
- Data persistence to JSON files

## 📊 Data Flow

### Raw Data Generation
- Generates 50,000+ realistic security logs
- Multiple datasets for different scenarios:
  - Normal business operations (70%)
  - Attack scenarios (20%)
  - System anomalies (10%)

### Processing Pipeline
1. **ScaleDown**: Aggregates logs by IP + event type
2. **Analysis**: Extracts features and calculates risk scores
3. **Detection**: Identifies threats using ML + rules
4. **Response**: Coordinates automated incident response

### Dashboard Integration
- Displays threats with severity levels
- Shows incidents with response actions
- Tracks system statistics
- Monitors network health

## 🎮 Using the Dashboard

### Main Views
- **Dashboard**: Overview with KPI cards
- **Threat Feed**: Real-time threat updates
- **Systems**: Network infrastructure status
- **Log Analyzer**: Detailed log analysis
- **Custom Data**: Add threats and monitor live
- **Playbooks**: Incident response automation
- **Analytics**: Trend analysis and reporting

### Custom Data Panel
1. Click **"🎯 Custom Data"** in sidebar
2. **Add Threat Tab**: Inject custom security events
3. **Add Incident Tab**: Create incidents
4. **Live Monitor Tab**: Watch data in real-time
5. **Settings Tab**: Manage data

## 🔧 Command Line Tools

### Data Injection
```bash
# View available presets
python data_injector.py presets

# Add preset threat
python data_injector.py add-preset sql_injection

# Add custom threat
python data_injector.py add-threat 192.168.1.50 MALWARE_ALERT 85 CRITICAL

# Create incident
python data_injector.py add-incident INC-001 192.168.1.50 CRITICAL

# View current data
python data_injector.py list

# Clear all data
python data_injector.py clear-threats
```

### Dataset Management
```bash
# List all datasets
python data/raw_logs/dataset_manager.py list

# Analyze dataset
python data/raw_logs/dataset_manager.py analyze siem_logs.json

# Compare datasets
python data/raw_logs/dataset_manager.py compare file1.json file2.json

# Estimate threat detection
python data/raw_logs/dataset_manager.py estimate siem_logs.json
```

## 📡 API Endpoints

### Data Retrieval
```bash
GET /api/health              # Health check
GET /api/data                # All security data
GET /api/threats             # Detected threats
GET /api/incidents           # Security incidents
GET /api/analyzed-logs       # Analyzed logs
GET /api/stats               # Statistics
```

### Data Injection
```bash
POST /api/add-threat         # Add custom threat
POST /api/add-incident       # Add custom incident
POST /api/clear-all-data     # Clear all data
POST /api/run-pipeline       # Run security pipeline
```

### Request Examples
```bash
# Add threat
curl -X POST http://localhost:8000/api/add-threat \
  -H "Content-Type: application/json" \
  -d '{
    "source_ip": "192.168.1.50",
    "event_type": "MALWARE_ALERT",
    "risk_score": 85,
    "threat_level": "CRITICAL"
  }'

# Add incident
curl -X POST http://localhost:8000/api/add-incident \
  -H "Content-Type: application/json" \
  -d '{
    "source_ip": "192.168.1.50",
    "severity": "CRITICAL",
    "description": "Malware detected on endpoint"
  }'
```

## 📈 Performance Metrics

- **Log Processing**: ~50,000 logs in <5 seconds
- **Threat Detection**: 716 threats detected (from 4,186 aggregated events)
- **Dashboard Update**: <100ms refresh
- **API Response**: <500ms (add threat/incident)
- **ML Model**: Isolation Forest with 150 estimators

## 🔒 Security Features

- CORS enabled for dashboard communication
- Risk-based threat classification
- Automated incident response
- Audit logging
- Data persistence to disk

## 📚 Documentation

### 🗺️ Navigation
- [DOCUMENTATION_MAP.md](DOCUMENTATION_MAP.md) - Choose the right guide for you
- [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md) - Complete list of all guides

### Getting Started
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - ⚡ **Start here!** Fast cheat sheet (5 min read)
- [ADD_AND_MONITOR_DATA_GUIDE.md](ADD_AND_MONITOR_DATA_GUIDE.md) - Complete workflow guide with test scenarios

### Detailed Guides
- [MANUAL_DATA_GUIDE.md](MANUAL_DATA_GUIDE.md) - CLI tool reference
- [CUSTOM_DATA_PANEL_GUIDE.md](CUSTOM_DATA_PANEL_GUIDE.md) - Dashboard features explained
- [data/raw_logs/DATASET_README.md](data/raw_logs/DATASET_README.md) - Dataset generation options
- [LINKEDIN_GUIDE.md](LINKEDIN_GUIDE.md) - Share your project on social media
- [GITHUB_UPLOAD_GUIDE.md](GITHUB_UPLOAD_GUIDE.md) - Deploy to GitHub

## 🧪 Testing

### Test Scenario 1: SQL Injection Attack
```bash
python data_injector.py add-preset sql_injection
```

### Test Scenario 2: DDoS Attack
```bash
python data_injector.py add-preset ddos_attack
```

### Test Scenario 3: Multi-Threat Attack Chain
```bash
python data_injector.py add-preset port_scan
python data_injector.py add-preset brute_force
python data_injector.py add-preset privilege_escalation
python data_injector.py add-preset data_exfiltration
```

### Test Scenario 4: Live Monitoring
1. Open dashboard and go to "Custom Data" → "Live Monitor"
2. Click "Start Auto-Refresh"
3. In another window, run threat injection commands
4. Watch threats appear in real-time

## 🚨 Troubleshooting

### Issue: Backend server won't start
```bash
# Check if port 8000 is in use
netstat -ano | findstr :8000

# Kill process on port 8000 and restart
```

### Issue: Dashboard not showing data
```bash
# Verify API is running
curl http://localhost:8000/api/health

# Check browser console for errors (F12)
# Verify CORS is enabled in api_server.py
```

### Issue: Threat data not appearing
```bash
# Verify data files exist
ls data/scaled_logs/

# Check JSON file format
cat data/scaled_logs/detected_threats.json

# Manually refresh: http://localhost:5174/ + Ctrl+F5
```

## 📦 Dependencies

### Python
- Flask 2.0+ - Web framework
- Flask-CORS - Cross-origin resource sharing
- scikit-learn - ML library (Isolation Forest)
- numpy - Numerical computing
- pyYAML - Configuration files

### Node.js
- Vue 3 - Frontend framework
- Vite - Build tool
- Vite Vue plugin - Vue integration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

Security Monitoring Platform - 2026

## 🎯 Roadmap

- [ ] Real-time WebSocket updates
- [ ] Machine learning model training interface
- [ ] Advanced filtering and search
- [ ] Export reports (PDF/CSV)
- [ ] User authentication and roles
- [ ] Historical data analysis
- [ ] Threat intelligence integration
- [ ] Mobile dashboard

## 📞 Support

For issues and feature requests, please open an issue on GitHub.

---

**Happy threat detecting! 🔐**
