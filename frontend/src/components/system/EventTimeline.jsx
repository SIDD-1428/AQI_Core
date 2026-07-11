import {
    CheckCircle2,
    Database,
    Server,
    Activity,
    WifiOff,
} from "lucide-react";

import "../../styles/system.css";

function EventTimeline({ status }) {

    const formatTime = (time) => {
        if (!time) return "--";

        return new Date(time).toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit",
        });
    };

    const backendOnline = status.status === "online";

    const events = [

        {
            icon: backendOnline
                ? <Server size={18} />
                : <WifiOff size={18} />,
            title: "Gateway Status",
            message: backendOnline
                ? "Gateway is receiving packets."
                : "No packets received recently.",
            time: formatTime(status.last_packet),
            color: backendOnline ? "#43D17C" : "#FF5C5C",
        },

        {
            icon: <Database size={18} />,
            title: "Database",
            message: `${status.database.toUpperCase()} • ${status.packets} packets stored`,
            time: formatTime(status.last_packet),
            color: "#45B5FF",
        },

        {
            icon: <Activity size={18} />,
            title: "Latest Packet",
            message: `Node AQI001 • ${status.packets} packets processed`,
            time: formatTime(status.last_packet),
            color: "#F4C542",
        },

        {
            icon: <CheckCircle2 size={18} />,
            title: "AQI Engine",
            message: `${status.aqi_records} AQI calculations completed`,
            time: formatTime(status.last_aqi),
            color: "#8C7CFF",
        },

    ];

    return (

        <div className="timeline-card">

            <h2 className="system-section-title">
                Recent System Events
            </h2>

            <div className="timeline">

                {events.map((event, index) => (

                    <div
                        key={index}
                        className="timeline-item"
                    >

                        <div
                            className="timeline-icon"
                            style={{
                                color: event.color,
                            }}
                        >
                            {event.icon}
                        </div>

                        <div className="timeline-content">

                            <div className="timeline-title">
                                {event.title}
                            </div>

                            <div className="timeline-message">
                                {event.message}
                            </div>

                            <div className="timeline-time">
                                {event.time}
                            </div>

                        </div>

                    </div>

                ))}

            </div>

        </div>

    );

}

export default EventTimeline;