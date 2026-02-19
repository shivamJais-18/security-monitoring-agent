<template>
  <div class="view-container">
    <div class="view-header">
      <h2>👥 SOC Team</h2>
      <div class="controls">
        <button class="btn-primary">+ Add Team Member</button>
      </div>
    </div>

    <div class="team-sections">
      <!-- Current Shift -->
      <div class="team-card">
        <h3>🟢 Currently On-Duty ({{ currentShift.length }})</h3>
        <div class="team-grid">
          <div v-for="member in currentShift" :key="member.id" class="member-card on-duty">
            <div class="member-header">
              <div class="member-avatar">{{ member.initials }}</div>
              <div class="member-info">
                <div class="member-name">{{ member.name }}</div>
                <div class="member-role">{{ member.role }}</div>
              </div>
            </div>
            <div class="member-status">
              <span class="status-badge on-call">On-Call</span>
              <span class="status-time">{{ member.shiftTime }}</span>
            </div>
            <div class="member-contact">
              <a :href="`tel:${member.phone}`" class="contact-link">📞 {{ member.phone }}</a>
            </div>
          </div>
        </div>
      </div>

      <!-- Off-Duty -->
      <div class="team-card">
        <h3>🔴 Off-Duty ({{ offDuty.length }})</h3>
        <div class="team-grid">
          <div v-for="member in offDuty" :key="member.id" class="member-card">
            <div class="member-header">
              <div class="member-avatar">{{ member.initials }}</div>
              <div class="member-info">
                <div class="member-name">{{ member.name }}</div>
                <div class="member-role">{{ member.role }}</div>
              </div>
            </div>
            <div class="member-status">
              <span class="status-badge off-call">Next: {{ member.nextShift }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Escalation Procedures -->
      <div class="team-card">
        <h3>📞 Escalation Procedures</h3>
        <div class="escalation-tree">
          <div v-for="(level, idx) in escalationLevels" :key="idx" class="escalation-level">
            <div class="level-header">
              <span class="level-number">{{ idx + 1 }}</span>
              <span class="level-name">{{ level.name }}</span>
            </div>
            <div class="level-members">
              <span v-for="member in level.members" :key="member" class="member-tag">{{ member }}</span>
            </div>
            <div class="level-action">
              <span class="action-time">Wait {{ level.wait }} min</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Shift Schedule -->
      <div class="team-card full-width">
        <h3>📅 Weekly Shift Schedule</h3>
        <div class="schedule-table">
          <div class="schedule-header">
            <div class="schedule-name">Team Member</div>
            <div v-for="day in weekDays" :key="day" class="schedule-day">{{ day }}</div>
          </div>
          <div v-for="member in allMembers" :key="member.id" class="schedule-row">
            <div class="schedule-name">{{ member.name }}</div>
            <div v-for="day in weekDays" :key="day" class="schedule-cell" :class="getShiftClass(member, day)">
              {{ getShiftLabel(member, day) }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'

const weekDays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

const allMembers = ref([
  {
    id: 1,
    name: 'Alex Johnson',
    role: 'Senior Analyst',
    initials: 'AJ',
    phone: '+1-555-0101',
    shiftTime: '8 hours',
    email: 'alex@security.local',
    schedule: [
      { day: 'Mon', shift: 'day' },
      { day: 'Tue', shift: 'day' },
      { day: 'Wed', shift: 'off' },
      { day: 'Thu', shift: 'off' },
      { day: 'Fri', shift: 'day' },
      { day: 'Sat', shift: 'evening' },
      { day: 'Sun', shift: 'off' }
    ]
  },
  {
    id: 2,
    name: 'Maya Chen',
    role: 'Threat Hunter',
    initials: 'MC',
    phone: '+1-555-0102',
    shiftTime: '8 hours',
    email: 'maya@security.local',
    schedule: [
      { day: 'Mon', shift: 'evening' },
      { day: 'Tue', shift: 'off' },
      { day: 'Wed', shift: 'evening' },
      { day: 'Thu', shift: 'evening' },
      { day: 'Fri', shift: 'off' },
      { day: 'Sat', shift: 'off' },
      { day: 'Sun', shift: 'night' }
    ]
  },
  {
    id: 3,
    name: 'David Park',
    role: 'Incident Responder',
    initials: 'DP',
    phone: '+1-555-0103',
    shiftTime: '8 hours',
    email: 'david@security.local',
    schedule: [
      { day: 'Mon', shift: 'night' },
      { day: 'Tue', shift: 'night' },
      { day: 'Wed', shift: 'day' },
      { day: 'Thu', shift: 'day' },
      { day: 'Fri', shift: 'off' },
      { day: 'Sat', shift: 'day' },
      { day: 'Sun', shift: 'off' }
    ]
  }
])

const currentShift = computed(() => {
  // Show first 2 members as on-duty (in real implementation, check actual time)
  return allMembers.value.slice(0, 2).map(m => ({
    ...m,
    shiftTime: `${8 + Math.floor(Math.random() * 4)} hours left`
  }))
})

const offDuty = computed(() => allMembers.value.slice(2))

const escalationLevels = ref([
  {
    name: 'Initial Response',
    members: ['On-Duty Analyst'],
    wait: 15
  },
  {
    name: 'Escalation 1',
    members: ['Senior Analyst', 'Threat Hunter'],
    wait: 20
  },
  {
    name: 'Escalation 2',
    members: ['Incident Commander', 'Security Manager'],
    wait: 30
  },
  {
    name: 'Critical Escalation',
    members: ['CISO', 'Legal', 'PR Team'],
    wait: 5
  }
])

const getShiftClass = (member, day) => {
  const dayShift = member.schedule.find(s => s.day === day)
  return dayShift?.shift || 'off'
}

const getShiftLabel = (member, day) => {
  const dayShift = member.schedule.find(s => s.day === day)
  if (!dayShift) return '-'
  const labels = { day: '9-17', evening: '17-01', night: '01-09', off: 'Off' }
  return labels[dayShift.shift]
}
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

.team-sections {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.team-card {
  background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.5));
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
}

.team-card h3 {
  margin: 0 0 1rem 0;
  font-size: 1.15rem;
  color: #f1f5f9;
}

.team-card.full-width {
  grid-column: 1 / -1;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
}

.member-card {
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.5rem;
  padding: 1rem;
  transition: all 0.3s;
}

.member-card:hover {
  border-color: rgba(59, 130, 246, 0.4);
  box-shadow: 0 10px 25px rgba(59, 130, 246, 0.1);
}

.member-card.on-duty {
  border-color: rgba(34, 197, 94, 0.3);
  background: rgba(34, 197, 94, 0.05);
}

.member-header {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 0.75rem;
}

.member-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.4), rgba(0, 212, 255, 0.4));
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  color: #93c5fd;
  font-size: 0.85rem;
}

