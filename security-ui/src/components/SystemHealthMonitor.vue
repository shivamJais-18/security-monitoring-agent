<template>
  <div class="system-health">
    <h3>💻 System Health Monitor</h3>
    <div class="systems-grid">
      <div v-for="system in systems" :key="system.name" class="system-card" :class="system.status?.toLowerCase()">
        <div class="system-header">
          <div class="system-info">
            <h4>{{ system.name }}</h4>
            <p class="system-type">{{ system.type }}</p>
          </div>
          <div class="system-status" :class="system.status?.toLowerCase()">
            <span class="status-dot"></span>
            {{ system.status }}
          </div>
        </div>

        <div class="system-metrics">
          <div class="metric">
            <div class="metric-label">
              <span class="metric-icon">⚙️</span>
              CPU
            </div>
            <div class="metric-value">{{ system.cpu }}%</div>
            <div class="progress-bar">
              <div class="progress-fill" :style="{ width: system.cpu + '%', backgroundColor: getMetricColor(system.cpu) }"></div>
            </div>
          </div>

          <div class="metric">
            <div class="metric-label">
              <span class="metric-icon">💾</span>
              Memory
            </div>
            <div class="metric-value">{{ system.memory }}%</div>
            <div class="progress-bar">
              <div class="progress-fill" :style="{ width: system.memory + '%', backgroundColor: getMetricColor(system.memory) }"></div>
            </div>
          </div>
        </div>

        <div class="system-events">
          <span class="event-icon">📊</span>
          <strong>{{ system.events }}</strong> events
          <span class="scan-time">Scanned 1 minute ago</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  systems: {
    type: Array,
    default: () => []
  }
})

const getMetricColor = (value) => {
  if (value >= 80) return '#ef4444'  // Red
  if (value >= 60) return '#f59e0b'  // Orange
  return '#22c55e'  // Green
}
</script>

<style scoped>
.system-health {
  background: rgba(30, 41, 59, 0.8);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  padding: 2rem;
  backdrop-filter: blur(10px);
}

.system-health h3 {
  margin: 0 0 1.5rem 0;
  font-size: 1.25rem;
  color: #60a5fa;
}

.systems-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.system-card {
  background: linear-gradient(135deg, rgba(15, 23, 42, 0.8) 0%, rgba(30, 41, 59, 0.6) 100%);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  transition: all 0.3s ease;
}

.system-card:hover {
  background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.85) 100%);
  border-color: rgba(148, 163, 184, 0.4);
  transform: translateY(-4px);
}

.system-card.healthy {
  border-top: 3px solid #22c55e;
}

.system-card.warning {
  border-top: 3px solid #f59e0b;
}

.system-card.critical {
  border-top: 3px solid #ef4444;
}

.system-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
}

.system-info h4 {
  margin: 0 0 0.25rem 0;
  font-size: 1.1rem;
  color: #e2e8f0;
}

.system-type {
  margin: 0;
  font-size: 0.85rem;
  color: #94a3b8;
}

.system-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.85rem;
  font-weight: 600;
  padding: 0.5rem 0.75rem;
  border-radius: 0.375rem;
}

.system-status.healthy {
  background: rgba(34, 197, 94, 0.1);
  color: #86efac;
}

.system-status.warning {
  background: rgba(245, 158, 11, 0.1);
  color: #fde047;
}

.system-status.critical {
  background: rgba(239, 68, 68, 0.1);
  color: #fca5a5;
}

.status-dot {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.system-status.healthy .status-dot {
  background: #22c55e;
}

.system-status.warning .status-dot {
  background: #f59e0b;
}

.system-status.critical .status-dot {
  background: #ef4444;
}

.system-metrics {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

.metric {
  flex: 1;
}

.metric-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.85rem;
  color: #cbd5e1;
  margin-bottom: 0.25rem;
}

.metric-icon {
  font-size: 1rem;
}

.metric-value {
  font-size: 1.1rem;
  font-weight: 700;
  color: #60a5fa;
  margin-bottom: 0.5rem;
}

.progress-bar {
  height: 6px;
  background: rgba(148, 163, 184, 0.2);
  border-radius: 3px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  transition: width 0.3s ease;
}

.system-events {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.85rem;
  color: #64748b;
  padding: 0.75rem;
  background: rgba(148, 163, 184, 0.1);
  border-radius: 0.375rem;
}

.event-icon {
  font-size: 1rem;
}

.scan-time {
  margin-left: auto;
  font-size: 0.8rem;
}

@media (max-width: 1024px) {
  .systems-grid {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  }
}

@media (max-width: 768px) {
  .systems-grid {
    grid-template-columns: 1fr;
  }

  .system-card {
    padding: 1rem;
  }
}
</style>
