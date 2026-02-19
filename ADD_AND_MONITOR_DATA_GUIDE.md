# Adding Custom Data & Monitoring Guide

A complete walkthrough for adding custom security data to the dashboard and monitoring it in real-time.

---

## 🎯 Overview

This guide shows you how to:
1. **Add Custom Data** - Threats and incidents
2. **Monitor in Real-Time** - Live dashboard updates
3. **Test Scenarios** - Simulate security events
4. **Track Changes** - Watch data flow through the pipeline

---

## ✅ Prerequisites

- Backend API running: `http://localhost:8000`
- Frontend dashboard: `http://localhost:5174/`
- Both servers should be active

### Start Servers (If Not Running)

**Terminal 1 - Backend:**
```powershell
cd d:\Coding\Pj
.\.venv\Scripts\python.exe api_server.py
```

**Terminal 2 - Frontend:**
```powershell
cd d:\Coding\Pj\security-ui
npm run dev
```

---

## 📊 Method 1: Dashboard UI (Easiest)

The **Custom Data Panel** in the dashboard is the easiest way to add data.

### Step 1: Open Dashboard

1. Open browser: `http://localhost:5174/`
2. Click **"🎯 Custom Data"** in left sidebar
3. You'll see 4 tabs: Add Threat, Add Incident, Live Monitor, Settings

### Step 2: Add a Custom Threat

**Navigate to "Add Threat" Tab:**

1. **Source IP**: Enter threat source
   - Example: `203.0.113.42` (external IP)
   - Or: `192.168.1.50` (internal IP)

2. **Event Type**: Select from dropdown
   - Brute Force (AUTH_FAIL)
   - Port Scan (PORT_SCAN)
   - Malware Alert
   - SQL Injection
   - DDoS Attack
   - Privilege Escalation
   - Data Exfiltration
   - Firewall Block

3. **Risk Score**: Use slider (0-100)
   - Automatically sets Threat Level:
     - 0-49: Below threshold
     - 50-64: MEDIUM
     - 65-79: HIGH
     - 80-100: CRITICAL

4. **Event Count**: Number of events (default: 1)

5. **Click "➕ Add Threat"**

**See this message:**
```
✅ Threat added successfully!
```

### Step 3: Add a Security Incident

**Navigate to "Add Incident" Tab:**

1. **Source IP**: Enter the attacking IP
   - Example: `192.168.1.50`

2. **Event Type**: Optional (default: SECURITY_INCIDENT)

3. **Severity**: Choose level
   - MEDIUM
   - HIGH
   - CRITICAL

4. **Description**: Details about incident
   - Example: "SQL injection attempt on customer database"

5. **Click "➕ Create Incident"**

**Automatic Actions Based on Severity:**
- **CRITICAL**: Block IP → Isolate System → Notify SOC → Generate Ticket
- **HIGH**: Block IP → Notify SOC → Generate Ticket
- **MEDIUM**: Notify SOC → Log Event

### Step 4: Monitor in Real-Time

**Go to "Live Monitor" Tab:**

1. **Click "Start Auto-Refresh"**
   - Updates every 5 seconds
   - Shows latest threats and incidents

2. **Watch the feeds:**
   - 📊 Latest Threats (top 5)
   - 🚨 Latest Incidents (top 5)
   - 📈 Current Statistics

3. **Statistics shown:**
   - Total Threats count
   - Total Incidents count
   - Critical Threats count
   - Last Update time

---

## 🎮 Method 2: Command Line Tool

Fast way to add data without opening dashboard.

### Add Preset Threats (Quick Test)

```powershell
cd d:\Coding\Pj

# Add SQL Injection threat
.\.venv\Scripts\python.exe data_injector.py add-preset sql_injection

# Add DDoS Attack threat
.\.venv\Scripts\python.exe data_injector.py add-preset ddos_attack

# Add Malware Alert
.\.venv\Scripts\python.exe data_injector.py add-preset malware

# Add Brute Force attack
.\.venv\Scripts\python.exe data_injector.py add-preset brute_force
```

### Add Custom Threats

**Format:**
```powershell
.\.venv\Scripts\python.exe data_injector.py add-threat <IP> <EVENT_TYPE> <RISK_SCORE> <LEVEL>
```

