# Quick Reference: Add & Monitor Data

A fast cheat sheet for adding custom data and monitoring in real-time.

---

## 🚀 One-Minute Setup

### Start Servers

**Terminal 1:**
```powershell
cd d:\Coding\Pj
.\.venv\Scripts\python.exe api_server.py
```

**Terminal 2:**
```powershell
cd d:\Coding\Pj\security-ui
npm run dev
```

### Open Dashboard
- Frontend: `http://localhost:5174/`
- Backend API: `http://localhost:8000/api/health`

---

## 📊 Method 1: Dashboard (Easiest)

1. Click **"🎯 Custom Data"** in sidebar
2. Go to **"Add Threat"** tab
3. Fill form:
   - IP: `203.0.113.42`
   - Event Type: `SQL Injection`
   - Risk Score: `95`
4. Click **"➕ Add Threat"**
5. Switch to **"Live Monitor"** tab
6. Click **"Start Auto-Refresh"**
7. Watch threat appear!

---

## 💻 Method 2: Command Line (Fast)

### Quick Presets
```powershell
cd d:\Coding\Pj

# Add SQL Injection threat
.\.venv\Scripts\python.exe data_injector.py add-preset sql_injection

# Add DDoS Attack
.\.venv\Scripts\python.exe data_injector.py add-preset ddos_attack

# Add Malware
.\.venv\Scripts\python.exe data_injector.py add-preset malware
```

### Custom Threats
```powershell
.\.venv\Scripts\python.exe data_injector.py add-threat <IP> <TYPE> <RISK> <LEVEL>

# Example:
.\.venv\Scripts\python.exe data_injector.py add-threat 192.168.1.50 MALWARE_ALERT 85 CRITICAL
```

### Create Incidents
```powershell
.\.venv\Scripts\python.exe data_injector.py add-incident <ID> <IP> <SEVERITY>

# Example:
.\.venv\Scripts\python.exe data_injector.py add-incident INC-001 192.168.1.50 CRITICAL
```

### View Data
```powershell
.\.venv\Scripts\python.exe data_injector.py list
```

### Clear Data
```powershell
.\.venv\Scripts\python.exe data_injector.py clear-threats
.\.venv\Scripts\python.exe data_injector.py clear-incidents
```

---

## 🎯 Quick Test Scenarios

### Test 1: Single Threat
```
1. Add SQL Injection threat (95 risk)
2. Watch appear in Live Monitor
3. See it marked as CRITICAL
Time: 2 minutes
```

### Test 2: Attack Chain
```
1. Add Port Scan (70 risk)
2. Add Brute Force (75 risk) - same IP
3. Add SQL Injection (95 risk) - same IP
4. Create Incident
Time: 5 minutes
```

### Test 3: Real-Time Monitoring
```
1. Open Live Monitor
2. Start Auto-Refresh
3. Add threats in separate Add Threat tab
4. Watch them appear instantly
Time: 5 minutes
```

---

## 📋 Event Types

| Type | Risk | Use |
|------|------|-----|
| AUTH_FAIL | 60-75 | Brute force attempts |
| PORT_SCAN | 65-75 | Reconnaissance |
| MALWARE_ALERT | 80-90 | Malware detected |
| SQL_INJECTION | 85-100 | Database attacks |
| DDoS_DETECTED | 90-100 | Denial of service |
| PRIVILEGE_ESCALATION | 80-90 | Privilege abuse |
| DATA_EXFILTRATION | 90-100 | Data theft |
| FIREWALL_BLOCK | 40-60 | Blocked traffic |

---

## ⏱️ Response Times

- **Add threat**: < 500ms
- **Appear in Live Monitor**: < 5 seconds (with auto-refresh)
- **Incident creation**: < 500ms
- **Dashboard refresh**: < 100ms

---

## 🔴 Threat Levels

Based on Risk Score:

| Level | Score | Color | Actions |
|-------|-------|-------|---------|
| CRITICAL | 80-100 | 🔴 Red | Block IP, Isolate, Notify SOC, Ticket |
| HIGH | 65-79 | 🟠 Orange | Block IP, Notify SOC, Ticket |
| MEDIUM | 50-64 | 🔵 Blue | Notify SOC, Log |

---

## 💡 Pro Tips

- **Batch add**: Add multiple threats simultaneously
- **Same IP**: Add different threats from same IP for realism
- **Auto-refresh**: Leave on for live monitoring (5-second intervals)
- **Clear data**: Start fresh each test session
- **Side-by-side**: Open 2 dashboard tabs to add and monitor together

---

## 🐛 Quick Fixes

| Problem | Solution |
|---------|----------|
| Data not appearing | Click "Refresh Now" |
| Auto-refresh stopped | Stop and start again |
| Form won't submit | Fill all required fields |
| Backend not responding | Check port 8000 |
| Frontend not loading | Check port 5174 |

---

## 📁 File Locations

```
d:\Coding\Pj\data\scaled_logs\
├── detected_threats.json       ← Your threats
├── incidents.json              ← Your incidents
├── analyzed_logs.json          ← Pipeline output
└── scaled_logs.json            ← Pipeline output
```

---

## 🎯 Common Commands

```powershell
cd d:\Coding\Pj

# Add multiple threats
.\.venv\Scripts\python.exe data_injector.py add-preset sql_injection
.\.venv\Scripts\python.exe data_injector.py add-preset ddos_attack
.\.venv\Scripts\python.exe data_injector.py add-preset malware

# Add threat with custom data
.\.venv\Scripts\python.exe data_injector.py add-threat 203.0.113.42 SQL_INJECTION 95 CRITICAL
.\.venv\Scripts\python.exe data_injector.py add-threat 192.168.1.50 MALWARE_ALERT 85 CRITICAL

# Create high severity incident
.\.venv\Scripts\python.exe data_injector.py add-incident INC-TEST-001 203.0.113.42 CRITICAL

# See what's currently in system
.\.venv\Scripts\python.exe data_injector.py list

# Start fresh
.\.venv\Scripts\python.exe data_injector.py clear-threats
```

---

## ✨ 5-Minute Test

```
Min 0: Open Live Monitor + Auto-Refresh
Min 1: Add SQL Injection threat
Min 2: See it appear in monitor  
Min 3: Add DDoS threat + Create incident
Min 5: See both in monitor with stats
```

---

## 📚 Full Documentation

- **ADD_AND_MONITOR_DATA_GUIDE.md** - Complete walkthrough
- **CUSTOM_DATA_PANEL_GUIDE.md** - Dashboard features
- **MANUAL_DATA_GUIDE.md** - CLI tool details
- **README.md** - Project overview

---

**Ready to go? Start with Method 1 (Dashboard) - go to http://localhost:5174/ and click "🎯 Custom Data"!** 🚀
