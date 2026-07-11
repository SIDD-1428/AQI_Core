
import StatusGrid from "../components/system/StatusGrid";
import HealthSummary from "../components/system/HealthSummary";
import SystemInfo from "../components/system/SystemInfo";
import EventTimeline from "../components/system/EventTimeline";
import { useDashboard } from "../context/DashboardContext";

function SystemStatus(){
    const{
        system,
        loading,
        error,
    }=useDashboard();
    if(loading){
        return <div>Loading System Status..</div>;
    }
    if(error){
        return <div>Failed to load system status</div>;
    }
    return(
        <div className="system-status-page">
            <StatusGrid status={system}/>
            <SystemInfo status={system}/>
            <HealthSummary status={system}/>
            <EventTimeline status={system}/>
        </div>
    );
}

export default SystemStatus;
