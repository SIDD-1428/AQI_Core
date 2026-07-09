import "../../../styles/gauge.css";
import { GAUGE } from "../../../constants/gaugeConfig";
import { AQI_RANGES } from "../../../constants/aqiRanges";
import GaugeArc from "./GaugeArc";
import GaugeCenter from "./GaugeCenter";
import GaugePointer from "./GaugePointer";
import GaugeGradient from "./GaugeGradient";

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
        <GaugeGradient/>
        {/*pointer*/}
        <GaugePointer value={value}/>
        {/* Center Text */}
        <GaugeCenter value={value}/>
      </svg>
    </div>
  );
}

export default AQIGauge;