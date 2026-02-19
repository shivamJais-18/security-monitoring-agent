<template>
  <div class="incidents-panel">
    <h2>🎯 Active Incidents</h2>
    <div class="incidents-list">
      <div v-if="incidents.length === 0" class="empty-state">
        <p>No active incidents 😊</p>
      </div>
      <div v-for="incident in incidents" :key="incident.incident_id" class="incident-card">
        <div class="incident-header">
          <div class="incident-id">{{ incident.incident_id }}</div>
          <span class="incident-severity" :class="incident.severity?.toLowerCase()">
            {{ incident.severity }}
          </span>
        </div>
        <div class="incident-body">
          <p><strong>Source IP:</strong> <code>{{ incident.source_ip }}</code></p>
          <p><strong>Type:</strong> {{ incident.event_type || 'General' }}</p>
        </div>
        <div class="incident-actions">
          <div class="action-label">Actions Taken:</div>
          <div class="action-tags">
            <span v-for="action in incident.actions_taken" :key="action" class="action-tag">
              {{ formatAction(action) }}
            </span>
          </div>
        </div>
        <div class="incident-timestamp">
          {{ formatTimestamp(incident.timestamp) }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  incidents: {
    type: Array,
    default: () => []
  }
})

const formatAction = (action) => {
  return action.replace(/_/g, ' ').split(' ').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ')
}

const formatTimestamp = (timestamp) => {
  if (!timestamp) return 'N/A'
  try {
    return new Date(timestamp).toLocaleString()
  } catch {
    return timestamp
  }
}
</script>

<style scoped>
.incidents-panel {
  background: rgba(30, 41, 59, 0.8);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  backdrop-filter: blur(10px);
}

.incidents-panel h2 {
  margin: 0 0 1.5rem 0;
  font-size: 1.5rem;
  color: #86efac;
}

.incidents-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-height: 500px;
  overflow-y: auto;
}

.empty-state {
  text-align: center;
  padding: 2rem;
  color: #94a3b8;
}

.incident-card {
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(134, 239, 172, 0.3);
  border-radius: 0.5rem;
  padding: 1rem;
  transition: all 0.3s ease;
}

.incident-card:hover {
  background: rgba(15, 23, 42, 0.9);
  border-color: rgba(134, 239, 172, 0.6);
}

.incident-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.incident-id {
  font-weight: 600;
  color: #86efac;
  font-family: 'Courier New', monospace;
  font-size: 0.9rem;
}

.incident-severity {
  padding: 0.25rem 0.75rem;
  border-radius: 0.25rem;
  font-size: 0.875rem;
  font-weight: 600;
}

.incident-severity.critical {
  background: rgba(220, 38, 38, 0.3);
  color: #fca5a5;
}

.incident-severity.high {
  background: rgba(234, 88, 12, 0.3);
  color: #fed7aa;
}

.incident-severity.medium {
  background: rgba(245, 158, 11, 0.3);
  color: #fde047;
}

.incident-severity.low {
  background: rgba(34, 197, 94, 0.3);
  color: #bbf7d0;
}

.incident-body {
  font-size: 0.875rem;
  color: #cbd5e1;
  margin-bottom: 0.75rem;
}

.incident-body p {
  margin: 0.25rem 0;
}

.incident-body code {
  background: rgba(0, 0, 0, 0.3);
  padding: 0.2rem 0.4rem;
  border-radius: 0.25rem;
  font-family: 'Courier New', monospace;
  color: #60a5fa;
}

.incident-actions {
  margin-bottom: 0.75rem;
}

.action-label {
  font-size: 0.875rem;
  font-weight: 600;
  color: #94a3b8;
  margin-bottom: 0.5rem;
}

.action-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.action-tag {
  background: rgba(59, 130, 246, 0.2);
  color: #93c5fd;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  border: 1px solid rgba(59, 130, 246, 0.3);
}

.incident-timestamp {
  font-size: 0.75rem;
  color: #64748b;
  text-align: right;
}
</style>
