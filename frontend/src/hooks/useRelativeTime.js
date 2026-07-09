import {useState,useEffect} from "react";

export default function useRelativeTime(timestamp){
    const[,forceUpdate]=useState(0);

    useEffect(()=>{
        const timer=setInterval(()=>{
            forceUpdate((value)=>value+1);
        },1000);

        return()=> clearInterval(timer);
    },[]);

    const seconds=Math.max(
        0,
        Math.floor((Date.now()-timestamp)/1000)
    );

    if(seconds<5) return "Just now";
    if(seconds<60) return `${seconds}s ago`

    const minutes=Math.floor(seconds/60);
    if(minutes<60)return `${minutes}m ago`

    const hours=Math.floor(minutes/60);
    return `${hours}h ago`
}