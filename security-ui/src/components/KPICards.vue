<template>
  <div class="kpi-section">
    <h3>Key Performance Indicators</h3>
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-icon">🛡️</div>
        <div class="kpi-content">
          <div class="kpi-value">{{ stats.threatened }}</div>
          <div class="kpi-label">Threats Blocked</div>
          <div class="kpi-change positive">↓ 23% from last period</div>
        </div>
      </div>

      <div class="kpi-card alert">
        <div class="kpi-icon">⚠️</div>
        <div class="kpi-content">
          <div class="kpi-value">{{ stats.incidents }}</div>
          <div class="kpi-label">Active Incidents</div>
          <div class="kpi-change neutral">↑ 2% from last period</div>
        </div>
      </div>

      <div class="kpi-card">
        <div class="kpi-icon">💻</div>
        <div class="kpi-content">
          <div class="kpi-value">{{ stats.systems }}</div>
          <div class="kpi-label">Systems Monitored</div>
          <div class="kpi-change negative">↓ 45% from last period</div>
        </div>
      </div>

      <div class="kpi-card">
        <div class="kpi-icon">📊</div>
        <div class="kpi-content">
          <div class="kpi-value">{{ stats.logsDay }} GB</div>
          <div class="kpi-label">Logs/Day</div>
          <div class="kpi-change negative">↑ 12% from last period</div>
        </div>
      </div>

      <div class="kpi-card">
        <div class="kpi-icon">✅</div>
        <div class="kpi-content">
          <div class="kpi-value">{{ stats.falsePositive }}%</div>
          <div class="kpi-label">False Positive Rate</div>
          <div class="kpi-change positive">↓ 15% from last period</div>
        </div>
      </div>

      <div class="kpi-card">
        <div class="kpi-icon">⏱️</div>
        <div class="kpi-content">
          <div class="kpi-value">{{ stats.mttr }} min</div>
          <div class="kpi-label">MTTR</div>
          <div class="kpi-change positive">↓ 8% from last period</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  stats: {
    type: Object,
    default: () => ({
      threatened: 0,
      incidents: 0,
      systems: 0,
      logsDay: 0,
      falsePositive: 0,
      mttr: 0
    })
  }
})
</script>

<style scoped>
.kpi-section h3 {
  margin: 0 0 1rem 0;
  font-size: 1.1rem;
  color: #cbd5e1;
}

.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.kpi-card {
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(134, 239, 172, 0.3);
  border-left: 4px solid #22c55e;
  border-radius: 0.75rem;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  transition: all 0.3s ease;
}

.kpi-card:hover {
  background: rgba(15, 23, 42, 0.9);
  border-color: rgba(134, 239, 172, 0.6);
  transform: translateY(-4px);
}

.kpi-card.alert {
  border-left-color: #ef4444;
  border-color: rgba(239, 68, 68, 0.3);
}

.kpi-icon {
  font-size: 2rem;
}

.kpi-content {
  flex: 1;
}

.kpi-value {
  font-size: 1.75rem;
  font-weight: 700;
  color: #60a5fa;
  margin-bottom: 0.25rem;
}

.kpi-label {
  font-size: 0.875rem;
  color: #94a3b8;
  margin-bottom: 0.5rem;
}

.kpi-change {
  font-size: 0.75rem;
  font-weight: 600;
}

.kpi-change.positive {
  color: #22c55e;
}

.kpi-change.negative {
  color: #ef4444;
}

.kpi-change.neutral {
  color: #f59e0b;
}
</style>
