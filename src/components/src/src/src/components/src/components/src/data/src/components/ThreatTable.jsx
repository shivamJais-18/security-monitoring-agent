import { threats } from "../data/threats";

export default function ThreatTable() {
  return (
    <div style={styles.container}>
      <h3>🚨 Detected Threats</h3>
      <table style={styles.table}>
        <thead>
          <tr><th>IP</th><th>Type</th><th>Severity</th></tr>
        </thead>
        <tbody>
          {threats.map((t, i) => (
            <tr key={i}>
              <td>{t.ip}</td>
              <td>{t.type}</td>
              <td>{t.level}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const styles = {
  container: { padding: "0 32px 24px" },
  table: { width: "100%", borderCollapse: "collapse" }
};
