from fastapi import APIRouter
from database.engine import SessionLocal
from database.models import Packet
from database.aqi_result_models import AQIResultModel
from api.schemas.system import SystemStatusResponse

from datetime import datetime, timezone,timedelta
from zoneinfo import ZoneInfo

router = APIRouter(tags=["System"])

SERVER_START_TIME = datetime.now()


@router.get("/system/status", response_model=SystemStatusResponse)
def system_status():
    session = SessionLocal()

    try:
        packet_count = session.query(Packet).count()
        aqi_count = session.query(AQIResultModel).count()

        latest_packet = (
            session.query(Packet)
            .order_by(Packet.received_at.desc())
            .first()
        )

        latest_aqi = (
            session.query(AQIResultModel)
            .order_by(AQIResultModel.created_at.desc())
            .first()
        )

        # Convert UTC -> IST
        last_aqi = None
        if latest_aqi:
            last_aqi = (
                latest_aqi.created_at
                .replace(tzinfo=timezone.utc)
                .astimezone(ZoneInfo("Asia/Kolkata"))
            )

        # Uptime calculation
        uptime = datetime.now() - SERVER_START_TIME

        days = uptime.days
        hours = uptime.seconds // 3600
        minutes = (uptime.seconds % 3600) // 60

        if days > 0:
            uptime_string = f"{days}d {hours}h"
        elif hours > 0:
            uptime_string = f"{hours}h {minutes}m"
        else:
            uptime_string = f"{minutes}m"

        
        #gateway status
        status="offline"
        if latest_packet:
            now=datetime.now(timezone.utc)
            packet_time=latest_packet.received_at.replace(tzinfo=timezone.utc)
            seconds_since_last_packet=(now-packet_time).total_seconds()
            if seconds_since_last_packet<=15:
                status="online"

        print("Now:", now)
        print("Packet:", packet_time)
        print("Seconds:", seconds_since_last_packet)
        return {
            "status": status,
            "database": "connected",
            "version": "1.0.0",

            "packets": packet_count,
            "aqi_records": aqi_count,

            "last_packet": latest_packet.received_at.replace(tzinfo=timezone.utc).astimezone(ZoneInfo("Asia/Kolkata"))
            if latest_packet else None,
            "last_aqi": last_aqi,

            "node_count": 1,
            "uptime": uptime_string,
        }

    finally:
        session.close()