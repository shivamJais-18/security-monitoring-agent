<template>
  <div class="sidebar">
    <div class="logo">
      <span class="logo-icon">🔒</span>
      <span class="logo-text">SecurityOps</span>
    </div>
    
    <nav class="nav-menu">
      <div class="nav-section">
        <div 
          class="nav-item" 
          :class="{ active: activeItem === 'Dashboard' }"
          @click="$emit('select', 'Dashboard')"
        >
          <span class="icon">📊</span>
          <span>Dashboard</span>
        </div>
        <div 
          class="nav-item has-badge" 
          :class="{ active: activeItem === 'Threat Feed' }"
          @click="$emit('select', 'Threat Feed')"
        >
          <span class="icon">⚠️</span>
          <span>Threat Feed</span>
          <span class="badge">3</span>
        </div>
        <div 
          class="nav-item"
          :class="{ active: activeItem === 'Systems' }"
          @click="$emit('select', 'Systems')"
        >
          <span class="icon">📁</span>
          <span>Systems</span>
        </div>
        <div 
          class="nav-item"
          :class="{ active: activeItem === 'Log Analyzer' }"
          @click="$emit('select', 'Log Analyzer')"
        >
          <span class="icon">📝</span>
          <span>Log Analyzer</span>
        </div>
        <div 
          class="nav-item"
          :class="{ active: activeItem === 'Playbooks' }"
          @click="$emit('select', 'Playbooks')"
        >
          <span class="icon">📖</span>
          <span>Playbooks</span>
        </div>
        <div 
          class="nav-item"
          :class="{ active: activeItem === 'Custom Data' }"
          @click="$emit('select', 'Custom Data')"
        >
          <span class="icon">🎯</span>
          <span>Custom Data</span>
        </div>
        <div 
          class="nav-item"
          :class="{ active: activeItem === 'Network Map' }"
          @click="$emit('select', 'Network Map')"
        >
          <span class="icon">🗺️</span>
          <span>Network Map</span>
        </div>
      </div>

      <div class="nav-section">
        <div 
          class="nav-item"
          :class="{ active: activeItem === 'Analytics' }"
          @click="$emit('select', 'Analytics')"
        >
          <span class="icon">📈</span>
          <span>Analytics</span>
        </div>
        <div 
          class="nav-item"
          :class="{ active: activeItem === 'Threat Intel' }"
          @click="$emit('select', 'Threat Intel')"
        >
          <span class="icon">🧠</span>
          <span>Threat Intel</span>
        </div>
      </div>

      <div class="nav-section">
        <div 
          class="nav-item"
          :class="{ active: activeItem === 'SOC Team' }"
          @click="$emit('select', 'SOC Team')"
        >
          <span class="icon">👥</span>
          <span>SOC Team</span>
        </div>
        <div 
          class="nav-item"
          :class="{ active: activeItem === 'Settings' }"
          @click="$emit('select', 'Settings')"
        >
          <span class="icon">⚙️</span>
          <span>Settings</span>
        </div>
      </div>
    </nav>

    <div class="live-monitoring">
      <div class="monitoring-icon">⚡</div>
      <div class="monitoring-text">Live Monitoring</div>
      <div class="monitoring-stat">Processing 15,432 events/sec</div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  activeItem: String
})
</script>

<style scoped>
.sidebar {
  width: 250px;
  background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
  border-right: 1px solid rgba(148, 163, 184, 0.1);
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1.5rem;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1);
  margin-bottom: 1rem;
}

.logo-icon {
  font-size: 1.75rem;
}

.logo-text {
  font-size: 1.25rem;
  font-weight: 700;
  color: #60a5fa;
}

.nav-menu {
  flex: 1;
  padding: 1rem 0;
}

.nav-section {
  margin-bottom: 1rem;
  padding: 0.5rem 0;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1);
}

.nav-section:last-of-type {
  border-bottom: none;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  color: #cbd5e1;
  font-size: 0.95rem;
}

.nav-item:hover {
  background: rgba(59, 130, 246, 0.1);
  color: #60a5fa;
}

.nav-item.active {
  background: rgba(59, 130, 246, 0.2);
  color: #60a5fa;
  border-left: 3px solid #60a5fa;
  padding-left: calc(1.5rem - 3px);
}

.icon {
  font-size: 1.25rem;
  min-width: 1.5rem;
}

.badge {
  margin-left: auto;
  background: #ef4444;
  color: white;
  border-radius: 9999px;
  padding: 0.25rem 0.5rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.live-monitoring {
  border-top: 1px solid rgba(148, 163, 184, 0.1);
  padding: 1rem 1.5rem;
  background: rgba(34, 197, 94, 0.1);
  color: #86efac;
  font-size: 0.875rem;
}

.monitoring-icon {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}

.monitoring-text {
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.monitoring-stat {
  font-size: 0.75rem;
  color: #22c55e;
}
</style>
