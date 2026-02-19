<template>
  <div class="view-container">
    <div class="view-header">
      <h2>🌐 Network Map</h2>
      <div class="controls">
        <select class="filter-select">
          <option>All Systems</option>
          <option>Critical</option>
          <option>Compromised</option>
          <option>Monitored</option>
        </select>
      </div>
    </div>

    <div class="network-container">
      <svg class="network-graph" viewBox="0 0 1000 600" preserveAspectRatio="xMidYMid meet">
        <!-- Connection lines -->
        <g class="connections" stroke="rgba(59, 130, 246, 0.3)" stroke-width="2">
          <line x1="150" y1="150" x2="450" y2="150" />
          <line x1="150" y1="150" x2="300" y2="450" />
          <line x1="450" y1="150" x2="750" y2="150" />
          <line x1="450" y1="150" x2="600" y2="450" />
          <line x1="750" y1="150" x2="900" y2="300" />
          <line x1="300" y1="450" x2="600" y2="450" />
          <line x1="600" y1="450" x2="900" y2="450" />
        </g>

        <!-- Nodes -->
        <circle cx="150" cy="150" r="35" class="node core" />
        <text x="150" y="155" text-anchor="middle" class="node-label">Core</text>

        <circle cx="450" cy="150" r="35" class="node server" />
        <text x="450" y="155" text-anchor="middle" class="node-label">WEB-SRV-01</text>

        <circle cx="750" cy="150" r="35" class="node server" />
        <text x="750" y="155" text-anchor="middle" class="node-label">API-SRV-02</text>

        <circle cx="900" cy="300" r="35" class="node database" />
        <text x="900" y="305" text-anchor="middle" class="node-label">DB-01</text>

        <circle cx="300" cy="450" r="35" class="node workstation" />
        <text x="300" y="455" text-anchor="middle" class="node-label">WS-01</text>

        <circle cx="600" cy="450" r="35" class="node workstation threatened" />
        <text x="600" y="455" text-anchor="middle" class="node-label">WS-02</text>

        <circle cx="900" cy="450" r="35" class="node workstation" />
        <text x="900" y="455" text-anchor="middle" class="node-label">WS-03</text>
      </svg>
    </div>

    <div class="network-stats">
      <div class="stat-card">
        <div class="stat-icon">🖥️</div>
        <div class="stat-info">
          <div class="stat-label">Total Systems</div>
          <div class="stat-value">7</div>
        </div>
      </div>
      <div class="stat-card critical">
        <div class="stat-icon">⚠️</div>
        <div class="stat-info">
          <div class="stat-label">Threatened</div>
          <div class="stat-value">1</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">🔒</div>
        <div class="stat-info">
          <div class="stat-label">Secure</div>
          <div class="stat-value">6</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">📡</div>
        <div class="stat-info">
          <div class="stat-label">Active Connections</div>
          <div class="stat-value">15</div>
        </div>
      </div>
    </div>

    <div class="legend">
      <div class="legend-item">
        <div class="legend-color core"></div>
        <span>Core Network</span>
      </div>
      <div class="legend-item">
        <div class="legend-color server"></div>
        <span>Server</span>
      </div>
      <div class="legend-item">
        <div class="legend-color database"></div>
        <span>Database</span>
      </div>
      <div class="legend-item">
        <div class="legend-color workstation"></div>
        <span>Workstation</span>
      </div>
      <div class="legend-item">
        <div class="legend-color threatened"></div>
        <span>Threatened</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

defineProps({
  systems: Array
})
</script>

<style scoped>
.view-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.view-header h2 {
  margin: 0;
  font-size: 2rem;
}

.filter-select {
  background: rgba(148, 163, 184, 0.1);
  border: 1px solid rgba(148, 163, 184, 0.2);
  color: #e2e8f0;
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
}

.network-container {
  background: linear-gradient(135deg, rgba(15, 23, 42, 0.9), rgba(30, 41, 59, 0.7));
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  padding: 2rem;
  margin-bottom: 1.5rem;
  min-height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.network-graph {
  width: 100%;
  max-width: 1000px;
  height: auto;
}

.node {
  fill: rgba(59, 130, 246, 0.3);
  stroke: rgba(59, 130, 246, 0.8);
  stroke-width: 2;
  filter: drop-shadow(0 0 10px rgba(59, 130, 246, 0.2));
  transition: all 0.3s;
}

.node:hover {
  filter: drop-shadow(0 0 20px rgba(59, 130, 246, 0.5));
  stroke-width: 3;
}

.node.core {
  fill: rgba(34, 197, 94, 0.2);
  stroke: rgba(34, 197, 94, 0.8);
}

.node.core:hover {
  filter: drop-shadow(0 0 20px rgba(34, 197, 94, 0.5));
}

.node.server {
  fill: rgba(59, 130, 246, 0.2);
  stroke: rgba(59, 130, 246, 0.8);
}

.node.database {
  fill: rgba(245, 158, 11, 0.2);
  stroke: rgba(245, 158, 11, 0.8);
}

.node.workstation {
  fill: rgba(168, 85, 247, 0.2);
  stroke: rgba(168, 85, 247, 0.8);
}

.node.threatened {
  fill: rgba(239, 68, 68, 0.3);
  stroke: rgba(239, 68, 68, 0.9);
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% {
    filter: drop-shadow(0 0 10px rgba(239, 68, 68, 0.2));
  }
  50% {
    filter: drop-shadow(0 0 20px rgba(239, 68, 68, 0.5));
  }
}

.node-label {
  fill: #e2e8f0;
  font-size: 11px;
  font-weight: 600;
  pointer-events: none;
}

.connections {
  opacity: 0.5;
}

.network-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.stat-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  background: rgba(15, 23, 42, 0.8);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.5rem;
  padding: 1rem;
  transition: all 0.3s;
}

.stat-card:hover {
  border-color: rgba(59, 130, 246, 0.4);
}

.stat-card.critical {
  border-color: rgba(239, 68, 68, 0.3);
}

.stat-icon {
  font-size: 2rem;
}

.stat-info {
  flex: 1;
}

.stat-label {
  color: #94a3b8;
  font-size: 0.85rem;
}

.stat-value {
  color: #f1f5f9;
  font-size: 1.5rem;
  font-weight: 700;
}

.legend {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
  background: rgba(15, 23, 42, 0.8);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.5rem;
  padding: 1rem;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #cbd5e1;
}

.legend-color {
  width: 20px;
  height: 20px;
  border-radius: 0.25rem;
  border: 2px solid currentColor;
}

.legend-color.core {
  background: rgba(34, 197, 94, 0.3);
  border-color: rgba(34, 197, 94, 0.8);
}

.legend-color.server {
  background: rgba(59, 130, 246, 0.3);
  border-color: rgba(59, 130, 246, 0.8);
}

.legend-color.database {
  background: rgba(245, 158, 11, 0.3);
  border-color: rgba(245, 158, 11, 0.8);
}

.legend-color.workstation {
  background: rgba(168, 85, 247, 0.3);
  border-color: rgba(168, 85, 247, 0.8);
}

.legend-color.threatened {
  background: rgba(239, 68, 68, 0.3);
  border-color: rgba(239, 68, 68, 0.8);
}
</style>
