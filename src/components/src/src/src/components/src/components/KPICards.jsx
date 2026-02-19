export default function KPICards() {
  return (
    <div style={styles.grid}>
      {[
        ["Total Threats", 128],
        ["Critical Threats", 21],
        ["Intel Confirmed", 18],
        ["Automated Responses", 34]
      ].map(([title, value]) => (
        <div key={title} style={styles.card}>
          <p>{title}</p>
          <h2>{value}</h2>
        </div>
      ))}
    </div>
  );
}

const styles = {
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(4,1fr)",
    gap: "16px",
    padding: "24px 32px"
  },
  card: {
    background: "#020617",
    border: "1px solid #1e293b",
    borderRadius: "10px",
    padding: "20px"
  }
};
