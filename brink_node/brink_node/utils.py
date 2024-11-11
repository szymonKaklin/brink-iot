from dotenv import load_dotenv
import os

def load_mqtt_config():
    load_dotenv(os.path.join(os.getcwd(), '.env'))

    config = {
        "broker": os.getenv("BRINK_MQTT_BROKER"),
        "port": int(os.getenv("BRINK_MQTT_PORT")),
        "username": os.getenv("BRINK_MQTT_USERNAME"),
        "password": os.getenv("BRINK_MQTT_PASSWORD"),
        "topic": "diagnostics/info"
    }

    return config
