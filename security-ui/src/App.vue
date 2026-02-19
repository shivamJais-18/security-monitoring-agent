<template>
  <div class="dashboard-layout">
    <Sidebar :activeItem="activeItem" @select="activeItem = $event" />
    <div class="main-content">
      <Header />
      <div class="content-area">
        <!-- Dashboard View -->
        <template v-if="activeItem === 'Dashboard'">
          <KPICards :stats="stats" />
          <div class="dashboard-grid">
            <ThreatFeed :threats="threats" />
            <LogAnalyzer :logs="analyzed" />
          </div>
          <SystemHealthMonitor :systems="systems" />
        </template>

        <!-- Threat Feed View -->
        <template v-else-if="activeItem === 'Threat Feed'">
          <ThreatFeedView :threats="threats" />
        </template>

        <!-- Systems View -->
        <template v-else-if="activeItem === 'Systems'">
          <SystemsView :systems="systems" />
        </template>

        <!-- Log Analyzer View -->
        <template v-else-if="activeItem === 'Log Analyzer'">
          <LogAnalyzerView :logs="analyzed" />
        </template>

        <!-- Playbooks View -->
        <template v-else-if="activeItem === 'Playbooks'">
          <PlaybooksView />
        </template>

        <!-- Network Map View -->
        <template v-else-if="activeItem === 'Network Map'">
          <NetworkMapView :systems="systems" />
        </template>

        <!-- Analytics View -->
        <template v-else-if="activeItem === 'Analytics'">
          <AnalyticsView :stats="stats" :threats="threats" />
        </template>

        <!-- Threat Intel View -->
        <template v-else-if="activeItem === 'Threat Intel'">
          <ThreatIntelView />
        </template>

        <!-- Custom Data Panel View -->
        <template v-else-if="activeItem === 'Custom Data'">
          <CustomDataPanel />
        </template>

        <!-- SOC Team View -->
        <template v-else-if="activeItem === 'SOC Team'">
          <SOCTeamView />
        </template>

        <!-- Settings View -->
        <template v-else-if="activeItem === 'Settings'">
          <SettingsView />
        </template>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Sidebar from './components/Sidebar.vue'
import Header from './components/Header.vue'
import KPICards from './components/KPICards.vue'
import ThreatFeed from './components/ThreatFeed.vue'
import LogAnalyzer from './components/LogAnalyzer.vue'
import SystemHealthMonitor from './components/SystemHealthMonitor.vue'
import CustomDataPanel from './components/CustomDataPanel.vue'
import ThreatFeedView from './views/ThreatFeedView.vue'
import SystemsView from './views/SystemsView.vue'
import LogAnalyzerView from './views/LogAnalyzerView.vue'
import PlaybooksView from './views/PlaybooksView.vue'
import NetworkMapView from './views/NetworkMapView.vue'
import AnalyticsView from './views/AnalyticsView.vue'
import ThreatIntelView from './views/ThreatIntelView.vue'
import SOCTeamView from './views/SOCTeamView.vue'
import SettingsView from './views/SettingsView.vue'

const activeItem = ref('Dashboard')
const threats = ref([])
const incidents = ref([])
const analyzed = ref([])
const stats = ref({
  threatened: 0,
  incidents: 0,
  systems: 0,
  logsDay: 0,
  falsePositive: 0,
  mttr: 0
})
const systems = ref([])

const loadData = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/data')
    if (!response.ok) throw new Error('Failed to fetch')
    const data = await response.json()
    
    threats.value = data.threats || []
    incidents.value = data.incidents || []
    analyzed.value = data.analyzed || []
    
    generateSystemData()
    
    stats.value = {
      threatened: threats.value.length * 100 + Math.floor(Math.random() * 9000),
      incidents: incidents.value.length,
      systems: systems.value.length,
      logsDay: 156.7,
      falsePositive: 2.3,
      mttr: 24
    }
  } catch (err) {
    console.error(err)
    loadMockData()
  }
}

const generateSystemData = () => {
  systems.value = [
    { name: 'Web Server Cluster', type: 'Application Server', status: 'Healthy', cpu: 45, memory: 62, events: 1234 },
    { name: 'Database Primary', type: 'Database', status: 'Healthy', cpu: 38, memory: 78, events: 892 },
    { name: 'Firewall Edge', type: 'Network Security', status: 'Warning', cpu: 72, memory: 65, events: 45678 },
    { name: 'Mail Gateway', type: 'Email Security', status: 'Healthy', cpu: 28, memory: 45, events: 3456 },
    { name: 'VPN Concentrator', type: 'Network Access', status: 'Critical', cpu: 92, memory: 88, events: 789 },
    { name: 'Log Aggregator', type: 'SIEM', status: 'Healthy', cpu: 55, memory: 71, events: 156789 }
  ]
}

const loadMockData = () => {
  threats.value = [
    { id: 1, name: 'Ransomware Detected', severity: 'CRITICAL', status: 'Active', description: 'Suspicious file encryption activity detected', source: '192.168.1.105', target: 'File Server Alpha', time: '2 minutes ago' },
    { id: 2, name: 'Brute Force Attack', severity: 'HIGH', status: 'Investigating', description: 'Multiple failed authentication attempts', source: '45.33.32.156', target: 'SSH Gateway', time: '15 minutes ago' },
    { id: 3, name: 'Suspicious DNS Query', severity: 'MEDIUM', status: 'Mitigated', description: 'Unusual DNS queries to known malicious domain', source: '192.168.2.88', target: 'DNS Resolver', time: 'about 1 hour ago' }
  ]
  stats.value = { threatened: 12847, incidents: 3, systems: 6, logsDay: 156.7, falsePositive: 2.3, mttr: 24 }
  generateSystemData()
}

onMounted(() => loadData())
</script>

<style scoped>
.dashboard-layout {
  display: flex;
  height: 100vh;
  background: #0a0e27;
  color: #e2e8f0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.content-area {
  flex: 1;
  overflow-y: auto;
  padding: 2rem;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin: 2rem 0;
}

@media (max-width: 1400px) {
  .dashboard-grid {
    grid-template-columns: 1fr;
  }
}
</style>
