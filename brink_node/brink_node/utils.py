import os
from typing import Dict, Any

from dotenv import load_dotenv

def load_mqtt_config() -> Dict[str, Any]:
    load_dotenv(os.path.join(os.getcwd(), '.env'))

    config = {
        "broker": os.getenv("BRINK_MQTT_BROKER"),
        "port": int(os.getenv("BRINK_MQTT_PORT")),
        "username": os.getenv("BRINK_MQTT_USERNAME"),
        "password": os.getenv("BRINK_MQTT_PASSWORD"),
        "topic": "diagnostics/info"
    }

    return config
