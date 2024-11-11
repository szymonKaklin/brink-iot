# Brink IoT
Brink IoT is a personal project which serves as a comprehensive demonstration of IoT architecture, showcasing skills in device management, cloud-native microservices, containerization, automation, and modern infrastructure tools.
It is designed as a personal project that simulates enterprise-level IoT management systems, suitable for use as a portfolio project to demonstrate expertise in key technologies and practices.

# Usage
Build docker container from whilst in the project directory using:
```
sudo docker build -t brink:latest .
```
Launch the container:
```
sudo docker run -d --network host --name brink_iot brink:latest
```
