"""
AirX Update Manager

Coordinates the complete update process.
"""

from pprint import pprint

from update.backup import create_backup
from update.git_manager import (
    get_git_info,
    check_for_updates,
    pull_updates,
)
from update.service_manager import (
    restart_backend,
    restart_gateway,
    restart_frontend,
)
from update.health import system_health
from update.version import get_version


def perform_update():
    """
    Execute the complete AirX update workflow.
    """
    report = {
        "version": get_version(),
        "backup": None,
        "git": None,
        "services": {},
        "health": None,
    }
    print("\n========== AirX Update Manager ==========\n")


    # Backup
    print("[1/5] Creating database backup...")
    report["backup"] = create_backup()
    if report["backup"]["success"]:
        print("✓ Backup completed.")
    else:
        print("✗ Backup failed.")
        return report

    # Git
    print("\n[2/5] Checking for updates...")
    updates=check_for_updates()

    report["git"] = {
        "info": get_git_info(),
        "update_check":updates
    }

    if updates["data"]["update_available"]:
        print("Updates found")
        report["git"]["pull"]=pull_updates()
    else:
        print("✓ System already up to date.")
    

    # Restart Services
    print("\n[3/5] Restarting services...")
    report["services"]["backend"] = restart_backend()
    report["services"]["gateway"] = restart_gateway()
    report["services"]["frontend"] = restart_frontend()
    print("✓ Services restarted.")

    # Health Check
    print("\n[4/5] Running health check...")
    report["health"] = system_health()
    print("✓ Health check completed.")
    print("\n[5/5] Update finished.\n")

    return report


if __name__ == "__main__":
    result = perform_update()
    print("\n========== FINAL REPORT ==========\n")
    pprint(result)