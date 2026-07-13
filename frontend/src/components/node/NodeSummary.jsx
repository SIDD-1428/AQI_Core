import {
    Server,
    Wifi,
    WifiOff,
    Radio,
} from "lucide-react";

import "../../styles/node.css";

function NodeSummary({ nodes }) {

    const totalNodes = nodes.length;

    const onlineNodes = nodes.filter(
        (node) => node.status === "online"
    ).length;

    const offlineNodes = totalNodes - onlineNodes;

    const averageRSSI =
        totalNodes > 0
            ? (
                  nodes.reduce(
                      (sum, node) => sum + node.rssi,
                      0
                  ) / totalNodes
              ).toFixed(0)
            : "--";

    const cards = [
        {
            title: "Total Nodes",
            value: totalNodes,
            icon: <Server size={24} />,
            color: "#45B5FF",
        },
        {
            title: "Online",
            value: onlineNodes,
            icon: <Wifi size={24} />,
            color: "#43D17C",
        },
        {
            title: "Offline",
            value: offlineNodes,
            icon: <WifiOff size={24} />,
            color: "#FF5F6D",
        },
        {
            title: "Average RSSI",
            value:
                averageRSSI === "--"
                    ? "--"
                    : `${averageRSSI} dBm`,
            icon: <Radio size={24} />,
            color: "#F4C542",
        },
    ];

    return (

        <div className="node-summary-grid">

            {cards.map((card) => (

                <div
                    key={card.title}
                    className="node-summary-card"
                >

                    <div
                        className="node-summary-icon"
                        style={{
                            color: card.color,
                        }}
                    >
                        {card.icon}
                    </div>

                    <div className="node-summary-content">

                        <div className="node-summary-value">
                            {card.value}
                        </div>

                        <div className="node-summary-title">
                            {card.title}
                        </div>

                    </div>

                </div>

            ))}

        </div>

    );

}

export default NodeSummary;