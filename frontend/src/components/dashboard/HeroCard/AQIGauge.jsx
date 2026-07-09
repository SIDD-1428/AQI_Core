import "../../../styles/gauge.css";
import { GAUGE } from "../../../constants/gaugeConfig";
import { AQI_RANGES } from "../../../constants/aqiRanges";
import GaugeArc from "./GaugeArc";
import GaugeSegment from "./GaugeSegment";
import GaugeCenter from "./GaugeCenter";
import GaugeNeedle from "./GaugeNeedle";

function AQIGauge({ value }) {
  const totalAngle = GAUGE.END_ANGLE - GAUGE.START_ANGLE;
  return (
    <div className="gauge">
      <svg
        width={GAUGE.SIZE}
        height={GAUGE.SIZE}
        viewBox={`0 0 ${GAUGE.SIZE} ${GAUGE.SIZE}`}
      >
        {/* Background Arc */}
        <GaugeArc />

        {/* AQI Range Segments */}
        {AQI_RANGES.map((range) => {

          const startAngle = GAUGE.START_ANGLE +
            (range.min / GAUGE.MAX_VALUE) *
            totalAngle;

          const endAngle = GAUGE.START_ANGLE +
            (range.max / GAUGE.MAX_VALUE) *
            totalAngle;

          return (
            <GaugeSegment
              key={range.label}
              startAngle={startAngle}
              endAngle={endAngle}
              color={range.color}
            />
          );

        })}
        {/*pointer*/}
        <GaugeNeedle value={value}/>
        {/* Center Text */}
        <GaugeCenter value={value}/>
      </svg>
    </div>
  );
}

export default AQIGauge;