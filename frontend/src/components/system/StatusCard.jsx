import "../../styles/system.css";

function StatusCard({
    title,
    icon,
    value,
    color="#43D17C",
}){
    return(
        <div className="status-card">
            <div className="status-icon" style={{color}}>
                {icon}
            </div>
            <div className="status-title">
                {title}
            </div>
            <div className="status-value" style={{color}}>
                {value}
            </div>
        </div>
    );
}
export default StatusCard;