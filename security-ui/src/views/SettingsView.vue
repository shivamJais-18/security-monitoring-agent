<template>
  <div class="view-container">
    <div class="view-header">
      <h2>⚙️ Settings</h2>
    </div>

    <div class="settings-grid">
      <!-- System Configuration -->
      <div class="settings-card">
        <h3>🖥️ System Configuration</h3>
        <div class="setting-group">
          <label>Dashboard Refresh Interval</label>
          <select class="setting-input">
            <option>5 seconds</option>
            <option selected>10 seconds</option>
            <option>30 seconds</option>
            <option>1 minute</option>
          </select>
        </div>
        <div class="setting-group">
          <label>Data Retention Period</label>
          <input type="number" class="setting-input" value="90" />
          <span class="setting-hint">days</span>
        </div>
        <div class="setting-group checkbox">
          <input type="checkbox" id="log-archiving" checked />
          <label for="log-archiving">Enable Log Archiving</label>
        </div>
      </div>

      <!-- API Configuration -->
      <div class="settings-card">
        <h3>🔌 API Configuration</h3>
        <div class="setting-group">
          <label>Backend URL</label>
          <input type="text" class="setting-input" value="http://localhost:8000" />
        </div>
        <div class="setting-group">
          <label>API Timeout (seconds)</label>
          <input type="number" class="setting-input" value="30" />
        </div>
        <div class="setting-group">
          <label>API Key</label>
          <div class="api-key-display">
            <code>sk-••••••••••••••••••••••••••••••••</code>
            <button class="btn-small">Regenerate</button>
          </div>
        </div>
      </div>

      <!-- Notifications -->
      <div class="settings-card">
        <h3>🔔 Notification Preferences</h3>
        <div class="notification-settings">
          <div v-for="notif in notifications" :key="notif.id" class="notification-item">
            <div class="notif-header">
              <input type="checkbox" :id="'notif-' + notif.id" :checked="notif.enabled" />
              <label :for="'notif-' + notif.id">{{ notif.name }}</label>
            </div>
            <div class="notif-channels">
              <label v-for="channel in notif.channels" :key="channel" class="channel-checkbox">
                <input type="checkbox" :checked="true" />
                <span>{{ channel }}</span>
              </label>
            </div>
          </div>
        </div>
      </div>

      <!-- Alert Rules -->
      <div class="settings-card full-width">
        <h3>🚨 Alert Rules</h3>
        <div class="alert-rules">
          <div v-for="(rule, idx) in alertRules" :key="idx" class="rule-item">
            <div class="rule-name">{{ rule.name }}</div>
            <div class="rule-condition">Trigger when: {{ rule.condition }}</div>
            <div class="rule-actions">
              <button class="btn-small">Edit</button>
              <button class="btn-small negative">Delete</button>
            </div>
          </div>
        </div>
        <button class="btn-secondary">+ Add Alert Rule</button>
      </div>

      <!-- Integrations -->
      <div class="settings-card">
        <h3>🔗 Integrations</h3>
        <div class="integrations-list">
          <div v-for="integration in integrations" :key="integration.id" class="integration-item">
            <div class="integration-icon">{{ integration.icon }}</div>
            <div class="integration-info">
              <div class="integration-name">{{ integration.name }}</div>
              <div class="integration-status" :class="{ active: integration.active }">
                {{ integration.active ? 'Connected' : 'Disconnected' }}
              </div>
            </div>
            <button class="btn-small" :class="{ active: integration.active }">
              {{ integration.active ? 'Edit' : 'Configure' }}
            </button>
          </div>
        </div>
      </div>

      <!-- Security -->
      <div class="settings-card">
        <h3>🔐 Security Settings</h3>
        <div class="setting-group">
          <label>Authentication Method</label>
          <select class="setting-input">
            <option selected>Local User</option>
            <option>LDAP/Active Directory</option>
            <option>SAML 2.0</option>
            <option>OAuth2</option>
          </select>
        </div>
        <div class="setting-group checkbox">
          <input type="checkbox" id="mfa" checked />
          <label for="mfa">Require Multi-Factor Authentication</label>
        </div>
        <div class="setting-group checkbox">
          <input type="checkbox" id="audit" checked />
          <label for="audit">Enable Audit Logging</label>
        </div>
        <button class="btn-danger">Change Password</button>
      </div>

      <!-- About -->
      <div class="settings-card">
        <h3>ℹ️ About</h3>
        <div class="about-info">
          <div class="info-row">
            <span class="info-label">Version:</span>
            <span class="info-value">2.4.1</span>
          </div>
          <div class="info-row">
            <span class="info-label">Build:</span>
            <span class="info-value">build-20240115-alpha</span>
          </div>
          <div class="info-row">
            <span class="info-label">Backend:</span>
            <span class="info-value">Python 3.11 + Flask</span>
          </div>
          <div class="info-row">
            <span class="info-label">Frontend:</span>
            <span class="info-value">Vue 3 + Vite</span>
          </div>
          <div class="info-row">
            <span class="info-label">Last Updated:</span>
            <span class="info-value">15 January 2024</span>
          </div>
        </div>
        <button class="btn-secondary">Check for Updates</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const notifications = ref([
  {
    id: 1,
    name: 'Critical Threats',
    enabled: true,
    channels: ['Email', 'SMS', 'Slack']
  },
  {
    id: 2,
    name: 'High Priority Incidents',
    enabled: true,
    channels: ['Email', 'Slack']
  },
  {
    id: 3,
    name: 'System Alerts',
    enabled: true,
    channels: ['Email', 'Dashboard']
  },
  {
    id: 4,
    name: 'Compliance Violations',
    enabled: true,
    channels: ['Email', 'SMS']
  }
])

