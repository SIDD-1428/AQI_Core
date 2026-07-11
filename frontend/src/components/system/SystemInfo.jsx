import "../../styles/system.css";
function SystemInfo({status}){
    return(
        <div className="system-info-card">
            <h2 className="system-section-title">
                System Information
            </h2>
            <div className="system-info-grid">
                <div className="info-item">
                    <span className="info-label">Version</span>
                    <span className="info-value">{status.version}</span>
                </div>

                <div className="info-item">
                    <span className="info-label">Refresh Rate</span>
                    <span className="info-value">5 seconds</span>
                </div>

                <div className="info-item">
                    <span className="info-label">API status</span>
                    <span className="info-value" style={{color:"#43D17C"}}>Healthy</span>
                </div>

                <div className="info-item">
                    <span className="info-label">Node Count</span>
                    <span className="info-value">1</span>
                </div>
            </div>
        </div>
    );
}

export default SystemInfo;