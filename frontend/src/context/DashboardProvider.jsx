import { useEffect, useState } from "react";

import DashboardContext from "./DashboardContext";

import {
    getSystemStatus,
    getLatestAQI,
    getLatestPacket,
    getNodeSummary,
} from "../api/aqiApi";

function DashboardProvider({ children }) {

    const [system, setSystem] = useState(null);
    const [aqi, setAQI] = useState(null);
    const[packet,setPacket]=useState(null);
    const[nodes,setNodes]=useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    async function refreshDashboard() {
        try {
            const [
                systemData,
                aqiData,
                packetData,
                nodeData
            ] = await Promise.all([
                getSystemStatus(),
                getLatestAQI(),
                getLatestPacket(),
                getNodeSummary(),
            ]);

            setSystem(systemData);
            setAQI(aqiData);
            setPacket(packetData);
            setNodes(nodeData.nodes);
            setError(null);

        } catch (err) {

            setError(err);

        } finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        refreshDashboard();

        const interval = setInterval(refreshDashboard, 5000);

        return () => clearInterval(interval);

    }, []);

    return (

        <DashboardContext.Provider
            value={{
                system,
                aqi,
                packet,
                nodes,
                loading,
                error,
            }}
        >

            {children}

        </DashboardContext.Provider>

    );

}

export default DashboardProvider;