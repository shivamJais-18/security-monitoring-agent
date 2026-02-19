<template>
  <div class="custom-data-panel">
    <div class="panel-header">
      <h2>🎯 Custom Data Monitor</h2>
      <div class="status-indicator" :class="{ 'connected': isConnected }">
        {{ isConnected ? '● Connected' : '○ Disconnected' }}
      </div>
    </div>

    <!-- Tabs -->
    <div class="tabs">
      <button 
        v-for="tab in tabs" 
        :key="tab"
        :class="['tab-btn', { active: activeTab === tab }]"
        @click="activeTab = tab"
      >
        {{ tab }}
      </button>
    </div>

    <!-- Add Threat Tab -->
    <div v-if="activeTab === 'Add Threat'" class="tab-content">
      <form @submit.prevent="addThreat" class="form-group">
        <h3>Add Custom Threat</h3>
        
        <div class="form-row">
          <div class="form-field">
            <label>Source IP</label>
            <input 
              v-model="threatForm.source_ip" 
              type="text" 
              placeholder="e.g., 192.168.1.50"
              required
            />
          </div>
          
          <div class="form-field">
            <label>Event Type</label>
            <select v-model="threatForm.event_type" required>
              <option value="">Select Event Type</option>
              <option value="AUTH_FAIL">Brute Force (AUTH_FAIL)</option>
              <option value="PORT_SCAN">Port Scan (PORT_SCAN)</option>
              <option value="MALWARE_ALERT">Malware Alert</option>
              <option value="SQL_INJECTION">SQL Injection</option>
              <option value="DDoS_DETECTED">DDoS Attack</option>
              <option value="PRIVILEGE_ESCALATION">Privilege Escalation</option>
              <option value="DATA_EXFILTRATION">Data Exfiltration</option>
              <option value="FIREWALL_BLOCK">Firewall Block</option>
            </select>
          </div>
        </div>

        <div class="form-row">
          <div class="form-field">
            <label>Risk Score (0-100)</label>
            <input 
              v-model.number="threatForm.risk_score" 
              type="range" 
              min="0" 
              max="100"
              @input="updateThreatLevel"
            />
            <span class="score-value">{{ threatForm.risk_score }}</span>
          </div>
          
          <div class="form-field">
            <label>Threat Level</label>
            <select v-model="threatForm.threat_level" required>
              <option value="MEDIUM">MEDIUM (50-64)</option>
              <option value="HIGH">HIGH (65-79)</option>
              <option value="CRITICAL">CRITICAL (80+)</option>
            </select>
          </div>
        </div>

        <div class="form-field">
          <label>Event Count</label>
          <input 
            v-model.number="threatForm.event_count" 
            type="number" 
            min="1"
            max="1000"
          />
        </div>

        <button type="submit" class="btn btn-primary" :disabled="submitting">
          {{ submitting ? '⏳ Adding...' : '➕ Add Threat' }}
        </button>
      </form>

      <div v-if="threatMessage" :class="['message', threatMessage.type]">
        {{ threatMessage.text }}
      </div>
    </div>

    <!-- Add Incident Tab -->
    <div v-if="activeTab === 'Add Incident'" class="tab-content">
      <form @submit.prevent="addIncident" class="form-group">
        <h3>Create Security Incident</h3>
        
        <div class="form-row">
          <div class="form-field">
            <label>Source IP</label>
            <input 
              v-model="incidentForm.source_ip" 
              type="text" 
              placeholder="e.g., 192.168.1.50"
              required
            />
          </div>
          
          <div class="form-field">
            <label>Event Type</label>
            <input 
              v-model="incidentForm.event_type" 
              type="text" 
              placeholder="e.g., SECURITY_INCIDENT"
            />
          </div>
        </div>

        <div class="form-row">
          <div class="form-field">
            <label>Severity</label>
            <select v-model="incidentForm.severity" required>
              <option value="MEDIUM">MEDIUM</option>
              <option value="HIGH">HIGH</option>
              <option value="CRITICAL">CRITICAL</option>
            </select>
          </div>
        </div>

        <div class="form-field">
          <label>Description</label>
          <textarea 
            v-model="incidentForm.description" 
            placeholder="Add incident details..."
            rows="3"
          ></textarea>
        </div>

        <button type="submit" class="btn btn-primary" :disabled="submitting">
          {{ submitting ? '⏳ Creating...' : '➕ Create Incident' }}
        </button>
      </form>

      <div v-if="incidentMessage" :class="['message', incidentMessage.type]">
        {{ incidentMessage.text }}
      </div>
    </div>

    <!-- Live Monitor Tab -->
    <div v-if="activeTab === 'Live Monitor'" class="tab-content monitor">
      <h3>Real-Time Data Feed</h3>
      
      <div class="monitor-controls">
        <button @click="startAutoRefresh" class="btn btn-small" :disabled="autoRefresh">
          🔄 Start Auto-Refresh (5s)
        </button>
        <button @click="stopAutoRefresh" class="btn btn-small" :disabled="!autoRefresh">
          ⏹️ Stop Auto-Refresh
        </button>
        <button @click="refreshData" class="btn btn-small">
          🔃 Refresh Now
        </button>
      </div>

      <!-- Threats Stream -->
      <div class="stream-section">
        <h4>📊 Latest Threats ({{ currentThreats.length }})</h4>
        <div v-if="currentThreats.length === 0" class="empty-state">
          No threats detected yet
        </div>
        <div v-else class="stream-items">
          <div 
            v-for="(threat, idx) in currentThreats.slice(0, 5)" 
            :key="idx"
            class="stream-item"
            :class="threat.threat_level.toLowerCase()"
          >
            <div class="item-header">
              <span class="threat-level">{{ threat.threat_level }}</span>
              <span class="event-type">{{ threat.event_type }}</span>
              <span class="risk-score">Risk: {{ threat.risk_score }}</span>
            </div>
            <div class="item-body">
              <span class="ip">🔗 {{ threat.source_ip }}</span>
              <span class="detection">{{ threat.detection_reason }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Incidents Stream -->
      <div class="stream-section">
        <h4>🚨 Latest Incidents ({{ currentIncidents.length }})</h4>
        <div v-if="currentIncidents.length === 0" class="empty-state">
          No incidents yet
        </div>
        <div v-else class="stream-items">
          <div 
            v-for="(incident, idx) in currentIncidents.slice(0, 5)" 
            :key="idx"
            class="stream-item"
            :class="incident.severity.toLowerCase()"
          >
            <div class="item-header">
              <span class="incident-id">{{ incident.incident_id }}</span>
              <span class="severity">{{ incident.severity }}</span>
            </div>
            <div class="item-body">
              <span class="ip">🔗 {{ incident.source_ip }}</span>
              <span class="description">{{ incident.description }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Stats -->
      <div class="stats-section">
        <h4>📈 Current Statistics</h4>
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-value">{{ currentThreats.length }}</div>
            <div class="stat-label">Total Threats</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">{{ currentIncidents.length }}</div>
            <div class="stat-label">Total Incidents</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">{{ criticalCount }}</div>
            <div class="stat-label">Critical Threats</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">{{ lastUpdateTime }}</div>
            <div class="stat-label">Last Update</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Settings Tab -->
    <div v-if="activeTab === 'Settings'" class="tab-content">
      <h3>Data Management</h3>
      
      <div class="settings-section">
        <h4>⚙️ Actions</h4>
        
        <button @click="clearAllData" class="btn btn-danger">
          🗑️ Clear All Data
        </button>
        
        <p class="help-text">This will clear all threats and incidents from the dashboard.</p>
      </div>

      <div class="settings-section">
        <h4>📖 API Endpoints</h4>
        <div class="api-info">
          <p><strong>Add Threat:</strong></p>
          <code>POST /api/add-threat</code>
          
          <p><strong>Add Incident:</strong></p>
          <code>POST /api/add-incident</code>
          
          <p><strong>Clear Data:</strong></p>
          <code>POST /api/clear-all-data</code>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CustomDataPanel',
  data() {
    return {
      activeTab: 'Add Threat',
      tabs: ['Add Threat', 'Add Incident', 'Live Monitor', 'Settings'],
      submitting: false,
      autoRefresh: false,
      refreshInterval: null,
      isConnected: true,
      lastUpdateTime: 'Never',
      
      threatForm: {
        source_ip: '203.0.113.',
        event_type: 'MALWARE_ALERT',
        risk_score: 80,
        threat_level: 'CRITICAL',
        event_count: 1
      },
      
      incidentForm: {
        source_ip: '192.168.1.',
        event_type: 'SECURITY_INCIDENT',
        severity: 'CRITICAL',
        description: ''
      },
      
      threatMessage: null,
      incidentMessage: null,
      currentThreats: [],
      currentIncidents: []
    }
  },
  
  computed: {
    criticalCount() {
      return this.currentThreats.filter(t => t.threat_level === 'CRITICAL').length;
    }
  },
  
  mounted() {
    this.loadData();
  },
  
  beforeUnmount() {
    this.stopAutoRefresh();
  },
  
  methods: {
    async addThreat() {
      this.submitting = true;
      try {
        const response = await fetch('http://localhost:8000/api/add-threat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.threatForm)
        });
        
        if (response.ok) {
          this.threatMessage = {
            type: 'success',
            text: '✅ Threat added successfully!'
          };
          
          // Reset form
          this.threatForm.source_ip = '203.0.113.';
          this.threatForm.event_type = 'MALWARE_ALERT';
          this.threatForm.risk_score = 80;
          
          // Refresh data
          await this.loadData();
          
          // Clear message after 3 seconds
          setTimeout(() => this.threatMessage = null, 3000);
        } else {
          this.threatMessage = {
            type: 'error',
            text: '❌ Failed to add threat'
          };
        }
      } catch (error) {
        this.threatMessage = {
          type: 'error',
          text: `❌ Error: ${error.message}`
        };
      } finally {
        this.submitting = false;
      }
    },
    
    async addIncident() {
      this.submitting = true;
      try {
        const response = await fetch('http://localhost:8000/api/add-incident', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.incidentForm)
        });
        
        if (response.ok) {
          this.incidentMessage = {
            type: 'success',
            text: '✅ Incident created successfully!'
          };
          
          // Reset form
          this.incidentForm.source_ip = '192.168.1.';
          this.incidentForm.description = '';
          
          // Refresh data
          await this.loadData();
          
          // Clear message after 3 seconds
          setTimeout(() => this.incidentMessage = null, 3000);
        } else {
          this.incidentMessage = {
            type: 'error',
            text: '❌ Failed to create incident'
          };
        }
      } catch (error) {
        this.incidentMessage = {
          type: 'error',
          text: `❌ Error: ${error.message}`
        };
      } finally {
        this.submitting = false;
      }
    },
    
    async loadData() {
      try {
        const response = await fetch('http://localhost:8000/api/data');
        if (response.ok) {
          const data = await response.json();
          this.currentThreats = data.threats || [];
          this.currentIncidents = data.incidents || [];
          this.isConnected = true;
          this.updateLastTime();
        }
      } catch (error) {
        this.isConnected = false;
        console.error('Failed to load data:', error);
      }
    },
    
    async refreshData() {
      await this.loadData();
    },
    
    updateLastTime() {
      const now = new Date();
      this.lastUpdateTime = now.toLocaleTimeString();
    },
    
    startAutoRefresh() {
      this.autoRefresh = true;
      this.refreshInterval = setInterval(() => {
        this.loadData();
      }, 5000);
    },
    
    stopAutoRefresh() {
      this.autoRefresh = false;
      if (this.refreshInterval) {
        clearInterval(this.refreshInterval);
        this.refreshInterval = null;
      }
    },
    
    updateThreatLevel() {
      if (this.threatForm.risk_score >= 80) {
        this.threatForm.threat_level = 'CRITICAL';
      } else if (this.threatForm.risk_score >= 65) {
        this.threatForm.threat_level = 'HIGH';
      } else {
        this.threatForm.threat_level = 'MEDIUM';
      }
    },
    
    async clearAllData() {
      if (confirm('Are you sure you want to clear ALL data? This cannot be undone.')) {
        try {
          const response = await fetch('http://localhost:8000/api/clear-all-data', {
            method: 'POST'
          });
          
          if (response.ok) {
            await this.loadData();
            alert('✅ All data cleared');
          }
        } catch (error) {
          alert(`❌ Error: ${error.message}`);
        }
      }
    }
  }
}
</script>

