import paho.mqtt.client as mqtt
import psutil
from dotenv import load_dotenv
import time
import os
import threading

# Load .env file environment variables
load_dotenv()

# MQTT broker configuration
BROKER = os.getenv("BRINK_MQTT_BROKER")        # Replace with your broker address
PORT = int(os.getenv("BRINK_MQTT_PORT"))       # Replace with your broker port
USERNAME = os.getenv("BRINK_MQTT_USERNAME")    # Replace with your broker username
PASSWORD = os.getenv("BRINK_MQTT_PASSWORD")    # Replace with your broker password

TOPIC = "diagnostics/info"

def get_mac_address():
    try:
        # Get the MAC address of the wifi interface to serve as identifier of device
        mac = open("/sys/class/net/wlan0/address").readline().strip()
        return mac.replace(":", "")
    except FileNotFoundError:
        return "unknown"

# Get and prepend device ID to topic
DEVICE_ID = get_mac_address()
TOPIC = DEVICE_ID + "/" + TOPIC

def get_cpu_temp():
    if os.path.exists("/sys/class/thermal/thermal_zone0/temp"):
        temp = int(os.popen("cat /sys/class/thermal/thermal_zone0/temp").read()) / 1000.0
        return temp
    else:
        return None

# Callback function when the client connects to the broker
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code: {reason_code}")
    # Subscribe to topics here if necessary
    # SYS Topic gives broker information - will monitor this in future
    # client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    pass

# Function to publish diagnostics information
def publish_diagnostics(client):
    while True:
        # Gather diagnostics information
        cpu_usage = psutil.cpu_percent(interval=1)
        cpu_temp = get_cpu_temp()
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent

        # Prepare the diagnostics message
        diagnostics_message = {
            "cpu_usage": cpu_usage,
            "cpu_temp": cpu_temp,
            "memory_usage": memory_usage
        }

        # Publish the diagnostics information to the MQTT broker
        client.publish(TOPIC, str(diagnostics_message))

        # Print to the console
        print(f"Published: {diagnostics_message}")

        # Wait for a while before sending the next update
        time.sleep(5)

# Create an MQTT client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Set username and password for the MQTT broker
client.username_pw_set(USERNAME, PASSWORD)

# Assign the on_connect and on_message callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(BROKER, PORT, 60)

# Start the MQTT loop in a separate thread
client.loop_start()

# Start publishing diagnostics in a separate thread
publish_thread = threading.Thread(target=publish_diagnostics, args=(client,))
publish_thread.daemon = True  # This ensures the thread will exit when the main program does
publish_thread.start()

try:
    # Keep the main thread alive
    while True:
        time.sleep(1)  # You can adjust this if needed

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Stop the MQTT loop and disconnect
    client.loop_stop()
    client.disconnect()

