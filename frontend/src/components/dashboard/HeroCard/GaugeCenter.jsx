import {getAqiCategory} from "../../../utils/aqiCategory";

function GaugeCenter({value}){
    const category=getAqiCategory(value);
    return(
        <g>
            <text
            x="120"
            y="125"
            textAnchor="middle"
            className="gauge-value-text">
                {Math.round(value)}
            </text>

            <text 
            x="120"
            y="140"
            textAnchor="middle"
            className="gauge-label-text">
            AQI
            </text>

            <text 
            x="120"
            y="158"
            textAnchor="middle"
            fill={category.color}
            className="gauge-category-text">
                {category.label}
            </text>
        </g>
    );
}

export default GaugeCenter;