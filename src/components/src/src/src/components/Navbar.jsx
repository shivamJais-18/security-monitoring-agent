export default function Navbar() {
  return (
    <div style={styles.nav}>
      <span>Overview</span>
      <span>Threats</span>
      <span>Incidents</span>
      <span>Analytics</span>
    </div>
  );
}

const styles = {
  nav: {
    display: "flex",
    gap: "30px",
    padding: "12px 32px",
    background: "#020617",
    borderBottom: "1px solid #1e293b",
    color: "#cbd5f5",
    fontSize: "14px"
  }
};
