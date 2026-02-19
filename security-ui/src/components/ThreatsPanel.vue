<template>
  <div class="threats-panel">
    <h2>⚠️ Detected Threats</h2>
    <div class="threats-list">
      <div v-if="threats.length === 0" class="empty-state">
        <p>No threats detected 🎉</p>
      </div>
      <div v-for="threat in threats" :key="threat.id" class="threat-card" :class="threat.threat_level?.toLowerCase()">
        <div class="threat-header">
          <span class="threat-type">{{ threat.event_type }}</span>
          <span class="threat-level" :class="threat.threat_level?.toLowerCase()">
            {{ threat.threat_level }}
          </span>
        </div>
        <div class="threat-body">
          <p><strong>Source IP:</strong> {{ threat.source_ip }}</p>
          <p><strong>Risk Score:</strong> {{ threat.risk_score }}/100</p>
        </div>
        <div class="threat-progress">
          <div class="progress-bar">
            <div class="progress-fill" :style="{ width: threat.risk_score + '%' }"></div>
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
.threats-panel {
  background: rgba(30, 41, 59, 0.8);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  backdrop-filter: blur(10px);
}

.threats-panel h2 {
  margin: 0 0 1.5rem 0;
  font-size: 1.5rem;
  color: #fca5a5;
}

.threats-list {
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
  border-left: 4px solid #f87171;
  border-radius: 0.5rem;
  padding: 1rem;
  transition: all 0.3s ease;
}

.threat-card:hover {
  background: rgba(15, 23, 42, 0.9);
  transform: translateX(4px);
}

.threat-card.critical {
  border-left-color: #dc2626;
  background: rgba(127, 29, 29, 0.2);
}

.threat-card.high {
  border-left-color: #ea580c;
  background: rgba(120, 53, 15, 0.2);
}

.threat-card.medium {
  border-left-color: #f59e0b;
  background: rgba(120, 53, 15, 0.15);
}

.threat-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.threat-type {
  font-weight: 600;
  color: #e2e8f0;
}

.threat-level {
  padding: 0.25rem 0.75rem;
  border-radius: 0.25rem;
  font-size: 0.875rem;
  font-weight: 600;
}

.threat-level.critical {
  background: rgba(220, 38, 38, 0.3);
  color: #fca5a5;
}

.threat-level.high {
  background: rgba(234, 88, 12, 0.3);
  color: #fed7aa;
}

.threat-level.medium {
  background: rgba(245, 158, 11, 0.3);
  color: #fde047;
}

.threat-body {
  font-size: 0.875rem;
  color: #cbd5e1;
  margin-bottom: 0.75rem;
}

.threat-body p {
  margin: 0.25rem 0;
}

.threat-progress {
  margin-top: 0.75rem;
}

.progress-bar {
  height: 6px;
  background: rgba(148, 163, 184, 0.2);
  border-radius: 3px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(to right, #ef4444, #dc2626);
  transition: width 0.3s ease;
}

.threat-card.high .progress-fill {
  background: linear-gradient(to right, #ea580c, #c2410c);
}

.threat-card.medium .progress-fill {
  background: linear-gradient(to right, #f59e0b, #d97706);
}
</style>
