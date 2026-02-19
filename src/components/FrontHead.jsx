export default function FrontHead() {
  return (
    <div style={styles.container}>
      <div>
        <h1 style={styles.title}>🛡️ Security Monitoring Platform</h1>
        <p style={styles.subtitle}>
          AI-Powered Threat Detection & Automated Response
        </p>
      </div>
      <div style={styles.right}>
        <span style={styles.status}>● SYSTEM ONLINE</span>
        <p>Log Compression: <b>90%</b></p>
        <p>MTTD Reduction: <b>60%</b></p>
      </div>
    </div>
  );
}

const styles = {
  container: {
    padding: "20px 32px",
    display: "flex",
    justifyContent: "space-between",
    background: "linear-gradient(135deg,#020617,#0f172a)",
    borderBottom: "1px solid #1e293b"
  },
  title: { margin: 0 },
  subtitle: { color: "#94a3b8" },
  right: { textAlign: "right" },
  status: { color: "#22c55e", fontWeight: "bold" }
};
