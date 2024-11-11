import paho.mqtt.client as mqtt
from brink_node.diagnostics import get_diagnostics
import time
import threading

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code: {reason_code}")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    pass

def publish_diagnostics(client, topic):
    while True:
        diagnostics_message = get_diagnostics()
        client.publish(topic, str(diagnostics_message))
        print(f"Published: {diagnostics_message}")
        time.sleep(5)

def start_mqtt_client(broker, port, username, password, topic):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port, 60)
    client.loop_start()

    publish_thread = threading.Thread(target=publish_diagnostics, args=(client, topic))
    publish_thread.daemon = True  # Ensure thread exits when the program does
    publish_thread.start()

    return client