<style scoped>
.custom-data-panel {
  background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
  border-radius: 12px;
  padding: 20px;
  color: #fff;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  margin: 20px 0;
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  border-bottom: 2px solid rgba(255, 255, 255, 0.2);
  padding-bottom: 10px;
}

.panel-header h2 {
  margin: 0;
  font-size: 24px;
  font-weight: bold;
}

.status-indicator {
  font-size: 14px;
  padding: 6px 12px;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 20px;
  transition: all 0.3s ease;
}

.status-indicator.connected {
  background: rgba(76, 175, 80, 0.3);
  color: #4caf50;
}

/* Tabs */
.tabs {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.tab-btn {
  padding: 10px 16px;
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(255, 255, 255, 0.2);
  color: #fff;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
}

.tab-btn:hover {
  background: rgba(255, 255, 255, 0.15);
  border-color: rgba(255, 255, 255, 0.4);
}

.tab-btn.active {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-color: #667eea;
}

.tab-content {
  background: rgba(0, 0, 0, 0.2);
  padding: 20px;
  border-radius: 8px;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Forms */
.form-group {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-group h3 {
  margin: 0 0 10px 0;
  font-size: 18px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
}

@media (max-width: 768px) {
  .form-row {
    grid-template-columns: 1fr;
  }
}

.form-field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.form-field label {
  font-weight: 600;
  font-size: 13px;
  text-transform: uppercase;
  opacity: 0.9;
}

.form-field input,
.form-field select,
.form-field textarea {
  padding: 10px 12px;
  border: 2px solid rgba(255, 255, 255, 0.2);
  background: rgba(0, 0, 0, 0.3);
  color: #fff;
  border-radius: 6px;
  font-size: 14px;
  font-family: inherit;
  transition: all 0.3s ease;
}

.form-field input:focus,
.form-field select:focus,
.form-field textarea:focus {
  outline: none;
  border-color: #667eea;
  background: rgba(102, 126, 234, 0.1);
}

.form-field textarea {
  resize: vertical;
  min-height: 80px;
}

.form-field input[type="range"] {
  padding: 6px;
  cursor: pointer;
}

.score-value {
  text-align: center;
  font-weight: bold;
  font-size: 16px;
  color: #667eea;
}

/* Buttons */
.btn {
  padding: 12px 20px;
  border: none;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 14px;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #fff;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}

.btn-danger {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  color: #fff;
}

.btn-danger:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(245, 87, 108, 0.4);
}

.btn-small {
  padding: 8px 16px;
  font-size: 13px;
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.btn-small:hover:not(:disabled) {
  background: rgba(255, 255, 255, 0.3);
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Messages */
.message {
  padding: 12px 16px;
  border-radius: 6px;
  margin-top: 10px;
  font-weight: 600;
  animation: slideIn 0.3s ease;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.message.success {
  background: rgba(76, 175, 80, 0.3);
  color: #4caf50;
  border: 1px solid rgba(76, 175, 80, 0.5);
}

.message.error {
  background: rgba(244, 67, 54, 0.3);
  color: #ff5252;
  border: 1px solid rgba(244, 67, 54, 0.5);
}

/* Monitor */
.monitor {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.monitor-controls {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.stream-section {
  background: rgba(0, 0, 0, 0.3);
  padding: 15px;
  border-radius: 8px;
  border-left: 4px solid #667eea;
}

.stream-section h4 {
  margin: 0 0 12px 0;
  font-size: 16px;
  color: #667eea;
}

.stream-items {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-height: 300px;
  overflow-y: auto;
}

.stream-item {
  background: rgba(0, 0, 0, 0.2);
  padding: 12px;
  border-radius: 6px;
  border-left: 4px solid #666;
  transition: all 0.3s ease;
}

.stream-item:hover {
  background: rgba(0, 0, 0, 0.3);
}

.stream-item.critical {
  border-left-color: #f5576c;
  background: rgba(245, 87, 108, 0.05);
}

.stream-item.high {
  border-left-color: #ffa502;
  background: rgba(255, 165, 2, 0.05);
}

.stream-item.medium {
  border-left-color: #667eea;
  background: rgba(102, 126, 234, 0.05);
}

.item-header {
  display: flex;
  gap: 10px;
  align-items: center;
  margin-bottom: 6px;
  flex-wrap: wrap;
}

.threat-level,
.incident-id,
.severity {
  font-weight: bold;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
  background: rgba(255, 255, 255, 0.1);
}

.event-type,
.detection {
  font-size: 12px;
  opacity: 0.8;
}

.risk-score {
  font-size: 12px;
  color: #667eea;
  font-weight: bold;
}

.item-body {
  display: flex;
  gap: 12px;
  font-size: 12px;
  opacity: 0.9;
  flex-wrap: wrap;
}

.empty-state {
  padding: 20px;
  text-align: center;
  opacity: 0.6;
  font-style: italic;
}

.stats-section {
  background: rgba(0, 0, 0, 0.3);
  padding: 15px;
  border-radius: 8px;
  border-left: 4px solid #667eea;
}

.stats-section h4 {
  margin: 0 0 12px 0;
  font-size: 16px;
  color: #667eea;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 10px;
}

.stat-card {
  background: rgba(102, 126, 234, 0.1);
  padding: 12px;
  border-radius: 6px;
  border: 1px solid rgba(102, 126, 234, 0.3);
  text-align: center;
}

.stat-value {
  font-size: 24px;
  font-weight: bold;
  color: #667eea;
}

.stat-label {
  font-size: 12px;
  opacity: 0.8;
  margin-top: 4px;
}

/* Settings */
.settings-section {
  margin-bottom: 20px;
  padding: 15px;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 8px;
}

.settings-section h4 {
  margin: 0 0 10px 0;
  color: #667eea;
}

.help-text {
  font-size: 12px;
  opacity: 0.7;
  margin: 10px 0 0 0;
}

.api-info {
  background: rgba(0, 0, 0, 0.3);
  padding: 12px;
  border-radius: 6px;
  font-size: 12px;
}

.api-info p {
  margin: 8px 0 4px 0;
  font-weight: 600;
}

.api-info code {
  background: rgba(0, 0, 0, 0.5);
  padding: 4px 8px;
  border-radius: 4px;
  color: #4caf50;
  display: inline-block;
  margin: 4px 0;
}

/* Scrollbar */
.stream-items::-webkit-scrollbar {
  width: 6px;
}

.stream-items::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 3px;
}

.stream-items::-webkit-scrollbar-thumb {
  background: rgba(102, 126, 234, 0.5);
  border-radius: 3px;
}

.stream-items::-webkit-scrollbar-thumb:hover {
  background: rgba(102, 126, 234, 0.8);
}
</style>
