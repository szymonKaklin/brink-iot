# Brink IoT
Brink IoT is a personal project which serves as a comprehensive demonstration of IoT architecture, showcasing skills in device management, cloud-native microservices, containerization, automation, and modern infrastructure tools.
It is designed as a personal project that simulates enterprise-level IoT management systems, suitable for use as a portfolio project to demonstrate expertise in key technologies and practices.

# Usage
Create and configure a .env file according to your broker configuration
```
# BRINK IOT MQTT BROKER CONFIGURATION
BRINK_MQTT_BROKER="<ip_address_of_broker>"
BRINK_MQTT_PORT="1883<port (usually 1883)>"
BRINK_MQTT_USERNAME="<username_of_client>"
BRINK_MQTT_PASSWORD="<password_of_client>"
```

Build docker container from whilst in the project directory using:
```
sudo docker build -t brink:latest .
```
Launch the container (include .env file):
```
sudo docker run -d --network host --name brink_iot brink:latest
```


