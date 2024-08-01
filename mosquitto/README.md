# Create and run Mosquitto using Docker



1. Install Docker
```
sudo yum install docker-engine docker-cli -y
```

2. Start Docker
```
sudo systemctl enable --now docker
```

3. Check whether Docker is running

```
systemctl status docker
```
4. Run simple, without auth, as test
```
sudo docker run -it --name mosquitto_simple -p 1883:1883 -p 8883:8883 eclipse-mosquitto 
```

5. Enable HTTP traffic to compute
```
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --reload
```

6. Stop Docker
```
sudo docker stop mosquitto_simple
```

7. Create directories and config
```
cd opc
mkdir docker-mosquitto
cd docker-mosquitto
mkdir mosquitto 
mkdir mosquitto/config/ 
mkdir mosquitto/data/
mkdir mosquitto/log/
mkdir mosquitto/config/certs/
touch mosquitto/config/mosquitto.conf
```
8. Edit config file
```
nano mosquitto/config/mosquitto.conf
```
9. Add:
```
allow_anonymous true
listener 8883
persistence true
persistence_loction /mosquitto/data/
log_dest file /mosquitto/log/mosquitto.log
cafile /mosquitto/config/certs/ca.crt
keyfile /mosquitto/config/certs/server.key
certfile /mosquitto/config/certs/server.crt
tls_version tlsv1
require_certificate true
use_identity_as_username true


```
10. See: https://stackoverflow.com/questions/70110392/mqtt-tls-certificate-verify-failed-self-signed-certificate
10. Create certifates for TLS connection. Step into the certs folder and run the below. pw mosquitto. For the 4th command. Use the hostname (IP) to add.

```
sudo openssl genrsa -des3 -out ca.key 2048
sudo openssl req -new -x509 -days 1826 -key ca.key -out ca.crt
sudo openssl genrsa -out server.key 2048
sudo openssl req -new -out server.csr -key server.key
sudo openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 360
```

10. Run Docker with conf file. 
```
sudo systemctl restart docker
sudo docker run -it --name mosquitto_open3 -p 1883:1883 -p 8883:8883 -v $(pwd)/mosquitto:/mosquitto/ eclipse-mosquitto
```
sudo docker run -it --name mosquitto_open5 -p 1883:1883 -p 8883:8883 -e MOSQUITTO_USERNAME=mosquittopw -e MOSQUITTO_PASSWORD=mosquittopw -v $(pwd)/mosquitto:/mosquitto/ eclipse-mosquitto

XX. Run with TLS/SSL
sudo docker run -it --name mosquitto_open15239 -p 1883:1883 -p 8883:8883 -v $(pwd)/mosquitto:/mosquitto/ eclipse-mosquitto





