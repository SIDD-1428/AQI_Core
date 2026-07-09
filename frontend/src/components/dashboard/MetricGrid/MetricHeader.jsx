import MetricIcon from "./MetricIcon";
function MetricHeader({
    title,
    icon,
    color,
}){
    return(
        <div className="metric-header">
            <MetricIcon
            name={icon}
            color={color}
            />

            <span className="metric-title">
                {title}
            </span>
        </div>
    );
}

export default MetricHeader;