import MetricCard from  "./MetricCard";
import useLatestPacket from "../../../hooks/useLatestPacket";

import "../../../styles/metricGrid.css";

function MetricGrid(){
const{
    packet,loading,error,
}=useLatestPacket();

if(loading){
    return(
        <div className="metric-grid">
            Loading..
        </div>
    );
}

if(error){
    return(
        <div className="metric-grid">
            Failed to load data.
        </div>
    );
}
const metrics = [
  {
    title: "PM2.5",
    value: packet.pm2_5,
    unit: "µg/m³",
    status: "Normal",
    color: "#43D17C",
    icon: "pm25",
  },
  {
    title: "PM10",
    value: packet.pm10,
    unit: "µg/m³",
    status: "Normal",
    color: "#45B5FF",
    icon: "pm10",
  },
  {
    title: "CO",
    value: packet.co,
    unit: "ppm",
    status: "Normal",
    color: "#F4C542",
    icon: "co",
  },
  {
    title: "Temperature",
    value: packet.temperature,
    unit: "°C",
    status: "Normal",
    color: "#FF8452",
    icon: "temp",
  },
];
return (
    
  <div className="metric-grid">

   {metrics.map((metric)=>(
    <MetricCard
        key={metric.title}
        title={metric.title}
        {...metric}
        />
   ))}

  </div>

);

}

export default MetricGrid;