<template>
  <div class="view-container">
    <h2>💻 Systems Management</h2>
    <div class="systems-list">
      <div v-for="system in systems" :key="system.name" class="system-detail-card" :class="system.status?.toLowerCase()">
        <div class="system-header">
          <div class="system-title">
            <h3>{{ system.name }}</h3>
            <p>{{ system.type }}</p>
          </div>
          <div class="system-status-badge" :class="system.status?.toLowerCase()">
            <span class="dot"></span> {{ system.status }}
          </div>
        </div>

        <div class="metrics-detailed">
          <div class="metric-box">
            <div class="metric-header">CPU Usage</div>
            <div class="metric-large">{{ system.cpu }}%</div>
            <div class="progress-bar">
              <div class="fill" :style="{ width: system.cpu + '%', background: getColor(system.cpu) }"></div>
            </div>
          </div>

          <div class="metric-box">
            <div class="metric-header">Memory Usage</div>
            <div class="metric-large">{{ system.memory }}%</div>
            <div class="progress-bar">
              <div class="fill" :style="{ width: system.memory + '%', background: getColor(system.memory) }"></div>
            </div>
          </div>

          <div class="metric-box">
            <div class="metric-header">Events Logged</div>
            <div class="metric-large">{{ system.events }}</div>
            <p class="metric-small">events in last 24h</p>
          </div>
        </div>

        <div class="system-actions">
          <button class="btn-action">📊 View Logs</button>
          <button class="btn-action">⚙️ Configure</button>
          <button class="btn-action">🔄 Restart</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  systems: Array
})

const getColor = (value) => {
  if (value >= 80) return '#ef4444'
  if (value >= 60) return '#f59e0b'
  return '#22c55e'
}
</script>

<style scoped>
.view-container h2 {
  margin: 0 0 2rem 0;
  font-size: 2rem;
}

.systems-list {
  display: grid;
  gap: 1.5rem;
}

.system-detail-card {
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-top: 3px solid #22c55e;
  border-radius: 0.75rem;
  padding: 2rem;
  transition: all 0.3s ease;
}

.system-detail-card.warning {
  border-top-color: #f59e0b;
}

.system-detail-card.critical {
  border-top-color: #ef4444;
}

.system-detail-card:hover {
  background: rgba(15, 23, 42, 0.95);
  border-color: rgba(148, 163, 184, 0.4);
}

.system-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.system-title h3 {
  margin: 0;
  font-size: 1.3rem;
  color: #e2e8f0;
}

.system-title p {
  margin: 0.25rem 0 0 0;
  color: #94a3b8;
}

.system-status-badge {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-weight: 600;
}

.system-status-badge.healthy {
  background: rgba(34, 197, 94, 0.2);
  color: #86efac;
}

.system-status-badge.warning {
  background: rgba(245, 158, 11, 0.2);
  color: #fde047;
}

.system-status-badge.critical {
  background: rgba(239, 68, 68, 0.2);
  color: #fca5a5;
}

.dot {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: currentColor;
}

.metrics-detailed {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.5rem;
}

.metric-box {
  background: rgba(15, 23, 42, 0.8);
  padding: 1rem;
  border-radius: 0.375rem;
  border-left: 3px solid #60a5fa;
}

.metric-header {
  font-size: 0.85rem;
  color: #94a3b8;
  margin-bottom: 0.5rem;
}

.metric-large {
  font-size: 1.75rem;
  font-weight: 700;
  color: #60a5fa;
  margin-bottom: 0.75rem;
}

.metric-small {
  font-size: 0.8rem;
  color: #64748b;
  margin: 0.5rem 0 0 0;
}

.progress-bar {
  height: 6px;
  background: rgba(148, 163, 184, 0.2);
  border-radius: 3px;
  overflow: hidden;
}

.fill {
  height: 100%;
  transition: width 0.3s ease;
}

.system-actions {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.btn-action {
  background: rgba(59, 130, 246, 0.2);
  border: 1px solid rgba(59, 130, 246, 0.3);
  color: #60a5fa;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
}

.btn-action:hover {
  background: rgba(59, 130, 246, 0.3);
  border-color: rgba(59, 130, 246, 0.5);
}
</style>
