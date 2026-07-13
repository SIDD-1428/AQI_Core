import { useState } from "react";

import Sidebar from "./components/layout/Sidebar";
import Topbar from "./components/layout/Topbar";
import HeroCard from "./components/dashboard/HeroCard/HeroCard";
import TrendChart from "./components/dashboard/TrendChart/TrendChart";
import { MOCK_NODES } from "./data/mockNodes";
import LiveMonitoring from "./components/dashboard/LiveMonitoring/LiveMonitoring";
import "./styles/global.css";
import MetricGrid from "./components/dashboard/MetricGrid/MetricGrid";
import SystemStatus from"./pages/SystemStatus";
import { useDashboard } from "./context/DashboardContext";
import Nodes from "./pages/Nodes";
function App() {
  
  // Currently active page
  const [activePage, setActivePage] = useState("dashboard");

  // Selected LoRa node
  const [selectedNode, setSelectedNode] = useState(MOCK_NODES[0].id);

  // Dashboard theme
  const [theme, setTheme] = useState("dark");
  //state sharing by livemonitoring
  const [liveMonitoringExpanded,setLiveMonitoringExpanded]=useState(false);

  //dashboardprovider
  const{
    aqi,system,loading,error,}=useDashboard();
  
  function toggleTheme() {
    setTheme((currentTheme) =>
      currentTheme === "dark" ? "light" : "dark"
    );
  }
  function handlePageChange(page){
    setActivePage(page);
    if(page==="live"){
      setLiveMonitoringExpanded(true);
    }else{
      setLiveMonitoringExpanded(false);
    }
  }
  function handleLiveMonitoringToggle() {

  if (liveMonitoringExpanded) {
    setLiveMonitoringExpanded(false);
    setActivePage("dashboard");
  } else {
    setLiveMonitoringExpanded(true);
    setActivePage("live");
  }

}
console.log("Current Page: ",activePage)
  return (
    <div className="app-shell">

      <Sidebar
        activePage={activePage}
        onSelectPage={handlePageChange}
      />

      <div className="app-content">

        <Topbar
          nodes={MOCK_NODES}
          selectedNode={selectedNode}
          onSelectNode={setSelectedNode}
          theme={theme}
          onToggleTheme={toggleTheme}
        />

        <main className="page-content">

            {(activePage === "dashboard"|| activePage==="live") && (
              <>
                <HeroCard
                  aqi={aqi?.aqi}
                  dominantPollutant={aqi?.dominant_pollutant}
                  updatedAt={Date.now()}
                />

                <LiveMonitoring
                  expanded={liveMonitoringExpanded}
                  onToggle={handleLiveMonitoringToggle}
                />

                <TrendChart />
              </>
            )}


            {activePage === "system-status" && (
              <SystemStatus />
            )}

            {activePage==="nodes"&&(
              <Nodes/>
            )}

          </main>
      </div>

    </div>
  );
}

export default App;