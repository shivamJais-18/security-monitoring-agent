# Custom Data Dashboard Guide

## Overview

The **Custom Data Monitor** is a built-in dashboard feature that allows you to:
- ✅ Add custom threats directly from the UI
- ✅ Create security incidents
- ✅ Monitor data in real-time
- ✅ Track all changes live
- ✅ Manage data with ease

---

## Accessing Custom Data Panel

1. **Open the Dashboard**: Navigate to `http://localhost:5174/`
2. **Click "Custom Data"** in the left sidebar (🎯 icon)
3. You'll see the Custom Data Monitor with multiple tabs

---

## Features

### 1️⃣ **Add Threat Tab**

Add custom security threats to test your monitoring system.

**Fields:**
- **Source IP** - IP address of threat source (e.g., `192.168.1.50` or `203.0.113.42`)
- **Event Type** - Type of security event:
  - Brute Force (AUTH_FAIL)
  - Port Scan (PORT_SCAN)
  - Malware Alert
  - SQL Injection
  - DDoS Attack
  - Privilege Escalation
  - Data Exfiltration
  - Firewall Block
- **Risk Score** - Slider from 0-100
- **Threat Level** - Auto-calculated based on risk score:
  - MEDIUM (50-64)
  - HIGH (65-79)
  - CRITICAL (80+)
- **Event Count** - Number of events (default: 1)

**Example Workflow:**
1. Enter Source IP: `203.0.113.42`
2. Select Event Type: `SQL Injection`
3. Set Risk Score to `95`
4. Click "➕ Add Threat"
5. See success message: ✅ Threat added successfully!

### 2️⃣ **Add Incident Tab**

Create security incidents that trigger response actions.

**Fields:**
- **Source IP** - Attacking system IP
- **Event Type** - Type of incident
- **Severity** - MEDIUM, HIGH, or CRITICAL
- **Description** - Details about the incident

**Automatic Actions:**
The system automatically adds appropriate response actions based on severity:
- **CRITICAL**: Block IP → Isolate System → Notify SOC → Generate Ticket
- **HIGH**: Block IP → Notify SOC → Generate Ticket
- **MEDIUM**: Notify SOC → Log Event

**Example Workflow:**
1. Enter Source IP: `192.168.1.50`
2. Set Severity: `CRITICAL`
3. Add Description: "SQL injection attempt on customer database"
4. Click "➕ Create Incident"
5. Incident is automatically created with response actions

### 3️⃣ **Live Monitor Tab**

Real-time monitoring of all threats and incidents in your system.

**Features:**
- 🔄 **Auto-Refresh**: Click "Start Auto-Refresh" to update every 5 seconds
- 🔃 **Manual Refresh**: "Refresh Now" button for immediate updates
- 📱 **Live Feed**: Shows latest 5 threats and incidents
- 📊 **Statistics**: View totals and critical threat count
- ⏰ **Last Update Time**: Shows when data was last refreshed

**Color Coding:**
- 🔴 **Red** = CRITICAL threats
- 🟠 **Orange** = HIGH threats
- 🔵 **Blue** = MEDIUM threats

**Real-Time Example:**
1. Switch to "Live Monitor" tab
2. Click "Start Auto-Refresh"
3. Open another window and add threats using "Add Threat" tab
4. Watch them appear live in the monitor feed!

### 4️⃣ **Settings Tab**

Data management and API endpoint information.

**Available Actions:**
- **Clear All Data** - Remove all threats and incidents (with confirmation)
- **View API Endpoints** - Reference for programmatic access

---

## Live Monitoring Workflow

### Scenario: Simulate a Cyber Attack

1. **Step 1: Initial Reconnaissance (Port Scan)**
   - Go to "Add Threat" tab
   - IP: `203.0.113.99`
   - Event Type: `Port Scan`
   - Risk Score: `70`
   - Click "Add Threat"

2. **Step 2: Enable Live Monitoring**
   - Switch to "Live Monitor" tab
   - Click "Start Auto-Refresh"
   - Watch the threat appear in the feed

3. **Step 3: Brute Force Attack**
   - Return to "Add Threat" tab
   - IP: `203.0.113.99`
   - Event Type: `Brute Force (AUTH_FAIL)`
   - Risk Score: `75`
   - Click "Add Threat"
   - See it update in the live monitor

4. **Step 4: Successful Breach (SQL Injection)**
   - IP: `203.0.113.99`
   - Event Type: `SQL Injection`
   - Risk Score: `95`
   - Click "Add Threat"
   - Watch threat level go to CRITICAL

5. **Step 5: Create Security Incident**
   - Switch to "Add Incident" tab
   - IP: `203.0.113.99`
   - Severity: `CRITICAL`
   - Description: "Multiple attacks detected - SQL injection on production database"
   - Click "Create Incident"
   - Incident appears in live monitor with automatic response actions

6. **Step 6: Monitor Response**
   - Watch the incident severity and action list in the live monitor
   - Dashboard KPI cards update automatically
   - Threat counts increase in real-time

---

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Add Threat | `Tab` to navigate form, `Enter` to submit |
| Auto-Refresh | Manual click (no keyboard shortcut) |
| Clear Data | Requires confirmation dialog |

---

## API Integration

The Custom Data Panel uses these backend API endpoints:

