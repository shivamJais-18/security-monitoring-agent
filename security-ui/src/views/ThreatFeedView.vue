<template>
  <div class="view-container">
    <div class="view-header">
      <h2>🔴 Threat Feed</h2>
      <div class="view-controls">
        <input type="text" placeholder="Search threats..." class="search-input" />
        <select class="filter-select">
          <option>All Severities</option>
          <option>Critical</option>
          <option>High</option>
          <option>Medium</option>
          <option>Low</option>
        </select>
      </div>
    </div>

    <div class="threats-grid">
      <div v-if="threats.length === 0" class="empty-state">
        <p>No threats detected 🎉</p>
      </div>

      <div v-for="threat in threats" :key="threat.id" class="threat-card-large" :class="threat.severity?.toLowerCase()">
        <div class="threat-header">
          <div class="threat-title-section">
            <h3>{{ threat.name }}</h3>
            <p class="threat-description">{{ threat.description }}</p>
          </div>
          <div class="threat-badges">
            <span class="badge severity" :class="threat.severity?.toLowerCase()">{{ threat.severity }}</span>
            <span class="badge status" :class="threat.status?.toLowerCase()">{{ threat.status }}</span>
          </div>
        </div>

        <div class="threat-details">
          <div class="detail-item">
            <strong>Source IP:</strong>
            <code>{{ threat.source }}</code>
          </div>
          <div class="detail-item">
            <strong>Target:</strong>
            <code>{{ threat.target }}</code>
          </div>
          <div class="detail-item">
            <strong>Detected:</strong>
            <span>{{ threat.time }}</span>
          </div>
          <div class="detail-item">
            <strong>Risk Score:</strong>
            <span class="risk-score" :class="getRiskClass(threat.risk_score)">{{ threat.risk_score || 75 }}/100</span>
          </div>
        </div>

        <div class="threat-actions">
          <button class="action-btn block">🚫 Block IP</button>
          <button class="action-btn isolate">🔒 Isolate</button>
          <button class="action-btn investigate">🔍 Investigate</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  threats: {
    type: Array,
    default: () => []
  }
})

const getRiskClass = (score) => {
  if (score >= 80) return 'critical'
  if (score >= 60) return 'high'
  if (score >= 40) return 'medium'
  return 'low'
}
</script>

<style scoped>
.view-container {
  max-width: 1400px;
  margin: 0 auto;
}

.view-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.view-header h2 {
  margin: 0;
  font-size: 2rem;
  color: #fca5a5;
}

.view-controls {
  display: flex;
  gap: 1rem;
}

.search-input, .filter-select {
  background: rgba(148, 163, 184, 0.1);
  border: 1px solid rgba(148, 163, 184, 0.2);
  color: #e2e8f0;
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  font-size: 0.95rem;
}

.search-input:focus, .filter-select:focus {
  outline: none;
  background: rgba(59, 130, 246, 0.1);
  border-color: rgba(59, 130, 246, 0.3);
}

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: #94a3b8;
}

.threats-grid {
  display: grid;
  gap: 1.5rem;
}

.threat-card-large {
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-left: 4px solid #f87171;
  border-radius: 0.75rem;
  padding: 1.5rem;
  transition: all 0.3s ease;
}

.threat-card-large:hover {
  background: rgba(15, 23, 42, 0.95);
  border-color: rgba(148, 163, 184, 0.4);
  transform: translateX(4px);
}

.threat-card-large.critical {
  border-left-color: #dc2626;
}

.threat-card-large.high {
  border-left-color: #ea580c;
}

.threat-card-large.medium {
  border-left-color: #f59e0b;
}

.threat-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
  gap: 1rem;
}

.threat-title-section h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.3rem;
  color: #e2e8f0;
}

.threat-description {
  margin: 0;
  color: #cbd5e1;
  font-size: 0.95rem;
}

.threat-badges {
  display: flex;
  gap: 0.75rem;
}

.badge {
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-size: 0.85rem;
  font-weight: 600;
  white-space: nowrap;
}

.badge.severity.critical {
  background: rgba(220, 38, 38, 0.2);
  color: #fca5a5;
}

.badge.severity.high {
  background: rgba(234, 88, 12, 0.2);
  color: #fed7aa;
}

.badge.status.active {
  background: rgba(239, 68, 68, 0.2);
  color: #fca5a5;
}

.badge.status.investigating {
  background: rgba(245, 158, 11, 0.2);
  color: #fde047;
}

.threat-details {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin-bottom: 1rem;
  padding: 1rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.5rem;
}

.detail-item {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.detail-item strong {
  color: #94a3b8;
  font-size: 0.85rem;
}

.detail-item code {
  background: rgba(0, 0, 0, 0.3);
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  color: #60a5fa;
  font-family: 'Courier New', monospace;
}

.risk-score {
  font-weight: 600;
  font-size: 1.1rem;
}

.risk-score.critical {
  color: #ef4444;
}

.risk-score.high {
  color: #f97316;
}

.risk-score.medium {
  color: #eab308;
}

.risk-score.low {
  color: #22c55e;
}

.threat-actions {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.action-btn {
  padding: 0.75rem 1.25rem;
  border-radius: 0.5rem;
  border: none;
  color: white;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  font-size: 0.9rem;
}

.action-btn.block {
  background: #ef4444;
}

.action-btn.block:hover {
  background: #dc2626;
  transform: translateY(-2px);
}

.action-btn.isolate {
  background: #f97316;
}

.action-btn.isolate:hover {
  background: #ea580c;
  transform: translateY(-2px);
}

.action-btn.investigate {
  background: #3b82f6;
}

.action-btn.investigate:hover {
  background: #2563eb;
  transform: translateY(-2px);
}
</style>
