import {useState, useEffect} from "react";
import { getAQIHistory } from "../api/aqiApi";
function useAQIHistory(){
    const[history,setHistory]=useState([]);
    const[loading,setLoading] = useState(true);
    const[error,setError]=useState(null);
    useEffect(()=>{
        async function loadHistory(){
            try{
                const data=await getAQIHistory();
                setHistory(data);
            }
            catch(err){
                setError(err);
            }
            finally{
                setLoading(false);
            }
        }
        loadHistory();
    },[]);

    return{
        history,
        loading,
        error,
    };
}

export default useAQIHistory;