**Examples:**
```powershell
# Malware on internal IP
.\.venv\Scripts\python.exe data_injector.py add-threat 192.168.1.50 MALWARE_ALERT 85 CRITICAL

# Port scan from external IP
.\.venv\Scripts\python.exe data_injector.py add-threat 203.0.113.25 PORT_SCAN 70 HIGH

# Failed auth attempts
.\.venv\Scripts\python.exe data_injector.py add-threat 192.168.1.100 AUTH_FAIL 55 MEDIUM
```

### Create Incidents

**Format:**
```powershell
.\.venv\Scripts\python.exe data_injector.py add-incident <INCIDENT_ID> <SOURCE_IP> <SEVERITY>
```

**Examples:**
```powershell
# Critical incident
.\.venv\Scripts\python.exe data_injector.py add-incident INC-001 192.168.1.50 CRITICAL

# High severity incident
.\.venv\Scripts\python.exe data_injector.py add-incident INC-002 203.0.113.10 HIGH

# Medium incident
.\.venv\Scripts\python.exe data_injector.py add-incident INC-003 192.168.1.75 MEDIUM
```

### View Current Data

```powershell
.\.venv\Scripts\python.exe data_injector.py list
```

**Output:**
```
📊 Threats (XXX total):
   1. 203.0.113.42 - SQL_INJECTION (CRITICAL)
   2. 203.0.113.88 - DDoS_DETECTED (CRITICAL)
   ...

📋 Incidents (XXX total):
   1. INC-001 - CRITICAL
   2. INC-002 - HIGH
```

---

## 🚀 Testing Scenarios

### Scenario 1: Single SQL Injection Attack

**Goal:** Add a SQL Injection threat and watch it appear in dashboard

**Steps:**

1. **Open dashboard** → Custom Data → Add Threat tab
2. **Fill form:**
   - IP: `203.0.113.42`
   - Event Type: SQL Injection
   - Risk Score: Slider to `95`
   - (Threat Level auto-set to CRITICAL)
3. **Click "Add Threat"** ✅
4. **Switch to "Live Monitor"** tab
5. **Click "Refresh Now"**
6. **See threat appear** in feed with CRITICAL badge (red border)

---

### Scenario 2: DDoS Attack Response

**Goal:** Simulate DDoS and create incident with automatic response

**Steps:**

1. **Terminal:** Add DDoS threat
   ```powershell
   .\.venv\Scripts\python.exe data_injector.py add-preset ddos_attack
   ```

2. **Dashboard:**
   - Go to "Custom Data" → "Live Monitor"
   - Click "Start Auto-Refresh"
   - DDoS threat appears immediately

3. **Add Incident:**
   - Switch to "Add Incident" tab
   - IP: `203.0.113.88` (from the threat)
   - Severity: CRITICAL
   - Description: "DDoS attack detected - 100,000 requests/second"
   - Click "Create Incident"

4. **Monitor Response:**
   - Response actions auto-trigger:
     - Block IP
     - Isolate System
     - Notify SOC
     - Generate Ticket
   - Watch in Live Monitor feed

---

### Scenario 3: Multi-Threat Attack Chain

**Goal:** Simulate realistic attack progression

**Timeline of Attack:**

**T+0min: Reconnaissance**
```powershell
# Add port scan threat
.\.venv\Scripts\python.exe data_injector.py add-threat 203.0.113.99 PORT_SCAN 70 HIGH
```
→ Appears in dashboard

**T+5min: Brute Force**
```powershell
# Add brute force threat
.\.venv\Scripts\python.exe data_injector.py add-threat 203.0.113.99 AUTH_FAIL 75 HIGH
```
→ Same IP, escalating threat level

**T+10min: Successful Breach**
```powershell
# Add SQL Injection threat
.\.venv\Scripts\python.exe data_injector.py add-threat 203.0.113.99 SQL_INJECTION 95 CRITICAL
```
→ Threat level jumps to CRITICAL

**T+12min: Create Incident**

Dashboard → Custom Data → Add Incident:
- IP: `203.0.113.99`
- Severity: CRITICAL
- Description: "Compromised database server - SQL injection from attacker"
- Click Create

→ Incident created with automatic response actions

**Watch in Live Monitor:**
- See all 3 threats from same IP
- See incident with CRITICAL response
- Watch stats update

---

### Scenario 4: Real-Time Side-by-Side Monitoring

**Goal:** Add data while monitoring live

**Setup - Two Browser Windows:**

**Left Window:** Dashboard → Custom Data → **Live Monitor**
- Click "Start Auto-Refresh"
- Watch the threat/incident feed