.member-info {
  flex: 1;
}

.member-name {
  color: #f1f5f9;
  font-weight: 600;
  font-size: 0.95rem;
}

.member-role {
  color: #94a3b8;
  font-size: 0.8rem;
}

.member-status {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.status-badge {
  padding: 0.25rem 0.6rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.status-badge.on-call {
  background: rgba(34, 197, 94, 0.2);
  color: #86efac;
}

.status-badge.off-call {
  background: rgba(148, 163, 184, 0.1);
  color: #cbd5e1;
}

.status-time {
  color: #94a3b8;
  font-size: 0.75rem;
}

.member-contact {
  display: flex;
  gap: 0.5rem;
}

.contact-link {
  color: #93c5fd;
  text-decoration: none;
  font-size: 0.85rem;
  padding: 0.4rem 0.6rem;
  background: rgba(59, 130, 246, 0.1);
  border-radius: 0.25rem;
  transition: all 0.3s;
}

.contact-link:hover {
  background: rgba(59, 130, 246, 0.2);
}

.escalation-tree {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.escalation-level {
  background: rgba(15, 23, 42, 0.7);
  padding: 1rem;
  border-radius: 0.5rem;
  border-left: 3px solid rgba(59, 130, 246, 0.5);
}

.level-header {
  display: flex;
  gap: 1rem;
  margin-bottom: 0.5rem;
}

.level-number {
  background: rgba(59, 130, 246, 0.3);
  color: #93c5fd;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.85rem;
}

.level-name {
  color: #f1f5f9;
  font-weight: 600;
  display: flex;
  align-items: center;
}

.level-members {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.member-tag {
  background: rgba(59, 130, 246, 0.2);
  color: #93c5fd;
  padding: 0.25rem 0.6rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  border: 1px solid rgba(59, 130, 246, 0.3);
}

.level-action {
  color: #94a3b8;
  font-size: 0.8rem;
  font-style: italic;
}

.schedule-table {
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.1);
  border-radius: 0.5rem;
  overflow: auto;
}

.schedule-header {
  display: grid;
  grid-template-columns: 150px repeat(7, 1fr);
  gap: 0.5px;
  background: rgba(15, 23, 42, 0.9);
  border-bottom: 2px solid rgba(148, 163, 184, 0.2);
  font-weight: 600;
  color: #94a3b8;
  font-size: 0.85rem;
}

.schedule-header > * {
  padding: 0.75rem;
  text-align: center;
}

.schedule-row {
  display: grid;
  grid-template-columns: 150px repeat(7, 1fr);
  gap: 0.5px;
  border-bottom: 1px solid rgba(148, 163, 184, 0.05);
}

.schedule-name {
  padding: 0.75rem;
  color: #cbd5e1;
  font-weight: 600;
  background: rgba(15, 23, 42, 0.8);
}

.schedule-cell {
  padding: 0.75rem;
  text-align: center;
  font-size: 0.8rem;
  color: #cbd5e1;
  background: rgba(30, 41, 59, 0.5);
}

.schedule-cell.day {
  background: rgba(34, 197, 94, 0.1);
  color: #86efac;
}

.schedule-cell.evening {
  background: rgba(245, 158, 11, 0.1);
  color: #fde047;
}

.schedule-cell.night {
  background: rgba(59, 130, 246, 0.1);
  color: #93c5fd;
}

.schedule-cell.off {
  background: rgba(148, 163, 184, 0.05);
  color: #94a3b8;
}
</style>
