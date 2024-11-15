import psutil
import os
from typing import Optional, Dict, Any

def get_mac_address() -> str:
    try:
        mac = open("/sys/class/net/wlan0/address").readline().strip()
        return mac.replace(":", "")
    except FileNotFoundError:
        return "unknown"

def get_cpu_temp() -> Optional[float]:
    if os.path.exists("/sys/class/thermal/thermal_zone0/temp"):
        temp = int(os.popen("cat /sys/class/thermal/thermal_zone0/temp").read()) / 1000.0
        return temp
    else:
        return None

def get_diagnostics() -> Dict[str, Any]:
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_temp = get_cpu_temp()
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    diagnostics_message = {
        "cpu_usage": cpu_usage,
        "cpu_temp": cpu_temp,
        "memory_usage": memory_usage
    }

    return diagnostics_message
