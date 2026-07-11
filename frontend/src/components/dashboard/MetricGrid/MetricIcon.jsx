import {
    Wind,
    Cloud,
    Flame,
    Thermometer,
    Droplets,
    Gauge,
    Radio,
    CircleDot,
} from "lucide-react";

function MetricIcon({ name, color }) {

    const icons = {

        pm25: Wind,

        pm10: Cloud,

        co: Flame,

        temp: Thermometer,

        humidity: Droplets,

        pressure: Gauge,

        no2: CircleDot,

        so2: CircleDot,

        nh3: CircleDot,

        o3: CircleDot,

        signal: Radio,

    };

    // Fallback if an icon name isn't found
    const Icon = icons[name] || CircleDot;

    return (
        <Icon
            size={22}
            color={color}
        />
    );
}

export default MetricIcon;