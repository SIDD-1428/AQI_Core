"""
Version Manager
reads software version from version.json
"""

import json
from pathlib import Path

PROJECT_ROOT=Path(__file__).resolve().parent.parent
VERSION_FILE=PROJECT_ROOT /"version.json"

def get_version():
    try:
        with open(VERSION_FILE,"r") as file:
            return json.load(file)
    
    except FileNotFoundError:
        return{
            "success":False,
            "error":"version.json not found"
        }

    except Exception as e:
        return{
            "success":False,
            "error":str(e)
        }

if __name__ == "__main__":
    version=get_version()
    print(version)
    