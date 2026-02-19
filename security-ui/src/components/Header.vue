<template>
  <div class="header">
    <div class="header-left">
      <h2>Security Dashboard</h2>
      <p class="subtitle">Real-time threat monitoring and incident response</p>
    </div>

    <div class="header-center">
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" placeholder="Search threats, systems, logs..." @input="search" />
      </div>
    </div>

    <div class="header-right">
      <div class="notification-bell">
        <span class="bell">🔔</span>
        <span class="badge">1</span>
      </div>
      <button class="settings-btn">⚙️</button>
      <div class="user-profile">
        <div class="avatar">👤</div>
        <span class="user-name">SOC Analyst</span>
      </div>
    </div>
  </div>
</template>

<script setup>
const search = (e) => {
  console.log('Search:', e.target.value)
}
</script>

<style scoped>
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 2rem;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1);
  background: linear-gradient(90deg, rgba(15, 23, 42, 0.8) 0%, rgba(30, 41, 59, 0.8) 100%);
  backdrop-filter: blur(10px);
}

.header-left h2 {
  margin: 0 0 0.25rem 0;
  font-size: 1.75rem;
  color: #e2e8f0;
}

.subtitle {
  margin: 0;
  font-size: 0.875rem;
  color: #94a3b8;
}

.header-center {
  flex: 1;
  margin: 0 2rem;
}

.search-box {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: rgba(148, 163, 184, 0.1);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 0.5rem;
  padding: 0.5rem 1rem;
  transition: all 0.3s ease;
}

.search-box:focus-within {
  background: rgba(59, 130, 246, 0.1);
  border-color: rgba(59, 130, 246, 0.3);
}

.search-icon {
  font-size: 1.1rem;
  color: #94a3b8;
}

.search-box input {
  background: none;
  border: none;
  outline: none;
  color: #e2e8f0;
  font-size: 0.95rem;
  width: 100%;
}

.search-box input::placeholder {
  color: #64748b;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.notification-bell {
  position: relative;
  cursor: pointer;
  font-size: 1.5rem;
}

.notification-bell .badge {
  position: absolute;
  top: -8px;
  right: -8px;
  background: #ef4444;
  color: white;
  border-radius: 9999px;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 600;
}

.settings-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #cbd5e1;
  transition: all 0.3s ease;
}

.settings-btn:hover {
  color: #60a5fa;
  transform: rotate(20deg);
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 1rem;
  background: rgba(59, 130, 246, 0.1);
  border: 1px solid rgba(59, 130, 246, 0.2);
  border-radius: 0.5rem;
  cursor: pointer;
}

.avatar {
  font-size: 1.25rem;
}

.user-name {
  color: #cbd5e1;
  font-size: 0.875rem;
}
</style>
