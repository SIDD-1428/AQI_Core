#service manager

import subprocess

def run_systemctl(command):
    try:
        result=subprocess.run(
            ["sudo","systemctl"]+command,
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
            "error":"systemctl not found."
        }
    
    except Exception as e:
        return{
            "success":False,
            "error":str(e)
        }

#service controls
def start_service(service):
    return run_systemctl(
        ["start",service]
    )

def stop_service(service):
    return run_systemctl(
        ["stop",service]
    )

def restart_service(service):
    return run_systemctl(
        ["restart",service]
    )

def get_service_status(service):
    result=subprocess.run(
        ["sudo","systemctl","is-active", service],
        capture_output=True,
        text=True
    )

    status=result.stdout.strip()

    return{
        "success":True,
        "data":{
            "service":service,
            "status":status
        }
    }

#shortcuts
def restart_backend():
    return restart_service("aqi-backend.service")

def restart_gateway():
    return restart_service("aqi-gateway.service")

def restart_frontend():
    return restart_service("aqi-frontend.service")

def status_backend():
    return get_service_status("aqi-backend.service")

def status_gateway():
    return get_service_status("aqi-gateway.service")

def status_frontend():
    return get_service_status("aqi-frontend.service")


if __name__=="__main__":
    print(status_backend())
    print(status_gateway())
    print(status_frontend())