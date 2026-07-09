import "../../../styles/trendChart.css";

import TrendHeader from "./TrendHeader";
import TrendGraph from "./TrendGraph";
import TrendLegend from "./TrendLegend";

function TrendChart(){
    return(
        <div className="trend-card">
            <TrendHeader/>
            <TrendGraph/>
            <TrendLegend/>
        </div>
    );
}

export default TrendChart;