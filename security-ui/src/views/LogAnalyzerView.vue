<template>
  <div class="view-container">
    <div class="view-header">
      <h2>📋 Log Analyzer</h2>
      <div class="controls">
        <input type="text" placeholder="Search logs..." class="search-input" />
        <select class="filter-select">
          <option>All Levels</option>
          <option>Error</option>
          <option>Warning</option>
          <option>Info</option>
        </select>
      </div>
    </div>

    <div class="logs-detailed">
      <div v-for="(log, idx) in logs.slice(0, 50)" :key="idx" class="log-line" :class="getLogLevel(log)">
        <span class="log-time">{{ log.timestamp || getRandomTime() }}</span>
        <span class="log-level" :class="getLogLevel(log)">{{ getLogLevelDisplay(log) }}</span>
        <span class="log-component">[{{ log.event_type || 'System' }}]</span>
        <span class="log-message">{{ log.message || log.description || log.event_type || 'System event' }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  logs: Array
})

const getLogLevel = (log) => {
  const level = log.label?.toLowerCase() || log.severity?.toLowerCase() || 'info'
  if (level.includes('error') || level.includes('critical')) return 'error'
  if (level.includes('warning')) return 'warning'
  if (level.includes('suspicious')) return 'warning'
  return 'info'
}

const getLogLevelDisplay = (log) => {
  return getLogLevel(log).toUpperCase()
}

const getRandomTime = () => {
  const h = String(Math.floor(Math.random() * 24)).padStart(2, '0')
  const m = String(Math.floor(Math.random() * 60)).padStart(2, '0')
  const s = String(Math.floor(Math.random() * 60)).padStart(2, '0')
  return `${h}:${m}:${s}`
}
</script>

<style scoped>
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
}

.controls {
  display: flex;
  gap: 1rem;
}

.search-input, .filter-select {
  background: rgba(148, 163, 184, 0.1);
  border: 1px solid rgba(148, 163, 184, 0.2);
  color: #e2e8f0;
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
}

.logs-detailed {
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  font-family: 'Monaco', 'Courier New', monospace;
  max-height: 800px;
  overflow-y: auto;
}

.log-line {
  display: grid;
  grid-template-columns: 80px 80px 150px 1fr;
  gap: 1rem;
  padding: 0.75rem;
  border-left: 3px solid #64748b;
  margin-bottom: 0.5rem;
  font-size: 0.85rem;
}

.log-line.error {
  border-left-color: #ef4444;
  background: rgba(127, 29, 29, 0.1);
}

.log-line.warning {
  border-left-color: #f59e0b;
  background: rgba(120, 53, 15, 0.1);
}

.log-time {
  color: #94a3b8;
  font-weight: 600;
}

.log-level {
  font-weight: 700;
  border-radius: 0.25rem;
  padding: 0.25rem 0.5rem;
  text-align: center;
}

.log-level.error {
  background: rgba(239, 68, 68, 0.3);
  color: #fca5a5;
}

.log-level.warning {
  background: rgba(245, 158, 11, 0.3);
  color: #fde047;
}

.log-level.info {
  background: rgba(59, 130, 246, 0.2);
  color: #93c5fd;
}

.log-component {
  color: #94a3b8;
  font-weight: 600;
}

.log-message {
  color: #cbd5e1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>
