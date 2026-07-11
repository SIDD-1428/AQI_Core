import { useState } from "react";

import PollutantGrid from "./PollutantGrid";
import ExpandButton from "./ExpandButton";

import useLatestPacket from "../../../hooks/useLatestPacket";

import "../../../styles/monitoring.css";

function LiveMonitoring({
    expanded,
    onToggle,
}) {

    const { packet, loading, error } = useLatestPacket();


    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Failed to load live data.</div>;
    }

    const priorityMetrics = [
        {
            title: "PM2.5",
            value: packet.pm2_5,
            unit: "µg/m³",
            status: "Normal",
            icon: "pm25",
            color: "#43D17C",
        },
        {
            title: "PM10",
            value: packet.pm10,
            unit: "µg/m³",
            status: "Normal",
            icon: "pm10",
            color: "#45B5FF",
        },
        {
            title: "CO",
            value: packet.co,
            unit: "ppm",
            status: "Normal",
            icon: "co",
            color: "#F4C542",
        },
        {
            title: "Temperature",
            value: packet.temperature,
            unit: "°C",
            status: "Normal",
            icon: "temp",
            color: "#FF8452",
        },
    ];

    const extraMetrics = [
        {
            title: "Humidity",
            value: packet.humidity,
            unit: "%",
            icon: "humidity",
            color: "#49A8FF",
        },
        {
            title: "Pressure",
            value: packet.pressure,
            unit: "hPa",
            icon: "pressure",
            color: "#8C7CFF",
        },
        {
            title: "NO₂",
            value: packet.no2,
            unit: "ppm",
            icon: "no2",
            color: "#F57C7C",
        },
        {
            title: "SO₂",
            value: packet.so2,
            unit: "ppm",
            icon: "so2",
            color: "#FFB84D",
        },
        {
            title: "NH₃",
            value: packet.nh3,
            unit: "ppm",
            icon: "nh3",
            color: "#00C8A5",
        },
        {
            title: "O₃",
            value: packet.o3,
            unit: "ppm",
            icon: "o3",
            color: "#73D13D",
        },
    ];

    return (

        <section className="live-monitoring">

        <div className="monitoring-header">
        <div className="monitoring-title">
            <span className="live-dot"></span>
            <h2>Live Monitoring</h2>
        </div>
        <p> Real-time environmental metrics</p>
    </div>

    <PollutantGrid
        metrics={priorityMetrics}
    />

    <div className="monitoring-divider" />

    <div
        className={
            expanded
            ? "extra-metrics expanded"
            : "extra-metrics"
        }
    >
        <PollutantGrid
            metrics={extraMetrics}
        />
    </div>
        <ExpandButton
        expanded={expanded}
        onClick={onToggle}
    />
</section>

    );

}

export default LiveMonitoring;