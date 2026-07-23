#airX git manager

from pathlib import Path
import subprocess

PROJECT_ROOT=Path(__file__).resolve().parent.parent

def run_git_command(command):
    try:
        result=subprocess.run(
            command,
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=True
        )

        return{
            "success":True,
            "data":result.stdout.strip()
        }
    
    except subprocess.CalledProcessError as e:
        return{
            "success":False,
            "error":e.stderr.strip()
        }
    
    except FileNotFoundError:
        return{
            "success":False,
            "error":"Git is not installed"
        }

    except Exception as e:
        return{
            "success":False,
            "error":str(e)
        }

def get_current_branch():
    return run_git_command(
        ["git","branch","--show-current"]
    )


def get_current_commit():
    return run_git_command(
        ["git","rev-parse","--short","HEAD"]
    )


def get_git_info():
    branch=get_current_branch()
    commit=get_current_commit()

    if not branch["success"]:
        return branch
    
    if not commit["success"]:
        return commit
    
    return{
        "success":True,
        "data":{
            "branch":branch["data"],
            "commit":commit["data"]
        }
    }

def fetch_updates():
    return run_git_command(
        ["git","fetch","origin"]
    )

def check_for_updates():
    fetch=fetch_updates()

    if not fetch["success"]:
        return fetch
    
    local=run_git_command(
        ["git","rev-parse","HEAD"]
    )

    remote=run_git_command(
        ["git","rev-parse","@{u}"]
    )

    if not local["success"]:
        return local
    
    if not remote["success"]:
        return remote
    
    update_available=local["data"]!=remote["data"]

    return{
        "success":True,
        "data":{
            "update_available":update_available,
            "local_commit":local["data"],
            "remote_commit":remote["data"]
        }
    }

def pull_updates():
    return run_git_command(
        ["git","pull","origin","main"]
    )
if __name__ == "__main__":
    print(check_for_updates())