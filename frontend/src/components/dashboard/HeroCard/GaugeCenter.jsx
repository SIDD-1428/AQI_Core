import { GAUGE } from "../../../constants/gaugeConfig";

function GaugeCenter({ value }) {
  return (
    <g>

      <text
        x={GAUGE.CENTER}
        y={GAUGE.CENTER + 19}
        textAnchor="middle"
        className="gauge-value-text"
      >
        {Math.round(value)}
      </text>
      <text className="gauge-label-text"
       x={GAUGE.CENTER}
        y={GAUGE.CENTER + 45}
        textAnchor="middle">
        AQI Index
      </text>
    
    </g>
  );
}

export default GaugeCenter;