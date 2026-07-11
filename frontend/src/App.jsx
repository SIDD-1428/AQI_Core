import { useState } from "react";

import Sidebar from "./components/layout/Sidebar";
import Topbar from "./components/layout/Topbar";
import HeroCard from "./components/dashboard/HeroCard/HeroCard";
import TrendChart from "./components/dashboard/TrendChart/TrendChart";
import { MOCK_NODES } from "./data/mockNodes";
import LiveMonitoring from "./components/dashboard/LiveMonitoring/LiveMonitoring";
import useLatestAQI from "./hooks/useLatestAQI";
import "./styles/global.css";
import MetricGrid from "./components/dashboard/MetricGrid/MetricGrid";

function App() {
  // Currently active page
  const [activePage, setActivePage] = useState("dashboard");

  // Selected LoRa node
  const [selectedNode, setSelectedNode] = useState(MOCK_NODES[0].id);

  // Dashboard theme
  const [theme, setTheme] = useState("dark");
  //state sharing by livemonitoring
  const [liveMonitoringExpanded,setLiveMonitoringExpanded]=useState(false);

  //live data pull
  const{aqiData,loading,error}=useLatestAQI();
  if(loading){
    return <div>Loading...</div>
  }
  if(error){
    return <div>Failed to load AQI.</div>
  }
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

          <HeroCard
              aqi={aqiData.aqi}
              dominantPollutant={aqiData.dominant_pollutant}
              updatedAt={Date.now()}
          />
          <LiveMonitoring
          expanded={liveMonitoringExpanded}
          onToggle={handleLiveMonitoringToggle}
          />
          <TrendChart/>
        </main>

      </div>

    </div>
  );
}

export default App;