<template>
  <div class="log-analyzer">
    <div class="log-header">
      <h3>📋 Log Analyzer</h3>
      <span class="log-count">{{ logs.length }} entries</span>
    </div>

    <div class="log-filters">
      <div class="filter-search">
        <span class="search-icon">🔍</span>
        <input type="text" placeholder="Search logs..." />
      </div>
      <div class="filter-tabs">
        <button class="filter-tab active">Error</button>
        <button class="filter-tab">Warning</button>
        <button class="filter-tab">Info</button>
        <button class="filter-tab">Debug</button>
      </div>
    </div>

    <div class="logs-container">
      <div v-if="logs.length === 0" class="empty-state">
        <p>No logs found</p>
      </div>

      <div v-for="(log, idx) in logs.slice(0, 10)" :key="idx" class="log-entry" :class="getLogLevel(log)">
        <div class="log-timestamp">{{ log.timestamp || getRandomTime() }}</div>
        <div class="log-level" :class="getLogLevel(log)">
          {{ getLogLevelDisplay(log) }}
        </div>
        <div class="log-source">
          [{{ log.system || 'System' }}]
        </div>
        <div class="log-message">
          {{ log.message || log.description || 'System event' }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  logs: {
    type: Array,
    default: () => []
  }
})

const getLogLevel = (log) => {
  const level = log.label?.toLowerCase() || 'info'
  if (level.includes('error') || level.includes('critical')) return 'error'
  if (level.includes('warning')) return 'warning'
  if (level.includes('info')) return 'info'
  return 'debug'
}

const getLogLevelDisplay = (log) => {
  const level = getLogLevel(log)
  return level.toUpperCase()
}

const getRandomTime = () => {
  const hour = String(Math.floor(Math.random() * 24)).padStart(2, '0')
  const min = String(Math.floor(Math.random() * 60)).padStart(2, '0')
  const sec = String(Math.floor(Math.random() * 60)).padStart(2, '0')
  return `${hour}:${min}:${sec}`
}
</script>

<style scoped>
.log-analyzer {
  background: rgba(30, 41, 59, 0.8);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  backdrop-filter: blur(10px);
  display: flex;
  flex-direction: column;
}

.log-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.log-header h3 {
  margin: 0;
  font-size: 1.25rem;
  color: #60a5fa;
}

.log-count {
  background: rgba(59, 130, 246, 0.2);
  color: #93c5fd;
  padding: 0.25rem 0.75rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  border: 1px solid rgba(59, 130, 246, 0.3);
}

.log-filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

.filter-search {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(148, 163, 184, 0.1);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.375rem;
  padding: 0.5rem 0.75rem;
}

.filter-search input {
  background: none;
  border: none;
  outline: none;
  color: #e2e8f0;
  font-size: 0.875rem;
  flex: 1;
}

.filter-search input::placeholder {
  color: #64748b;
}

.filter-tabs {
  display: flex;
  gap: 0.5rem;
}

.filter-tab {
  background: transparent;
  border: 1px solid rgba(148, 163, 184, 0.2);
  color: #94a3b8;
  padding: 0.375rem 0.75rem;
  border-radius: 0.375rem;
  cursor: pointer;
  font-size: 0.8rem;
  transition: all 0.3s ease;
}

.filter-tab:hover,
.filter-tab.active {
  background: rgba(59, 130, 246, 0.2);
  border-color: rgba(59, 130, 246, 0.3);
  color: #60a5fa;
}

.logs-container {
  flex: 1;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  max-height: 300px;
}

.empty-state {
  text-align: center;
  padding: 2rem;
  color: #94a3b8;
}

.log-entry {
  display: grid;
  grid-template-columns: 60px 70px 130px 1fr;
  gap: 0.75rem;
  padding: 0.75rem;
  background: rgba(15, 23, 42, 0.6);
  border-left: 3px solid #64748b;
  border-radius: 0.375rem;
  font-size: 0.8rem;
  align-items: center;
  line-height: 1.4;
}

.log-entry.error {
  border-left-color: #ef4444;
  background: rgba(127, 29, 29, 0.1);
}

.log-entry.warning {
  border-left-color: #f59e0b;
  background: rgba(120, 53, 15, 0.1);
}

.log-entry.info {
  border-left-color: #3b82f6;
  background: rgba(30, 58, 138, 0.1);
}

.log-timestamp {
  color: #94a3b8;
  font-family: 'Courier New', monospace;
  font-weight: 600;
}

.log-level {
  border-radius: 0.25rem;
  padding: 0.25rem 0.5rem;
  font-weight: 600;
  text-align: center;
  font-size: 0.7rem;
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

.log-source {
  color: #64748b;
  font-family: 'Courier New', monospace;
  font-size: 0.75rem;
}

.log-message {
  color: #cbd5e1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.log-entry.error .log-message {
  color: #fca5a5;
}
</style>
