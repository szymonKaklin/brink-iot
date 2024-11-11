# Usage

Create and configure a .env file according to your broker configuration to sit in the directory from which
the node is launched from

```
# BRINK IOT MQTT BROKER CONFIGURATION
BRINK_MQTT_BROKER="<ip_address_of_broker>"
BRINK_MQTT_PORT="<port (usually 1883)>"
BRINK_MQTT_USERNAME="<username_of_client>"
BRINK_MQTT_PASSWORD="<password_of_client>"
```

# Build the python package

```
python setup.py sdist bdist_wheel
```

## Install using pip

```
pip install dist/brink_node-<version>.whl
```

## Run

```
brink-node
```

# Docker (depractaed - update this)

Build docker container from whilst in the project directory using:

```
sudo docker build -t brink:latest .
```

Launch the container (include .env file):

```
sudo docker run -d --network host --name brink_iot brink:latest
```
