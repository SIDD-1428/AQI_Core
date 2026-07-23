from pathlib import Path
from datetime import datetime
import shutil

#configuration
MAX_BACKUPS=10
PROJECT_ROOT=Path(__file__).resolve().parent.parent
DATABASE_FILE=PROJECT_ROOT /"aqi_core.db"
BACKUP_DIR=PROJECT_ROOT /"backups"

#backup functions
def create_backup():
    try:
        if not DATABASE_FILE.exists():
            return{
                "success":False,
                "error":"Database file not found"
            }
        
        BACKUP_DIR.mkdir(exist_ok=True)
        timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_file=BACKUP_DIR /f"aqi_core_{timestamp}.db"
        shutil.copy2(DATABASE_FILE,backup_file)
        cleanup_old_backups()

        return{
            "success":True,
            "backup_file":str(backup_file)
        }
    
    except Exception as e:
        return{
            "success":False,
            "error":str(e)
        }

#keeps only the latest backup file
def cleanup_old_backups():
    backups=sorted(
        BACKUP_DIR.glob("aqi_core_*.db"),
        key=lambda x:x.stat().st_mtime,
        reverse=True
    )

    for backup in backups[MAX_BACKUPS:]:
        backup.unlink()

#test
if __name__=="__main__":
    result=create_backup()
    if result["success"]:
        print("Backup created")
        print(result["backup_file"])
    else:
        print("Backup failed")
        print(result["error"])
