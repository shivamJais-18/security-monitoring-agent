<template>
  <div class="view-container">
    <div class="view-header">
      <h2>🔍 Threat Intelligence</h2>
      <div class="controls">
        <input type="text" placeholder="Search CVEs, IOCs..." class="search-input" />
      </div>
    </div>

    <div class="intel-sections">
      <!-- CVEs Section -->
      <div class="intel-card">
        <h3>⚠️ Critical CVEs</h3>
        <div class="intel-list">
          <div v-for="cve in criticalCves" :key="cve.id" class="intel-item">
            <div class="intel-header">
              <span class="intel-id">{{ cve.id }}</span>
              <span class="intel-score">CVSS {{ cve.score }}</span>
            </div>
            <p class="intel-desc">{{ cve.description }}</p>
            <div class="intel-meta">
              <span class="affected">Affected: {{ cve.affected }}</span>
              <button class="btn-small">Learn More</button>
            </div>
          </div>
        </div>
      </div>

      <!-- IOCs Section -->
      <div class="intel-card">
        <h3>📍 Indicators of Compromise (IOCs)</h3>
        <div class="ioc-filters">
          <button v-for="type in iocTypes" :key="type" 
                  :class="{ active: selectedIocType === type }"
                  @click="selectedIocType = type"
                  class="ioc-filter-btn">
            {{ type }}
          </button>
        </div>
        <div class="intel-list">
          <div v-for="ioc in filteredIocs" :key="ioc.id" class="ioc-item">
            <div class="ioc-header">
              <code class="ioc-value">{{ ioc.value }}</code>
              <span class="ioc-badge">{{ ioc.type }}</span>
            </div>
            <p class="ioc-desc">{{ ioc.description }}</p>
            <div class="ioc-meta">
              <span>Seen: {{ ioc.seen }} times</span>
              <span>Last: {{ ioc.last }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Threat Feeds -->
      <div class="intel-card">
        <h3>📡 Active Threat Feeds</h3>
        <div class="feeds-list">
          <div v-for="feed in threatFeeds" :key="feed.id" class="feed-item">
            <div class="feed-status" :class="{ active: feed.active }"></div>
            <div class="feed-info">
              <div class="feed-name">{{ feed.name }}</div>
              <div class="feed-source">{{ feed.source }}</div>
            </div>
            <div class="feed-stats">
              <span class="indicators">{{ feed.indicators }} IOCs</span>
              <span class="updated">Updated {{ feed.updated }}</span>
            </div>
            <button class="btn-feed" :class="{ active: feed.active }">
              {{ feed.active ? 'Active' : 'Inactive' }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const selectedIocType = ref('All')

const iocTypes = ref(['All', 'IP Address', 'Domain', 'Hash', 'Email'])

const criticalCves = ref([
  {
    id: 'CVE-2024-1234',
    score: 9.8,
    description: 'Critical vulnerability in OpenSSL allowing remote code execution',
    affected: 'OpenSSL 1.1.1 to 3.0.7'
  },
  {
    id: 'CVE-2024-5678',
    score: 9.1,
    description: 'Authentication bypass in Windows Server component',
    affected: 'Windows Server 2019-2022'
  },
  {
    id: 'CVE-2024-9012',
    score: 8.7,
    description: 'Privilege escalation vulnerability in Kubernetes',
    affected: 'Kubernetes 1.24-1.27'
  }
])

const allIocs = ref([
  {
    id: 1,
    type: 'IP Address',
    value: '192.168.1.105',
    description: 'Known C2 server for Emotet malware',
    seen: 1247,
    last: '2 hours ago'
  },
  {
    id: 2,
    type: 'Domain',
    value: 'malicious-domain.xyz',
    description: 'Phishing domain targeting financial institutions',
    seen: 3421,
    last: '10 minutes ago'
  },
  {
    id: 3,
    type: 'Hash',
    value: 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6',
    description: 'Ransomware executable detected in multiple attacks',
    seen: 567,
    last: '1 day ago'
  },
  {
    id: 4,
    type: 'Email',
    value: 'attacker@phishing.net',
    description: 'Sender of credential harvesting emails',
    seen: 892,
    last: '3 hours ago'
  },
  {
    id: 5,
    type: 'IP Address',
    value: '10.10.10.50',
    description: 'Scanning activity detected from this IP',
    seen: 450,
    last: '30 minutes ago'
  }
])

const threatFeeds = ref([
  {
    id: 1,
    name: 'Abuse.ch URLhaus',
    source: 'abuse.ch',
    indicators: 15420,
    updated: '5 minutes ago',
    active: true
  },
  {
    id: 2,
    name: 'MISP Feed',
    source: 'misp-project.org',
    indicators: 42305,
    updated: '15 minutes ago',
    active: true
  },
  {
    id: 3,
    name: 'AlienVault OTX',
    source: 'otx.alienvault.com',
    indicators: 78934,
    updated: '2 hours ago',
    active: true
  },
  {
    id: 4,
    name: 'Custom Internal Feed',
    source: 'internal',
    indicators: 2145,
    updated: '1 hour ago',
    active: false
  }
])

const filteredIocs = computed(() => {
  if (selectedIocType.value === 'All') {
    return allIocs.value
  }
  return allIocs.value.filter(ioc => ioc.type === selectedIocType.value)
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

.search-input {
  background: rgba(148, 163, 184, 0.1);
  border: 1px solid rgba(148, 163, 184, 0.2);
  color: #e2e8f0;
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  min-width: 300px;
}

.intel-sections {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.intel-card {
  background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.5));
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
}

.intel-card h3 {
  margin: 0 0 1rem 0;
  font-size: 1.15rem;
  color: #f1f5f9;
}

.intel-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.intel-item {
  background: rgba(15, 23, 42, 0.7);
  border-left: 3px solid rgba(239, 68, 68, 0.5);
  border-radius: 0.5rem;
  padding: 1rem;
  transition: all 0.3s;
}

.intel-item:hover {
  border-color: rgba(239, 68, 68, 0.8);
  box-shadow: 0 0 15px rgba(239, 68, 68, 0.1);
}

.intel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.intel-id {
  font-family: 'Monaco', monospace;
  color: #f1f5f9;
  font-weight: 600;
}

.intel-score {
  background: rgba(239, 68, 68, 0.2);
  color: #fca5a5;
  padding: 0.25rem 0.75rem;
  border-radius: 0.25rem;
  font-size: 0.85rem;
  font-weight: 600;
}

.intel-desc {
  color: #cbd5e1;
  margin: 0.5rem 0;
  font-size: 0.9rem;
}

.intel-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #94a3b8;
  font-size: 0.85rem;
  padding-top: 0.75rem;
  border-top: 1px solid rgba(148, 163, 184, 0.1);
}

.btn-small {
  background: rgba(59, 130, 246, 0.2);
  color: #93c5fd;
  border: 1px solid rgba(59, 130, 246, 0.3);
  padding: 0.4rem 0.75rem;
  border-radius: 0.25rem;
  cursor: pointer;
  font-size: 0.8rem;
  transition: all 0.3s;
}

.btn-small:hover {
  background: rgba(59, 130, 246, 0.3);
}

.ioc-filters {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.ioc-filter-btn {
  background: rgba(148, 163, 184, 0.1);
  color: #94a3b8;
  border: 1px solid rgba(148, 163, 184, 0.2);
  padding: 0.4rem 0.8rem;
  border-radius: 0.25rem;
  cursor: pointer;
  font-size: 0.85rem;
  transition: all 0.3s;
}

.ioc-filter-btn.active {
  background: rgba(59, 130, 246, 0.3);
  color: #93c5fd;
  border-color: rgba(59, 130, 246, 0.4);
}

.ioc-item {
  background: rgba(15, 23, 42, 0.7);
  border-left: 3px solid rgba(59, 130, 246, 0.5);
  border-radius: 0.5rem;
  padding: 1rem;
  transition: all 0.3s;
}

.ioc-item:hover {
  border-color: rgba(59, 130, 246, 0.8);
}

.ioc-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
  gap: 1rem;
}

.ioc-value {
  font-family: 'Monaco', monospace;
  color: #93c5fd;
  background: rgba(15, 23, 42, 0.5);
  padding: 0.4rem 0.8rem;
  border-radius: 0.25rem;
  flex: 1;
  overflow: auto;
}

.ioc-badge {
  background: rgba(59, 130, 246, 0.2);
  color: #93c5fd;
  padding: 0.25rem 0.75rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 600;
  white-space: nowrap;
}

.ioc-desc {
  color: #cbd5e1;
  margin: 0.5rem 0;
  font-size: 0.9rem;
}

.ioc-meta {
  display: flex;
  gap: 1rem;
  color: #94a3b8;
  font-size: 0.85rem;
}

.feeds-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.feed-item {
  display: grid;
  grid-template-columns: 12px 1fr 2fr 100px;
  gap: 1rem;
  align-items: center;
  background: rgba(15, 23, 42, 0.7);
  padding: 1rem;
  border-radius: 0.5rem;
  border: 1px solid rgba(148, 163, 184, 0.1);
  transition: all 0.3s;
}

.feed-item:hover {
  border-color: rgba(59, 130, 246, 0.3);
}

.feed-status {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(239, 68, 68, 0.5);
  animation: pulse-dot 2s infinite;
}

.feed-status.active {
  background: rgba(34, 197, 94, 0.8);
  animation: pulse-dot-active 2s infinite;
}

@keyframes pulse-dot {
  0%, 100% { opacity: 0.5; }
  50% { opacity: 1; }
}

@keyframes pulse-dot-active {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.6; }
}

.feed-info {
  display: flex;
  flex-direction: column;
}

.feed-name {
  color: #f1f5f9;
  font-weight: 600;
}

.feed-source {
  color: #94a3b8;
  font-size: 0.85rem;
}

.feed-stats {
  display: flex;
  gap: 1.5rem;
  color: #94a3b8;
  font-size: 0.85rem;
}

.btn-feed {
  background: rgba(34, 197, 94, 0.1);
  color: #86efac;
  border: 1px solid rgba(34, 197, 94, 0.2);
  padding: 0.4rem 0.8rem;
  border-radius: 0.25rem;
  cursor: pointer;
  font-size: 0.8rem;
  transition: all 0.3s;
}

.btn-feed:not(.active) {
  background: rgba(148, 163, 184, 0.1);
  color: #94a3b8;
  border-color: rgba(148, 163, 184, 0.2);
}

.btn-feed:hover {
  opacity: 0.8;
}
</style>
