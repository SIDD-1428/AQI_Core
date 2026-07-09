import { useState } from "react";

import Sidebar from "./components/layout/Sidebar";
import Topbar from "./components/layout/Topbar";
import HeroCard from "./components/dashboard/HeroCard/HeroCard";

import { MOCK_NODES } from "./data/mockNodes";
import { MOCK_AQI_LATEST } from "./data/mockAqi";

import "./styles/global.css";
import MetricGrid from "./components/dashboard/MetricGrid/MetricGrid";

function App() {
  // Currently active page
  const [activePage, setActivePage] = useState("dashboard");

  // Selected LoRa node
  const [selectedNode, setSelectedNode] = useState(MOCK_NODES[0].id);

  // Dashboard theme
  const [theme, setTheme] = useState("dark");

  function toggleTheme() {
    setTheme((currentTheme) =>
      currentTheme === "dark" ? "light" : "dark"
    );
  }

  return (
    <div className="app-shell">

      <Sidebar
        activePage={activePage}
        onSelectPage={setActivePage}
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
            aqi={MOCK_AQI_LATEST.aqi}
            dominantPollutant={MOCK_AQI_LATEST.dominantPollutant}
            updatedAt={MOCK_AQI_LATEST.updatedAt}
          />

          <MetricGrid/>

        </main>

      </div>

    </div>
  );
}

export default App;