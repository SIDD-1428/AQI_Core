import { useEffect, useState } from "react";
import { getLatestPacket } from "../../api/aqiApi";

function useLatestPacket() {

    const [packet, setPacket] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {

        async function loadPacket() {

            try {

                const data = await getLatestPacket();

                setPacket(data);
                setError(null);

            } catch (err) {

                setError(err);

            } finally {

                setLoading(false);

            }

        }

        // Initial fetch
        loadPacket();

        const interval = setInterval(loadPacket, 5000);

        return () => clearInterval(interval);

    }, []);

    return {
        packet,
        loading,
        error,
    };

}

export default useLatestPacket;