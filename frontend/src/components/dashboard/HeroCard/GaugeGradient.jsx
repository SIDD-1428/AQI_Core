import { GAUGE } from "../../../constants/gaugeConfig";

function polarToCartesian(cx, cy, radius, angle) {
  const radians = (angle - 90) * Math.PI / 180;

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

function GaugeGradient() {

  return (
    <>
      <defs>

        <linearGradient
          id="gaugeGradient"
          x1="0%"
          y1="0%"
          x2="100%"
          y2="0%"
        >

          <stop
            offset="0%"
            stopColor="#35E17A"
          />

          <stop
            offset="30%"
            stopColor="#9FE870"
          />

          <stop
            offset="55%"
            stopColor="#FFD94A"
          />

          <stop
            offset="78%"
            stopColor="#FF9A3D"
          />

          <stop
            offset="100%"
            stopColor="#FF4A4A"
          />

        </linearGradient>

      </defs>

      <path
        d={describeArc(
          GAUGE.START_ANGLE,
          GAUGE.END_ANGLE
        )}
        fill="none"
        stroke="url(#gaugeGradient)"
        strokeWidth={GAUGE.STROKE_WIDTH}
        strokeLinecap="round"
      />
    </>
  );

}

export default GaugeGradient;