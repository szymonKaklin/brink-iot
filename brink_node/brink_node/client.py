import time

from brink_node.mqtt_client import start_mqtt_client
from brink_node.utils import load_mqtt_config
from brink_node.diagnostics import get_mac_address

def main():
    # Load MQTT configuration from .env
    config = load_mqtt_config()

    # Generate the device-specific topic using the MAC address
    device_id = get_mac_address()
    topic = f"{device_id}/{config['topic']}"

    # Start the MQTT client
    client = start_mqtt_client(
        config['broker'],
        config['port'],
        config['username'],
        config['password'],
        topic
    )

    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        # Stop the MQTT loop and disconnect
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
