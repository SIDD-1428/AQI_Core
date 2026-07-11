import "../../styles/system.css";
function HealthSummary({status}){
    const backendHealthy=status.status==="online";
    const databaseHealthy=status.database==="connected";
    const health=(Number(backendHealthy)+Number(databaseHealthy))/2*100;

    return(
        <div className="health-summary-card">
            <div className="health-header">
                <h2 className="system-section-title">Overall System Health</h2>
                <span className="health-score">{health}%</span>
            </div>

            <div className="health-bar">
                <div className="health-fill" style={{width:`${health}%`}}></div>
            </div>
            <p className="health-message">
                    {health===100?"All monitored services are operating normally.":"One or more services require attention."}
                </p>
        </div>
    );
}
export default HealthSummary;