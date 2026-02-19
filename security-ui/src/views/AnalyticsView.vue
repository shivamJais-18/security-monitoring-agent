<template>
  <div class="view-container">
    <div class="view-header">
      <h2>📊 Analytics & Insights</h2>
      <div class="time-range">
        <button :class="{ active: timeRange === '24h' }" @click="timeRange = '24h'">24h</button>
        <button :class="{ active: timeRange === '7d' }" @click="timeRange = '7d'">7d</button>
        <button :class="{ active: timeRange === '30d' }" @click="timeRange = '30d'">30d</button>
      </div>
    </div>

    <div class="charts-grid">
      <!-- Threat Timeline -->
      <div class="chart-card">
        <h3>Threat Timeline</h3>
        <div class="chart-area">
          <svg viewBox="0 0 500 200" class="chart-svg">
            <!-- Y-axis -->
            <line x1="30" y1="10" x2="30" y2="170" stroke="rgba(148, 163, 184, 0.2)" stroke-width="2" />
            <!-- X-axis -->
            <line x1="30" y1="170" x2="480" y2="170" stroke="rgba(148, 163, 184, 0.2)" stroke-width="2" />
            
            <!-- Grid lines -->
            <line x1="30" y1="130" x2="480" y2="130" stroke="rgba(148, 163, 184, 0.1)" stroke-width="1" />
            <line x1="30" y1="90" x2="480" y2="90" stroke="rgba(148, 163, 184, 0.1)" stroke-width="1" />
            <line x1="30" y1="50" x2="480" y2="50" stroke="rgba(148, 163, 184, 0.1)" stroke-width="1" />
            
            <!-- Line chart -->
            <polyline points="30,150 80,130 130,140 180,100 230,110 280,80 330,90 380,70 430,85 480,50" 
                      fill="none" stroke="url(#lineGradient)" stroke-width="3" stroke-linecap="round" />
            
            <!-- Points -->
            <circle cx="30" cy="150" r="4" fill="rgba(59, 130, 246, 0.5)" />
            <circle cx="80" cy="130" r="4" fill="rgba(59, 130, 246, 0.5)" />
            <circle cx="130" cy="140" r="4" fill="rgba(59, 130, 246, 0.5)" />
            <circle cx="180" cy="100" r="4" fill="rgba(59, 130, 246, 0.5)" />
            <circle cx="230" cy="110" r="4" fill="rgba(59, 130, 246, 0.5)" />
            <circle cx="280" cy="80" r="4" fill="rgba(59, 130, 246, 0.5)" />
            <circle cx="330" cy="90" r="4" fill="rgba(59, 130, 246, 0.5)" />
            <circle cx="380" cy="70" r="4" fill="rgba(59, 130, 246, 0.5)" />
            <circle cx="430" cy="85" r="4" fill="rgba(59, 130, 246, 0.5)" />
            <circle cx="480" cy="50" r="4" fill="rgba(59, 130, 246, 0.5)" />

            <!-- Y labels -->
            <text x="20" y="175" text-anchor="end" font-size="11" fill="rgba(148, 163, 184, 0.6)">0</text>
            <text x="20" y="135" text-anchor="end" font-size="11" fill="rgba(148, 163, 184, 0.6)">50</text>
            <text x="20" y="95" text-anchor="end" font-size="11" fill="rgba(148, 163, 184, 0.6)">100</text>
            <text x="20" y="55" text-anchor="end" font-size="11" fill="rgba(148, 163, 184, 0.6)">150</text>

            <defs>
              <linearGradient id="lineGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#3b82f6;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#0ea5e9;stop-opacity:1" />
              </linearGradient>
            </defs>
          </svg>
        </div>
        <div class="chart-footer">Detected threats trending down - good progress</div>
      </div>

      <!-- Severity Distribution -->
      <div class="chart-card">
        <h3>Severity Distribution</h3>
        <div class="pie-chart">
          <svg viewBox="0 0 200 200" class="pie-svg">
            <!-- Critical -->
            <circle cx="100" cy="100" r="70" fill="none" stroke="rgba(239, 68, 68, 0.8)" stroke-width="35" stroke-dasharray="110 400" />
            <!-- High -->
            <circle cx="100" cy="100" r="70" fill="none" stroke="rgba(245, 158, 11, 0.8)" stroke-width="35" stroke-dasharray="140 400" stroke-dashoffset="-110" />
            <!-- Medium -->
            <circle cx="100" cy="100" r="70" fill="none" stroke="rgba(59, 130, 246, 0.8)" stroke-width="35" stroke-dasharray="80 400" stroke-dashoffset="-250" />
            <!-- Low -->
            <circle cx="100" cy="100" r="70" fill="none" stroke="rgba(34, 197, 94, 0.8)" stroke-width="35" stroke-dasharray="70 400" stroke-dashoffset="-330" />
            <!-- Center -->
            <circle cx="100" cy="100" r="45" fill="rgba(15, 23, 42, 1)" />
            <text x="100" y="105" text-anchor="middle" font-size="24" font-weight="700" fill="#f1f5f9">42</text>
          </svg>
        </div>
        <div class="pie-legend">
          <div><span class="dot critical"></span> Critical (11)</div>
          <div><span class="dot high"></span> High (14)</div>
          <div><span class="dot medium"></span> Medium (8)</div>
          <div><span class="dot low"></span> Low (7)</div>
        </div>
      </div>

      <!-- Top Attack Vectors -->
      <div class="chart-card full-width">
        <h3>Top Attack Vectors</h3>
        <div class="bar-chart">
          <div v-for="(item, idx) in topVectors" :key="idx" class="bar-item">
            <div class="bar-label">{{ item.name }}</div>
            <div class="bar-track">
              <div class="bar-fill" :style="{ width: item.percent + '%' }"></div>
            </div>
            <div class="bar-value">{{ item.count }} attacks</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const timeRange = ref('24h')

