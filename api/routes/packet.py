from fastapi import APIRouter, HTTPException
from api.services.packet_service import PacketService
from api.schemas.packet import PacketResponse
from typing import List

router=APIRouter(tags=["Packet"])

@router.get("/packet/latest",response_model=PacketResponse)
def latest_packet():
    service=PacketService()

    try:
        packet=service.get_latest_packet()
        if packet is None:
            raise HTTPException(
                status_code=404,
                detail="No packet data available"
            )
        
        return{
            "node":packet.node,
            "sequence":packet.sequence,
            "temperature":packet.temperature,
            "humidity":packet.humidity,
            "pressure":packet.pressure,
            "pm1_0":packet.pm1_0,
            "pm2_5":packet.pm2_5,
            "pm10":packet.pm10,
            "o3":packet.o3,
            "no2":packet.no2,
            "co":packet.co,
            "nh3":packet.nh3,
            "so2":packet.so2,
            "rssi":packet.rssi,
            "snr":packet.snr,
            "timestamp":packet.timestamp
        }
    
    finally:
        service.close()

@router.get("/packet/history",response_model=List[PacketResponse])

def packet_history(limit: int=50):
    service=PacketService()

    try:
        packets=service.get_history(limit)
        history=[]
        for packet in packets:
            history.append({
                "node":packet.node,
                "sequence":packet.sequence,
                "temperature":packet.temperature,
                "humidity":packet.humidity,
                "pressure":packet.pressure,
                "pm1_0":packet.pm1_0,
                "pm2_5":packet.pm2_5,
                "pm10":packet.pm10,
                "o3":packet.o3,
                "no2":packet.no2,
                "co":packet.co,
                "nh3":packet.nh3,
                "so2":packet.so2,
                "rssi":packet.rssi,
                "snr":packet.snr,
                "timestamp":packet.timestamp
            })
        return history
    finally:
        service.close()