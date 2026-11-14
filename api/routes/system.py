from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from fastapi import APIRouter

from api.schemas.system import SystemStatusResponse
from database.aqi_result_models import AQIResultModel
from database.engine import SessionLocal
from database.models import Packet


router = APIRouter(tags=["System"])
SERVER_START_TIME = datetime.now(timezone.utc)


@router.get("/system/status", response_model=SystemStatusResponse)
def system_status():
    session = SessionLocal()

    try:
        packet_count = session.query(Packet).count()
        aqi_count = session.query(AQIResultModel).count()
        node_count = session.query(Packet.node).distinct().count()

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

        now = datetime.now(timezone.utc)
        status = "offline"
        last_packet = None

        if latest_packet is not None:
            packet_time = latest_packet.received_at
            if packet_time.tzinfo is None:
                packet_time = packet_time.replace(tzinfo=timezone.utc)

            age_seconds = (now - packet_time).total_seconds()
            status = (
                "online" if 0 <= age_seconds <= 15 else "offline"
            )
            last_packet = packet_time.astimezone(
                ZoneInfo("Asia/Kolkata")
            )

        last_aqi = None
        if latest_aqi is not None and latest_aqi.created_at is not None:
            aqi_time = latest_aqi.created_at
            if aqi_time.tzinfo is None:
                aqi_time = aqi_time.replace(tzinfo=timezone.utc)
            last_aqi = aqi_time.astimezone(ZoneInfo("Asia/Kolkata"))

        uptime = now - SERVER_START_TIME
        days = uptime.days
        hours = uptime.seconds // 3600
        minutes = (uptime.seconds % 3600) // 60

        if days > 0:
            uptime_string = f"{days}d {hours}h"
        elif hours > 0:
            uptime_string = f"{hours}h {minutes}m"
        else:
            uptime_string = f"{minutes}m"

        return {
            "status": status,
            "database": "connected",
            "version": "1.0.0",
            "packets": packet_count,
            "aqi_records": aqi_count,
            "last_packet": last_packet,
            "last_aqi": last_aqi,
            "node_count": node_count,
            "uptime": uptime_string,
        }
    finally:
        session.close()