const topVectors = ref([
  { name: 'Phishing', count: 127, percent: 100 },
  { name: 'Brute Force', count: 89, percent: 70 },
  { name: 'SQL Injection', count: 54, percent: 42 },
  { name: 'XSS Attacks', count: 31, percent: 24 },
  { name: 'DDoS', count: 18, percent: 14 }
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

.time-range {
  display: flex;
  gap: 0.5rem;
  background: rgba(15, 23, 42, 0.8);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.5rem;
  padding: 0.5rem;
}

.time-range button {
  background: transparent;
  color: #94a3b8;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
  border-radius: 0.35rem;
  transition: all 0.3s;
}

.time-range button.active {
  background: rgba(59, 130, 246, 0.3);
  color: #93c5fd;
  border: 1px solid rgba(59, 130, 246, 0.4);
}

.charts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 1.5rem;
}

.chart-card {
  background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.5));
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
}

.chart-card h3 {
  margin: 0 0 1rem 0;
  font-size: 1.15rem;
  color: #f1f5f9;
}

.chart-card.full-width {
  grid-column: 1 / -1;
}

.chart-area {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 200px;
}

.chart-svg {
  width: 100%;
  height: 100%;
}

.chart-footer {
  color: #64748b;
  font-size: 0.85rem;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(148, 163, 184, 0.1);
}

.pie-chart {
  display: flex;
  justify-content: center;
  margin: 1rem 0;
}

.pie-svg {
  width: 150px;
  height: 150px;
  filter: drop-shadow(0 0 10px rgba(59, 130, 246, 0.1));
}

.pie-legend {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-top: 1rem;
  font-size: 0.85rem;
  color: #cbd5e1;
}

.pie-legend div {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 2px;
}

.dot.critical {
  background: rgba(239, 68, 68, 0.8);
}

.dot.high {
  background: rgba(245, 158, 11, 0.8);
}

.dot.medium {
  background: rgba(59, 130, 246, 0.8);
}

.dot.low {
  background: rgba(34, 197, 94, 0.8);
}

.bar-chart {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.bar-item {
  display: grid;
  grid-template-columns: 120px 1fr 80px;
  gap: 1rem;
  align-items: center;
}

.bar-label {
  color: #cbd5e1;
  font-weight: 600;
  font-size: 0.9rem;
}

.bar-track {
  background: rgba(15, 23, 42, 0.7);
  border-radius: 0.5rem;
  height: 24px;
  overflow: hidden;
}

.bar-fill {
  background: linear-gradient(90deg, rgba(59, 130, 246, 0.3), rgba(59, 130, 246, 0.8));
  height: 100%;
  border-radius: 0.5rem;
  transition: all 0.3s;
}

.bar-item:hover .bar-fill {
  background: linear-gradient(90deg, rgba(59, 130, 246, 0.5), rgba(0, 212, 255, 1));
}

.bar-value {
  color: #94a3b8;
  font-size: 0.85rem;
  text-align: right;
}
</style>
