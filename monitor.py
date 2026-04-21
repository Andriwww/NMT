import subprocess
import platform
from datetime import datetime

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        if "time=" in output or "tiempo=" in output:
            if "time=" in output:
                time_part = output.split("time=")[1].split("ms")[0]
            else:
                time_part = output.split("tiempo=")[1].split("ms")[0]
            latency = time_part.strip()
        else:
            latency = None
        return True, latency
    except subprocess.CalledProcessError:
        return False, None

def check_hosts(hosts):
    for host in hosts:
        status, latency = ping(host)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if status:
            print(f"{timestamp} | {host} -> UP ({latency} ms)")
        else:
            print(f"{timestamp} | {host} -> DOWN")
