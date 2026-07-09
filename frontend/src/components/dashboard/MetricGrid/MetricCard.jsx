import "../../../styles/metricCard.css";

import MetricHeader from "./MetricHeader";
import MetricValue from "./MetricValue";
import MetricStatus from "./MetricStatus";

function MetricCard({
  title,
  value,
  unit,
  status,
  color,
  icon,
}) {

  return (
    <div className="metric-card">
      <MetricHeader
        title={title}
        icon={icon}
        color={color}
      />

      <MetricValue
        value={value}
        unit={unit}
      />

      <MetricStatus
        status={status}
        color={color}
      />
    </div>
  );
}

export default MetricCard;