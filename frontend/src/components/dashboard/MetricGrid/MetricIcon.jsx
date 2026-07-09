import{
    Wind,Cloud,Flame,Thermometer
} from "lucide-react";

function MetricIcon({name,color}){
    const icons={
        pm25: Wind,
        pm10: Cloud,
        co:Flame,
        temp:Thermometer,
    };

    const Icon=icons[name];

    return(<Icon size={22} color={color}/>);
}

export default MetricIcon;