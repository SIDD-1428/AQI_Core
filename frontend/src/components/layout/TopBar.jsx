import "../../styles/topbar.css";

import NodeSelector from "./NodeSelector";
import Clock from "./Clock";
import ThemeToggle from "./ThemeToggle";


function Topbar({
  nodes,
  selectedNode,
  onSelectNode,
  theme,
  onToggleTheme,
}){
  return(
    <header className="topbar">
      <div className="topbar-title">
        KJU AirX
      </div>
      <div className="topbar-actions">
        <NodeSelector
        nodes={nodes}
        selectedNode={selectedNode}
        onSelectNode={onSelectNode}/>

        <Clock/>
        <ThemeToggle
        theme={theme}
        onToggleTheme={onToggleTheme}
        />
      </div>
    </header>
  );
}

export default Topbar;