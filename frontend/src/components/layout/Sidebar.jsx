import { useState } from "react";
import Logo from "./Logo"
import NavItem from "./NavItem";
import {NAV_ITEMS} from "../../data/navigation";
import "../../styles/sidebar.css"

function Sidebar({
  activePage,
  onSelectPage,
  liveMonitoringExpanded,
}){
  const [expanded,setExpanded]=useState(false);
  return(
    <aside className={`sidebar ${expanded ?"sidebar-expanded":""}`}
    onMouseEnter={()=>setExpanded(true)}
    onMouseLeave={()=>setExpanded(false)}>
      <Logo expanded={expanded}/>
      <nav className="sidebar-nav">
        {NAV_ITEMS.map((item)=>(
          <NavItem
          key={item.id}
          item={item}
          expanded={expanded}
          activePage={activePage}
          onSelectPage={onSelectPage}
          />
        ))}
      </nav>
    </aside>
  );
}

export default Sidebar;