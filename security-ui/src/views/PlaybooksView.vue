<template>
  <div class="view-container">
    <div class="view-header">
      <h2>📚 Incident Playbooks</h2>
      <button class="btn-primary">+ New Playbook</button>
    </div>

    <div class="playbooks-grid">
      <div v-for="playbook in playbooks" :key="playbook.id" class="playbook-card">
        <div class="playbook-header">
          <h3>{{ playbook.name }}</h3>
          <span class="playbook-type">{{ playbook.type }}</span>
        </div>
        <p class="playbook-desc">{{ playbook.description }}</p>
        
        <div class="playbook-steps">
          <div class="step-label">Steps</div>
          <ol class="steps-list">
            <li v-for="(step, idx) in playbook.steps.slice(0, 3)" :key="idx">
              {{ step }}
            </li>
          </ol>
          <span v-if="playbook.steps.length > 3" class="more-steps">+{{ playbook.steps.length - 3 }} more...</span>
        </div>

        <div class="playbook-meta">
          <span class="meta-item">
            <strong>Triggers:</strong> {{ playbook.triggers.length }}
          </span>
          <span class="meta-item">
            <strong>MTTR:</strong> {{ playbook.mttr }}
          </span>
        </div>

        <div class="playbook-actions">
          <button class="btn-small">View</button>
          <button class="btn-small">Edit</button>
          <button class="btn-small negative">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const playbooks = ref([
  {
    id: 1,
    name: 'Ransomware Response',
    type: 'Security',
    description: 'Automated response procedures for ransomware detection and containment',
    steps: [
      'Isolate affected hosts from network',
      'Snapshot systems for forensics',
      'Block C2 communications',
      'Initiate backup restoration protocol',
      'Conduct security audit'
    ],
    triggers: ['HIGH_RISK_BEHAVIOR', 'RANSOM_NOTE_DETECTED'],
    mttr: '45 min'
  },
  {
    id: 2,
    name: 'DDoS Attack Mitigation',
    type: 'Network',
    description: 'Defensive procedures for distributed denial-of-service attacks',
    steps: [
      'Activate DDoS scrubbing center',
      'Rate limit traffic from suspicious IPs',
      'Enable geo-blocking if applicable',
      'Scale infrastructure capacity',
      'Notify upstream ISP'
    ],
    triggers: ['TRAFFIC_SPIKE', 'MULTIPLE_SOURCES'],
    mttr: '15 min'
  },
  {
    id: 3,
    name: 'Data Exfiltration Response',
    type: 'Incident',
    description: 'Response protocol for unauthorized data access and transfer',
    steps: [
      'Block suspicious user accounts',
      'Monitor network egress points',
      'Revoke API tokens and credentials',
      'Quarantine data stores',
      'Notify compliance team'
    ],
    triggers: ['UNUSUAL_DATA_ACCESS', 'EXTERNAL_TRANSFER'],
    mttr: '30 min'
  },
  {
    id: 4,
    name: 'Malware Containment',
    type: 'Malware',
    description: 'Procedures for identifying and removing malware infections',
    steps: [
      'Quarantine infected systems',
      'Collect memory dumps and logs',
      'Run full system scan',
      'Remove malicious files',
      'Restore from clean backup'
    ],
    triggers: ['MALWARE_DETECTED', 'SUSPICIOUS_BEHAVIOR'],
    mttr: '60 min'
  }
])
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

.btn-primary {
  background: linear-gradient(135deg, #3b82f6, #0ea5e9);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);
}

.playbooks-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
}

.playbook-card {
  background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.5));
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  backdrop-filter: blur(10px);
  transition: all 0.3s;
}

.playbook-card:hover {
  border-color: rgba(59, 130, 246, 0.4);
  box-shadow: 0 20px 40px rgba(59, 130, 246, 0.1);
  transform: translateY(-2px);
}

.playbook-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 0.75rem;
}

.playbook-header h3 {
  margin: 0;
  font-size: 1.15rem;
  color: #f1f5f9;
}

.playbook-type {
  background: rgba(59, 130, 246, 0.2);
  color: #93c5fd;
  padding: 0.25rem 0.75rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.playbook-desc {
  color: #cbd5e1;
  margin: 0.5rem 0 1rem;
  font-size: 0.9rem;
  line-height: 1.4;
}

.playbook-steps {
  background: rgba(15, 23, 42, 0.7);
  padding: 1rem;
  border-radius: 0.5rem;
  margin-bottom: 1rem;
}

.step-label {
  font-weight: 600;
  color: #94a3b8;
  font-size: 0.85rem;
  margin-bottom: 0.5rem;
}

.steps-list {
  margin: 0;
  padding-left: 1.5rem;
  color: #cbd5e1;
  font-size: 0.85rem;
}

.steps-list li {
  margin-bottom: 0.4rem;
}

.more-steps {
  color: #64748b;
  font-style: italic;
  margin-top: 0.5rem;
  display: block;
}

.playbook-meta {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1);
  font-size: 0.85rem;
}

.meta-item {
  color: #94a3b8;
}

.meta-item strong {
  color: #cbd5e1;
}

.playbook-actions {
  display: flex;
  gap: 0.5rem;
}

.btn-small {
  flex: 1;
  background: rgba(59, 130, 246, 0.2);
  color: #93c5fd;
  border: 1px solid rgba(59, 130, 246, 0.3);
  padding: 0.5rem;
  border-radius: 0.35rem;
  cursor: pointer;
  font-size: 0.75rem;
  font-weight: 600;
  transition: all 0.3s;
}

.btn-small:hover {
  background: rgba(59, 130, 246, 0.3);
  border-color: rgba(59, 130, 246, 0.5);
}

.btn-small.negative {
  background: rgba(239, 68, 68, 0.1);
  color: #fca5a5;
  border-color: rgba(239, 68, 68, 0.2);
}

.btn-small.negative:hover {
  background: rgba(239, 68, 68, 0.2);
  border-color: rgba(239, 68, 68, 0.4);
}
</style>
