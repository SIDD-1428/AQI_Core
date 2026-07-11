import { useEffect, useState } from "react";

import DashboardContext from "./DashboardContext";

import {
    getSystemStatus,
    getLatestAQI,
    getLatestPacket,
} from "../api/aqiApi";

function DashboardProvider({ children }) {

    const [system, setSystem] = useState(null);
    const [aqi, setAQI] = useState(null);
    const[packet,setPacket]=useState(null);

    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    async function refreshDashboard() {
        try {
            const [
                systemData,
                aqiData,
                packetData,
            ] = await Promise.all([
                getSystemStatus(),
                getLatestAQI(),
                getLatestPacket(),

            ]);

            setSystem(systemData);
            setAQI(aqiData);
            setPacket(packetData);

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
                loading,
                error,
            }}
        >

            {children}

        </DashboardContext.Provider>

    );

}

export default DashboardProvider;