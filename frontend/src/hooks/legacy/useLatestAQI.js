import { useEffect, useState } from "react";
import { getLatestAQI } from "../../api/aqiApi";

function useLatestAQI() {
    const [aqiData, setAqiData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {

        async function loadAQI() {
            try {
                const data = await getLatestAQI();
                setAqiData(data);
                setError(null);
            } catch (err) {
                setError(err);
            } finally {
                setLoading(false);
            }
        }

        // Initial fetch
        loadAQI();

        //5 seconds
        const interval = setInterval(loadAQI, 5000);

        return () => clearInterval(interval);

    }, []);

    return {
        aqiData,
        loading,
        error,
    };
}

export default useLatestAQI;