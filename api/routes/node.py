from fastapi import APIRouter
from api.services.packet_service import PacketService
router=APIRouter()

@router.get("/node/list")
def node_list():
    service=PacketService()
    try:
        nodes=service.get_nodes()
        return{
            "nodes":[node[0] for node in nodes]
        }
    finally:
        service.close()


@router.get("/node/{node_id}/latest")
def latest_node(node_id:str):
    service=PacketService()

    try:
        packet=service.get_latest_node(node_id)
        if packet is None:
            return {"message":"Node not found"}
        
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

@router.get("/node/{node_id}/history")
def node_history(node_id:str, limit: int=50):
    service=PacketService()

    try:
        packets=service.get_history_by_node(node_id,limit)
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