const alertRules = ref([
  {
    name: 'Ransomware Detection',
    condition: 'Multiple files encrypted in 5 minutes'
  },
  {
    name: 'Brute Force Attack',
    condition: '5+ failed login attempts in 5 minutes'
  },
  {
    name: 'Data Exfiltration',
    condition: '>100MB data transfer to external IP'
  }
])

const integrations = ref([
  {
    id: 1,
    name: 'Slack',
    icon: '💬',
    active: true
  },
  {
    id: 2,
    name: 'Jira',
    icon: '📋',
    active: true
  },
  {
    id: 3,
    name: 'Splunk',
    icon: '📊',
    active: false
  },
  {
    id: 4,
    name: 'ServiceNow',
    icon: '⚙️',
    active: false
  }
])
</script>

<style scoped>
.view-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.view-header h2 {
  margin: 0;
  font-size: 2rem;
}

.settings-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 1.5rem;
}

.settings-card {
  background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.5));
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
}

.settings-card h3 {
  margin: 0 0 1rem 0;
  font-size: 1.15rem;
  color: #f1f5f9;
}

.settings-card.full-width {
  grid-column: 1 / -1;
}

.setting-group {
  margin-bottom: 1rem;
}

.setting-group label {
  display: block;
  color: #cbd5e1;
  font-weight: 600;
  margin-bottom: 0.4rem;
  font-size: 0.9rem;
}

.setting-input {
  width: 100%;
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.2);
  color: #e2e8f0;
  padding: 0.6rem 0.8rem;
  border-radius: 0.4rem;
  font-size: 0.9rem;
  transition: all 0.3s;
}

