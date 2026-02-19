import { incidents } from "../data/incidents";

export default function IncidentTable() {
  return (
    <div style={{ padding: "0 32px 40px" }}>
      <h3>🧾 Incident Responses</h3>
      <table style={{ width: "100%" }}>
        <thead>
          <tr><th>ID</th><th>Severity</th><th>Action</th></tr>
        </thead>
        <tbody>
          {incidents.map((i, idx) => (
            <tr key={idx}>
              <td>{i.id}</td>
              <td>{i.severity}</td>
              <td>{i.action}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
