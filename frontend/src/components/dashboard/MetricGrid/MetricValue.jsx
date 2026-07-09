function MetricValue({
    value,
    unit
}){
    return(
        <div className="metric-value-group">
            <span className="metric-value">
                {value}
            </span>
            <span className="metric-unit">
                {unit}
            </span>
        </div>
    );
}

export default MetricValue;