.setting-input:focus {
  outline: none;
  border-color: rgba(59, 130, 246, 0.4);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.setting-hint {
  color: #94a3b8;
  font-size: 0.8rem;
  margin-left: 0.5rem;
}

.setting-group.checkbox {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.75rem;
}

.setting-group.checkbox input {
  width: 18px;
  height: 18px;
  cursor: pointer;
}

.setting-group.checkbox label {
  margin-bottom: 0;
  cursor: pointer;
  font-weight: 400;
}

.api-key-display {
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.4rem;
  padding: 0.75rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.api-key-display code {
  color: #93c5fd;
  font-family: 'Monaco', monospace;
  font-size: 0.8rem;
}

.notification-settings {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.notification-item {
  background: rgba(15, 23, 42, 0.7);
  padding: 1rem;
  border-radius: 0.4rem;
  border-left: 3px solid rgba(59, 130, 246, 0.3);
}

.notif-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
}

.notif-header input {
  width: 18px;
  height: 18px;
  cursor: pointer;
}

.notif-header label {
  color: #cbd5e1;
  font-weight: 600;
  cursor: pointer;
  margin: 0;
}

.notif-channels {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  padding-left: 1.75rem;
}

.channel-checkbox {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  color: #94a3b8;
  cursor: pointer;
  font-size: 0.85rem;
}

.channel-checkbox input {
  width: 16px;
  height: 16px;
  cursor: pointer;
}

.alert-rules {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.rule-item {
  background: rgba(15, 23, 42, 0.7);
  padding: 0.75rem;
  border-radius: 0.4rem;
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 1rem;
  align-items: center;
}

.rule-name {
  color: #f1f5f9;
  font-weight: 600;
}

.rule-condition {
  color: #94a3b8;
  font-size: 0.85rem;
  grid-column: 1 / -1;
  margin-top: -0.4rem;
}

.rule-actions {
  display: flex;
  gap: 0.5rem;
}

.btn-secondary {
  background: rgba(148, 163, 184, 0.1);
  color: #cbd5e1;
  border: 1px solid rgba(148, 163, 184, 0.2);
  padding: 0.6rem 1rem;
  border-radius: 0.4rem;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.3s;
}

.btn-secondary:hover {
  background: rgba(148, 163, 184, 0.15);
  border-color: rgba(148, 163, 184, 0.3);
}

.btn-danger {
  background: rgba(239, 68, 68, 0.2);
  color: #fca5a5;
  border: 1px solid rgba(239, 68, 68, 0.3);
  padding: 0.6rem 1rem;
  border-radius: 0.4rem;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.3s;
}

.btn-danger:hover {
  background: rgba(239, 68, 68, 0.3);
  border-color: rgba(239, 68, 68, 0.4);
}

.btn-small {
  background: rgba(59, 130, 246, 0.2);
  color: #93c5fd;
  border: 1px solid rgba(59, 130, 246, 0.3);
  padding: 0.35rem 0.6rem;
  border-radius: 0.25rem;
  cursor: pointer;
  font-size: 0.75rem;
  font-weight: 600;
  transition: all 0.3s;
}

.btn-small:hover {
  background: rgba(59, 130, 246, 0.3);
}

.btn-small.negative {
  background: rgba(239, 68, 68, 0.1);
  color: #fca5a5;
  border-color: rgba(239, 68, 68, 0.2);
}

.btn-small.negative:hover {
  background: rgba(239, 68, 68, 0.2);
}

.integrations-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.integration-item {
  background: rgba(15, 23, 42, 0.7);
  padding: 0.75rem;
  border-radius: 0.4rem;
  display: grid;
  grid-template-columns: 40px 1fr auto;
  gap: 1rem;
  align-items: center;
  border: 1px solid rgba(148, 163, 184, 0.1);
}

.integration-icon {
  font-size: 1.5rem;
}

.integration-info {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.integration-name {
  color: #cbd5e1;
  font-weight: 600;
}

.integration-status {
  color: #94a3b8;
  font-size: 0.8rem;
}

.integration-status.active {
  color: #86efac;
}

.about-info {
  background: rgba(15, 23, 42, 0.7);
  padding: 1rem;
  border-radius: 0.4rem;
  margin-bottom: 1rem;
}

.info-row {
  display: flex;
  justify-content: space-between;
  padding: 0.5rem 0;
  color: #cbd5e1;
  font-size: 0.9rem;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1);
}

.info-row:last-child {
  border-bottom: none;
}

.info-label {
  color: #94a3b8;
  font-weight: 600;
}

.info-value {
  color: #e2e8f0;
  font-family: 'Monaco', monospace;
}
</style>