**Right Window:** Dashboard → Custom Data → **Add Threat**
- Ready to add data

**Actions:**

1. In Right window, add a threat
2. Watch it appear in Left window within 5 seconds
3. Add another threat
4. Watch both update together
5. Add an incident
6. See it in the incidents section

---

## 📊 Understanding the Data Flow

### What Happens When You Add Data:

```
Dashboard Form Input
        ↓
API Request to Backend (/api/add-threat)
        ↓
Flask Server
        ↓
Write to JSON File (detected_threats.json)
        ↓
API Response (Success/Error)
        ↓
Dashboard Refreshes (Auto or Manual)
        ↓
Data Appears in Live Monitor
        ↓
Statistics Update Automatically
```

### File Locations:

All data stored in: `d:\Coding\Pj\data\scaled_logs\`

```
detected_threats.json       ← Your custom threats go here
incidents.json              ← Your custom incidents go here
analyzed_logs.json          ← From log analyzer
scaled_logs.json            ← From scaledown
```

---

## 🔍 Monitoring Dashboard

### Live Monitor Features

**Real-Time Feeds:**
- Shows last 5 threats (newest first)
- Shows last 5 incidents (newest first)
- Auto-refreshes every 5 seconds
- Color-coded by severity

**Color Scheme:**
- 🔴 **Red** = CRITICAL (80+)
- 🟠 **Orange** = HIGH (65-79)
- 🔵 **Blue** = MEDIUM (50-64)

**Statistics Panel:**
- Total Threats Count
- Total Incidents Count
- Critical Threats Count
- Last Update Timestamp

**Controls:**
- ⏹️ **Start Auto-Refresh** - Enable 5-second updates
- 🔃 **Stop Auto-Refresh** - Disable auto-updates
- 🔄 **Refresh Now** - Manual immediate refresh

---

## ✨ Tips & Tricks

### Tip 1: Batch Add Threats Quickly

Use PowerShell to add multiple threats:

```powershell
cd d:\Coding\Pj

# Add 5 different threats
.\.venv\Scripts\python.exe data_injector.py add-preset sql_injection
.\.venv\Scripts\python.exe data_injector.py add-preset ddos_attack
.\.venv\Scripts\python.exe data_injector.py add-preset malware
.\.venv\Scripts\python.exe data_injector.py add-preset brute_force
.\.venv\Scripts\python.exe data_injector.py add-preset port_scan
```

Then watch them all appear in Live Monitor!

### Tip 2: Clear Data Between Tests

```powershell
# Clear all threats
.\.venv\Scripts\python.exe data_injector.py clear-threats

# Clear all incidents
.\.venv\Scripts\python.exe data_injector.py clear-incidents
```

Or use Dashboard → Custom Data → Settings → "🗑️ Clear All Data"

### Tip 3: Test Current Data

```powershell
# See what's currently in dashboard
.\.venv\Scripts\python.exe data_injector.py list
```

### Tip 4: Use Same IP for Related Threats

Add multiple threats from same attacker IP to simulate realistic scenario:

```powershell
# Same attacker, escalating threats
.\.venv\Scripts\python.exe data_injector.py add-threat 203.0.113.50 PORT_SCAN 60 MEDIUM
.\.venv\Scripts\python.exe data_injector.py add-threat 203.0.113.50 AUTH_FAIL 70 HIGH
.\.venv\Scripts\python.exe data_injector.py add-threat 203.0.113.50 SQL_INJECTION 95 CRITICAL
```

---

## 🚨 Troubleshooting

### Data Not Appearing in Live Monitor

**Problem:** Added threat but doesn't show up

**Solution:**
1. Check "Live Monitor" tab is showing (not another tab)
2. Click "Refresh Now" button
3. Wait 5 seconds if "Auto-Refresh" is on
4. Check browser console (F12) for errors
5. Verify backend running: `http://localhost:8000/api/health`

### Auto-Refresh Not Working

**Problem:** Live Monitor doesn't update automatically

**Solution:**
1. Click "Stop Auto-Refresh" then "Start Auto-Refresh" again
2. Check if page is in focus
3. Look for errors in browser console (F12)
4. Close and reopen the Live Monitor tab

### API Connection Errors

**Problem:** "Failed to connect to API" message

**Solution:**
1. Verify Flask backend is running
   ```powershell
   # Should show: WARNING: This is a development server
   ```
2. Check port 8000 is available
3. Restart both servers
4. Check `CORS` is enabled in `api_server.py`

