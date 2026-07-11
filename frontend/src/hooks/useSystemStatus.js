import { useEffect, useState } from "react";
import { getSystemStatus } from "../api/aqiApi";

function useSystemStatus() {

    const [status, setStatus] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {

        async function loadStatus() {

            try {

                const data = await getSystemStatus();

                setStatus(data);
                setError(null);

            } catch (err) {

                setError(err);

            } finally {

                setLoading(false);

            }

        }

        loadStatus();

        const interval = setInterval(loadStatus, 5000);

        return () => clearInterval(interval);

    }, []);

    return {
        status,
        loading,
        error,
    };

}

export default useSystemStatus;