import { GAUGE } from "../../../constants/gaugeConfig";

function polarToCartesian(cx, cy, radius, angle) {
  const radians = ((angle - 90) * Math.PI) / 180;

  return {
    x: cx + radius * Math.cos(radians),
    y: cy + radius * Math.sin(radians),
  };
}

function describeArc(startAngle, endAngle) {
  const start = polarToCartesian(
    GAUGE.CENTER,
    GAUGE.CENTER,
    GAUGE.RADIUS,
    endAngle
  );

  const end = polarToCartesian(
    GAUGE.CENTER,
    GAUGE.CENTER,
    GAUGE.RADIUS,
    startAngle
  );

  const largeArcFlag =
    endAngle - startAngle <= 180 ? 0 : 1;

  return [
    "M",
    start.x,
    start.y,

    "A",
    GAUGE.RADIUS,
    GAUGE.RADIUS,
    0,
    largeArcFlag,
    0,

    end.x,
    end.y,
  ].join(" ");
}

function GaugeArc() {
  return (
    <path
      d={describeArc(
        GAUGE.START_ANGLE,
        GAUGE.END_ANGLE
      )}
      fill="none"
      stroke="rgba(255,255,255,0.08)"
      strokeWidth={GAUGE.STROKE_WIDTH}
      strokeLinecap="round"
    />
  );
}

export default GaugeArc;