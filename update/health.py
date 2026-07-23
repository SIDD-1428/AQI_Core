
from pathlib import Path
from datetime import datetime
import shutil
import subprocess

from update.service_manager import (
    status_backend,
    status_frontend,
    status_gateway
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_FILE = PROJECT_ROOT / "aqi_core.db"
MIN_FREE_DISK_PERCENT = 10


# Database
def check_database():
    exists = DATABASE_FILE.exists()
    return {
        "success": exists,
        "data": {
            "exists": exists,
            "path": str(DATABASE_FILE)
        }
    }


# Disk
def check_disk():
    usage = shutil.disk_usage(PROJECT_ROOT)
    free_percent = (usage.free / usage.total) * 100
    healthy = free_percent > MIN_FREE_DISK_PERCENT
    return {
        "success": healthy,
        "data": {
            "total_gb": round(usage.total / (1024 ** 3), 2),
            "used_gb": round(usage.used / (1024 ** 3), 2),
            "free_gb": round(usage.free / (1024 ** 3), 2),
            "free_percent": round(free_percent, 2)
        }
    }



# Internet
def check_internet():
    result = subprocess.run(
        ["ping", "-c", "1", "8.8.8.8"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    connected = result.returncode == 0
    return {
        "success": connected,
        "data": {
            "connected": connected
        }
    }



# Services
def check_services():
    return {
        "success": True,
        "data": {
            "backend": status_backend(),
            "gateway": status_gateway(),
            "frontend": status_frontend()
        }
    }



# Complete Health Report
def system_health():
    report = {
        "database": check_database(),
        "disk": check_disk(),
        "internet": check_internet(),
        "services": check_services()
    }
    overall = (
        report["database"]["success"]
        and report["disk"]["success"]
        and report["internet"]["success"]
    )
    return {
        "success": overall,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "data": report
    }


# Test
if __name__ == "__main__":
    from pprint import pprint
    pprint(system_health())