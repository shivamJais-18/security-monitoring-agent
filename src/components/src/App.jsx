import FrontHead from "./components/FrontHead";
import Navbar from "./components/Navbar";
import KPICards from "./components/KPICards";
import ThreatTable from "./components/ThreatTable";
import IncidentTable from "./components/IncidentTable";

export default function App() {
  return (
    <>
      <FrontHead />
      <Navbar />
      <KPICards />
      <ThreatTable />
      <IncidentTable />
    </>
  );
}