### Form Validation Errors

**Problem:** Can't submit threat form

**Solution:**
- Source IP must be valid format (e.g., `192.168.1.50`)
- Select an Event Type (don't leave blank)
- Risk Score must be 0-100
- All required fields must be filled

---

## 📈 Monitoring Best Practices

### 1. **Start Fresh**
```powershell
# Clear all data before testing
.\.venv\Scripts\python.exe data_injector.py clear-threats
.\.venv\Scripts\python.exe data_injector.py clear-incidents
```

### 2. **Add Data Purposefully**
- Have a scenario in mind
- Plan the attack progression
- Track which IPs are which

### 3. **Monitor Actively**
- Use "Live Monitor" tab
- Keep "Auto-Refresh" on
- Watch statistics update
- Note how fast data appears

### 4. **Create Realistic Scenarios**
- Use believable IP addresses
- Simulate attack progression
- Add incidents for critical threats
- Track response actions

### 5. **Document Your Tests**
- Note what you added
- Record response times
- Document any issues
- Test dashboard stability

---

## 📝 Test Checklist

When testing custom data:

- [ ] Backend running on port 8000
- [ ] Frontend running on port 5174
- [ ] Dashboard accessible
- [ ] Custom Data menu item visible
- [ ] Can add threat successfully
- [ ] Threat appears in Live Monitor within 5 seconds
- [ ] Can add incident successfully
- [ ] Incident appears in Live Monitor
- [ ] Auto-Refresh working (updates every 5 seconds)
- [ ] Statistics updating correctly
- [ ] Color-coding by severity correct
- [ ] Clear data button works
- [ ] No errors in browser console

---

## 🎯 Complete Workflow Example

### 10-Minute Test Session

**Minute 0: Setup**
```
1. Browser: Open dashboard (http://localhost:5174/)
2. Click: Custom Data → Live Monitor
3. Click: "Start Auto-Refresh"
4. Keep this window open
```

**Minute 1: Add First Threat**
```
5. Switch to: Custom Data → Add Threat
6. IP: 203.0.113.42
7. Event Type: SQL Injection
8. Risk Score: 95
9. Click: Add Threat ✅
```

**Minute 2: Monitor**
```
10. Switch back to: Custom Data → Live Monitor
11. See SQL_INJECTION threat appear (CRITICAL, red)
12. Note: Last Update time changed
```

**Minute 4: Add DDoS**
```
13. Switch to: Custom Data → Add Threat
14. IP: 203.0.113.88
15. Event Type: DDoS_DETECTED
16. Risk Score: 100
17. Click: Add Threat ✅
```

**Minute 5: Create Incident**
```
18. Switch to: Custom Data → Add Incident
19. IP: 203.0.113.88
20. Severity: CRITICAL
21. Description: DDoS attack detected
22. Click: Create Incident ✅
```

**Minute 6: Monitor Results**
```
23. Switch to: Custom Data → Live Monitor
24. See both threats
25. See incident with actions
26. Check statistics (2 threats, 1 incident, 2 critical)
```

**Minute 7-10: Advanced Testing**
```
27. Try batch adding threats
28. Test clearing data
29. Test manual refresh
30. Verify all works smoothly
```

---

## 🎓 Learning Outcomes

After completing this guide, you'll understand:

✅ How to add custom security data
✅ How data flows through the system
✅ How to monitor threats in real-time
✅ How incidents are created and tracked
✅ How automatic response works
✅ How to test security scenarios
✅ Dashboard capabilities and features

---

## 🚀 Next Steps

After mastering custom data:

1. **Explore More Features**
   - Check other dashboard views
   - Review analytics
   - Explore playbooks

2. **Load More Data**
   - Generate larger datasets
   - Process real security logs
   - Analyze patterns

3. **Customize Further**
   - Modify risk scoring
   - Add new event types
   - Create custom playbooks

4. **Deploy & Share**
   - Deploy to server
   - Share with team
   - Get feedback

---

## 📱 Need Help?

- **Dashboard not loading?** → Check both servers running
- **Data not appearing?** → Try manual refresh
- **Form errors?** → Check all fields filled
- **Performance issues?** → Too much data stored, try clearing

---

**Happy monitoring! 🎯🔐**

For detailed documentation, see:
- CUSTOM_DATA_PANEL_GUIDE.md
- MANUAL_DATA_GUIDE.md
- README.md
