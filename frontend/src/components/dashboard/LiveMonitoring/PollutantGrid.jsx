import MetricCard from "../MetricGrid/MetricCard";

function PollutantGrid({ metrics }) {
  return (
    <div className="pollutant-grid">
      {metrics.map((metric, index) => (
        <MetricCard
          key={metric.title}
          title={metric.title}
          value={metric.value}
          unit={metric.unit}
          status={metric.status || "Normal"}
          color={metric.color}
          icon={metric.icon}
          index={index}
        />
      ))}
    </div>
  );
}

export default PollutantGrid;