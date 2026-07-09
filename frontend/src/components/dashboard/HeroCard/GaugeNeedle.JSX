import {GAUGE} from "../../../constants/gaugeConfig";

function GaugeNeedle({value}){
    const angle=GAUGE.START_ANGLE+(value/GAUGE.MAX_VALUE)*(GAUGE.END_ANGLE-GAUGE.START_ANGLE);

    return(
        <g
            transform={`
            rotate(${angle}
            ${GAUGE.CENTER}
            ${GAUGE.CENTER}
            )
            `}
        >
            {/*NEEDLE*/}
            <line 
            x1={GAUGE.CENTER}
            y1={GAUGE.CENTER}
            x2={GAUGE.CENTER}
            y2={GAUGE.CENTER - GAUGE.RADIUS+18}
            stroke="#F4FBF8"
            strokeWidth="4"
            strokeLinecap="round"/>

            {/*needle hub*/}
            <circle
            cx={GAUGE.CENTER}
            cy={GAUGE.CENTER}
            r="7"
            fill="#F4FBF8"
            />
        </g>
    );
}

export default GaugeNeedle;