### Add Threat
```bash
POST /api/add-threat
Content-Type: application/json

{
  "source_ip": "192.168.1.50",
  "event_type": "MALWARE_ALERT",
  "risk_score": 85,
  "threat_level": "CRITICAL",
  "event_count": 1
}
```

### Add Incident
```bash
POST /api/add-incident
Content-Type: application/json

{
  "source_ip": "192.168.1.50",
  "event_type": "SECURITY_INCIDENT",
  "severity": "CRITICAL",
  "description": "Database breach detected"
}
```

### Get All Data
```bash
GET /api/data
```

### Clear All Data
```bash
POST /api/clear-all-data
```

---

## Tips & Tricks

### 🎨 Color-Coded Threats
- Red border = CRITICAL (80+)
- Orange border = HIGH (65-79)
- Blue border = MEDIUM (50-64)

### ⚡ Quick Testing
1. Open two browser windows side-by-side
2. Left window: "Add Threat" tab
3. Right window: "Live Monitor" tab
4. Add threats and watch them appear instantly in monitor

### 📊 Batch Testing
Create multiple threats rapidly:
```
1. SQL Injection (95) → See immediately
2. DDoS Attack (100) → Appears in live feed
3. Malware Alert (90) → Auto-updates stats
4. Privilege Escalation (88) → Triggers critical alert
```

### 🔄 Auto-Refresh Best Practices
- Enable auto-refresh (5 second intervals) when testing
- Disable if monitoring manually (saves server resources)
- Manually refresh when you need immediate updates

### 🧹 Clean Testing
- Clear all data before starting new tests
- Use "Settings" tab → "Clear All Data"
- Ensures accurate counts and fresh state

---

## Troubleshooting

### Data Not Appearing
**Problem**: Added threat but doesn't show in monitor
**Solution**:
1. Click "Refresh Now" or wait for auto-refresh (5 seconds)
2. Check browser console (F12) for errors
3. Verify backend is running: `http://localhost:8000/api/health`

### Auto-Refresh Not Working
**Problem**: Live monitor shows stale data
**Solution**:
1. Click "Stop Auto-Refresh" then "Start Auto-Refresh"
2. Manually click "Refresh Now"
3. Check network tab in browser dev tools (F12)

### Form Validation Errors
**Problem**: Cannot submit threat form
**Solution**:
1. Ensure Source IP is valid format (e.g., `192.168.1.50`)
2. Select an Event Type from dropdown
3. Risk Score must be between 0-100
4. All required fields must be filled

### Backend Connection Issues
**Problem**: "Failed to connect to API" message
**Solution**:
1. Verify Flask backend is running: `python api_server.py`
2. Check if running on port 8000
3. Ensure CORS is enabled in backend
4. Restart both backend and frontend servers

---

## Data Persistence

- ✅ Data is saved to JSON files immediately
- ✅ Persists across browser refreshes
- ✅ Survives frontend server restart
- ⚠️ Lost if backend is restarted (unless manually imported)

---

## Advanced Features

### Custom Risk Scores
- Drag the risk score slider to set precise values
- Threat level auto-adjusts:
  - 0-49: Below threshold (not flagged)
  - 50-64: MEDIUM
  - 65-79: HIGH
  - 80-100: CRITICAL

### Multiple Threat Sources
- Add threats from different IPs simultaneously
- Monitor how system handles multiple concurrent threats
- Perfect for stress testing the dashboard

### Incident Tracking
- Each incident gets auto-generated `incident_id`
- Timestamp automatically set to current time
- Response actions listed based on severity
- Description persists for reference

---

## Performance Metrics

**Expected Performance:**
- Add Threat: < 500ms
- Add Incident: < 500ms
- Auto-Refresh: 5 second interval
- Live Monitor: Handles 1000+ entries
- Dashboard update: < 100ms

---

## Security Considerations

⚠️ **Note**: This is a TEST FEATURE. Use for:
- ✅ Development and testing
- ✅ Training and demonstrations
- ✅ Dashboard validation
- ❌ NOT for production data injection
- ❌ NOT for real threat management

---

## Example Test Cases

### Test Case 1: Single Threat Detection
```
1. Add threat: SQL Injection (95)
2. Expected: Shows as CRITICAL in monitor
3. Verify: Risk score 95, Threat level CRITICAL
```

### Test Case 2: Multi-Threat Scenario
```
1. Add threat: Port Scan (70)
2. Add threat: Brute Force (75)
3. Add threat: Malware Alert (90)
4. Expected: All 3 appear in live monitor
5. Verify: Total threats = 3, Critical = 1
```

### Test Case 3: Incident Response
```
1. Add incident: CRITICAL severity
2. Expected: Auto-generated incident_id
3. Verify: Actions include block_ip, isolate_system, notify_soc
```

### Test Case 4: Real-Time Monitoring
```
1. Open Live Monitor tab
2. Click "Start Auto-Refresh"
3. Add 5 threats rapidly
4. Expected: All appear within 5 seconds
5. Verify: Stats update in real-time
```

---

## Support & Questions

For issues or questions:
1. Check the troubleshooting section above
2. Review API response in browser console (F12)
3. Check backend logs for errors
4. Verify all services are running

---

**Happy Testing! 🎯🔐**

