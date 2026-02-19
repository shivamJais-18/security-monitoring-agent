<template>
  <div class="stats-panel">
    <h2>📊 Pipeline Statistics</h2>
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon">📝</div>
        <div class="stat-value">{{ stats.scaled }}</div>
        <div class="stat-label">Scaled Logs</div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">🔍</div>
        <div class="stat-value">{{ stats.analyzed }}</div>
        <div class="stat-label">Analyzed Events</div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">⚠️</div>
        <div class="stat-value">{{ stats.detected }}</div>
        <div class="stat-label">Threats Detected</div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">🎯</div>
        <div class="stat-value">{{ stats.incidents }}</div>
        <div class="stat-label">Incidents</div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  stats: {
    type: Object,
    default: () => ({ scaled: 0, analyzed: 0, detected: 0, incidents: 0 })
  }
})
</script>

<style scoped>
.stats-panel {
  background: rgba(30, 41, 59, 0.8);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  backdrop-filter: blur(10px);
}

.stats-panel h2 {
  margin: 0 0 1.5rem 0;
  font-size: 1.5rem;
  color: #60a5fa;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  gap: 1rem;
}

.stat-card {
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(59, 130, 246, 0.3);
  border-radius: 0.5rem;
  padding: 1rem;
  text-align: center;
  transition: all 0.3s ease;
}

.stat-card:hover {
  border-color: rgba(59, 130, 246, 0.6);
  background: rgba(15, 23, 42, 0.9);
  transform: translateY(-4px);
}

.stat-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.stat-value {
  font-size: 2rem;
  font-weight: bold;
  color: #60a5fa;
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 0.875rem;
  color: #94a3b8;
}
</style>
