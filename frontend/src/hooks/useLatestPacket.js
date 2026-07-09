import { useEffect, useState } from "react";
import { getLatestPacket } from "../api/aqiApi";

function useLatestPacket() {
  const [packet, setPacket] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadPacket() {
      try {
        const data =
          await getLatestPacket();
        setPacket(data);
      }

      catch(err){
        setError(err);
      }

      finally{
        setLoading(false);
      }

    }

    loadPacket();

  }, []);

  return {
    packet,
    loading,
    error,
  };

}

export default useLatestPacket;