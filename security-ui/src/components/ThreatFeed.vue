<template>
  <div class="threat-feed">
    <div class="threat-feed-header">
      <h3>🔴 Real-time Threat Feed</h3>
      <button class="view-all">View All →</button>
    </div>

    <div class="threats-container">
      <div v-if="threats.length === 0" class="empty-state">
        <p>No threats detected</p>
      </div>

      <div v-for="threat in threats.slice(0, 5)" :key="threat.id" class="threat-card" :class="threat.severity?.toLowerCase()">
        <div class="threat-icon">
          <span v-if="threat.severity === 'CRITICAL'">🛑</span>
          <span v-else-if="threat.severity === 'HIGH'">⚠️</span>
          <span v-else>⚡</span>
        </div>

        <div class="threat-details">
          <div class="threat-title">
            <span class="threat-name">{{ threat.name || 'Unknown Threat' }}</span>
            <span class="threat-badge" :class="threat.severity?.toLowerCase()">
              {{ threat.severity }}
            </span>
            <span class="threat-status" :class="threat.status?.toLowerCase()">
              {{ threat.status || 'Unknown' }}
            </span>
          </div>
          
          <p class="threat-description">
            {{ threat.description || 'No description available' }}
          </p>
          
          <div class="threat-meta">
            <span class="meta-item">
              <strong>Source:</strong> 
              <code>{{ threat.source || 'Unknown' }}</code>
            </span>
            <span class="meta-item">→</span>
            <span class="meta-item">
              <strong>Target:</strong> 
              <code>{{ threat.target || 'Unknown' }}</code>
            </span>
            <span class="meta-time">⏱️ {{ threat.time || 'Recently' }}</span>
          </div>
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
</script>

<style scoped>
.threat-feed {
  background: rgba(30, 41, 59, 0.8);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  backdrop-filter: blur(10px);
}

.threat-feed-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.threat-feed-header h3 {
  margin: 0;
  font-size: 1.25rem;
  color: #fca5a5;
}

.view-all {
  background: none;
  border: 1px solid rgba(96, 165, 250, 0.3);
  color: #60a5fa;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  cursor: pointer;
  font-size: 0.875rem;
  transition: all 0.3s ease;
}

.view-all:hover {
  background: rgba(59, 130, 246, 0.1);
  border-color: rgba(96, 165, 250, 0.6);
}

.threats-container {
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

.threat-card {
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-left: 4px solid #f87171;
  border-radius: 0.5rem;
  padding: 1rem;
  display: flex;
  gap: 1rem;
  transition: all 0.3s ease;
}

.threat-card:hover {
  background: rgba(15, 23, 42, 0.9);
  border-color: rgba(148, 163, 184, 0.4);
}

.threat-card.critical {
  border-left-color: #dc2626;
}

.threat-card.high {
  border-left-color: #ea580c;
}

.threat-card.medium {
  border-left-color: #f59e0b;
}

.threat-icon {
  font-size: 1.75rem;
  min-width: 2rem;
}

.threat-details {
  flex: 1;
}

.threat-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.5rem;
  flex-wrap: wrap;
}

.threat-name {
  font-weight: 600;
  color: #e2e8f0;
  font-size: 0.95rem;
}

.threat-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.threat-badge.critical {
  background: rgba(220, 38, 38, 0.3);
  color: #fca5a5;
}

.threat-badge.high {
  background: rgba(234, 88, 12, 0.3);
  color: #fed7aa;
}

.threat-badge.medium {
  background: rgba(245, 158, 11, 0.3);
  color: #fde047;
}

.threat-status {
  padding: 0.25rem 0.75rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.threat-status.active {
  background: rgba(239, 68, 68, 0.2);
  color: #fca5a5;
}

.threat-status.investigating {
  background: rgba(245, 158, 11, 0.2);
  color: #fde047;
}

.threat-status.mitigated {
  background: rgba(34, 197, 94, 0.2);
  color: #bbf7d0;
}

.threat-description {
  margin: 0.5rem 0;
  font-size: 0.875rem;
  color: #cbd5e1;
  line-height: 1.4;
}

.threat-meta {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.8rem;
}

.meta-item {
  color: #94a3b8;
}

.meta-item code {
  background: rgba(0, 0, 0, 0.3);
  padding: 0.2rem 0.4rem;
  border-radius: 0.25rem;
  color: #60a5fa;
  font-family: 'Courier New', monospace;
}

.meta-time {
  margin-left: auto;
  color: #64748b;
}
</style>
