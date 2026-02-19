<template>
  <div class="dashboard">
    <header class="dashboard-header">
      <h1>🔒 Security Monitoring Dashboard</h1>
      <p class="subtitle">Real-time threat detection and incident response</p>
    </header>

    <div class="dashboard-grid">
      <StatsPanel :stats="stats" />
      <ThreatsPanel :threats="threats" />
      <IncidentsPanel :incidents="incidents" />
    </div>

    <div class="dashboard-actions">
      <button @click="loadData" class="btn btn-primary">
        🔄 Refresh Data
      </button>
      <button @click="runPipeline" class="btn btn-secondary">
        ▶️ Run Pipeline
      </button>
    </div>

    <div v-if="loading" class="loading">Loading data...</div>
    <div v-if="error" class="error">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import StatsPanel from './StatsPanel.vue'
import ThreatsPanel from './ThreatsPanel.vue'
import IncidentsPanel from './IncidentsPanel.vue'

const threats = ref([])
const incidents = ref([])
const stats = ref({ scaled: 0, analyzed: 0, detected: 0, incidents: 0 })
const loading = ref(false)
const error = ref('')

const loadData = async () => {
  loading.value = true
  error.value = ''
  
  try {
    // Fetch data from backend API
    const response = await fetch('http://localhost:8000/api/data')
    if (!response.ok) throw new Error(`API returned ${response.status}`)
    const data = await response.json()
    
    // Map API response to component state
    threats.value = data.threats || []
    incidents.value = data.incidents || []
    stats.value = data.stats || stats.value
    
    console.log('✅ Data loaded from backend API')
  } catch (err) {
    error.value = `Cannot connect to backend: ${err.message}. Using demo data.`
    console.warn('Backend unavailable, loading mock data:', err)
    // Use mock data as fallback
    loadMockData()
  } finally {
    loading.value = false
  }
}

const loadMockData = () => {
  threats.value = [
    { id: 1, source_ip: '192.168.1.105', event_type: 'PORT_SCAN', threat_level: 'HIGH', risk_score: 75 },
    { id: 2, source_ip: '10.0.0.50', event_type: 'AUTH_FAIL', threat_level: 'CRITICAL', risk_score: 85 },
    { id: 3, source_ip: '172.16.0.20', event_type: 'MALWARE_ALERT', threat_level: 'HIGH', risk_score: 92 },
  ]
  
  incidents.value = [
    { incident_id: 'INC-1708350000', source_ip: '10.0.0.50', severity: 'CRITICAL', actions_taken: ['block_ip', 'notify_soc'] },
    { incident_id: 'INC-1708350100', source_ip: '192.168.1.105', severity: 'HIGH', actions_taken: ['isolate_system'] },
  ]
  
  stats.value = { scaled: 2, analyzed: 2, detected: 3, incidents: 2 }
}

const runPipeline = async () => {
  loading.value = true
  try {
    const response = await fetch('http://localhost:8000/api/run-pipeline', { 
      method: 'POST' 
    })
    if (!response.ok) throw new Error('Pipeline execution failed')
    
    // Wait a moment then refresh data
    setTimeout(() => loadData(), 2000)
  } catch (err) {
    error.value = `Pipeline error: ${err.message}`
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadMockData()
})
</script>

<style scoped>
.dashboard {
  min-height: 100vh;
  background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
  color: #e2e8f0;
  padding: 2rem;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.dashboard-header {
  text-align: center;
  margin-bottom: 3rem;
}

.dashboard-header h1 {
  font-size: 2.5rem;
  margin: 0 0 0.5rem 0;
  color: #60a5fa;
}

.subtitle {
  font-size: 1.1rem;
  color: #94a3b8;
  margin: 0;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.dashboard-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 2rem;
}

.btn {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 0.5rem;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
}

.btn-primary {
  background: #3b82f6;
  color: white;
}

.btn-primary:hover {
  background: #2563eb;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
}

.btn-secondary {
  background: #10b981;
  color: white;
}

.btn-secondary:hover {
  background: #059669;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
}

.loading {
  text-align: center;
  padding: 2rem;
  font-size: 1.1rem;
  color: #60a5fa;
  animation: pulse 1.5s infinite;
}

.error {
  text-align: center;
  padding: 1rem;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid #ef4444;
  border-radius: 0.5rem;
  color: #fca5a5;
  margin-bottom: 1rem;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
</style>
