import { GAUGE } from "../../../constants/gaugeConfig";

function GaugePointer({ value }) {

  const angle =
    GAUGE.START_ANGLE +
    (value / GAUGE.MAX_VALUE) *
      (GAUGE.END_ANGLE - GAUGE.START_ANGLE);

  return (
    <g
      transform={`
        rotate(
          ${angle}
          ${GAUGE.CENTER}
          ${GAUGE.CENTER}
        )
      `}
      style={{
        transition: "transform .5s ease",
      }}
    >

      {/* Soft Glow */}
      <circle
        cx={GAUGE.CENTER}
        cy={GAUGE.CENTER - GAUGE.RADIUS + 6}
        r="25"
        fill="rgba(255,255,255,.18)"
      />

      {/* Pointer */}
      <path
        d={`
          M ${GAUGE.CENTER} ${GAUGE.CENTER - GAUGE.RADIUS - 8}
          L ${GAUGE.CENTER - 8} ${GAUGE.CENTER - GAUGE.RADIUS + 12}
          L ${GAUGE.CENTER + 8} ${GAUGE.CENTER - GAUGE.RADIUS + 12}
          Z
        `}
        fill="#012515"
      />

    </g>
  );
}

export default GaugePointer;