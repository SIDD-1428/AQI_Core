function MetricStatus({
    status,
    color,
}){
    return(
        <div className="metric-status">
            <span className="metric-status-dot" style={{background:color,}}></span>
            <span className="metric-status-text">
                {status}
            </span>
        </div>
    );
}

export default MetricStatus;