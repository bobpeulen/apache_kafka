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

TEST - PW FILE
sudo docker run -it --name mosquitto_open323 -p 1883:1883 -v $(pwd)/mosquitto:/mosquitto/ eclipse-mosquitto


sudo chmod 0700 mosquitto/pwfile
sudo chown root mosquitto/pwfile

sudo docker exec mosquitto_open4456 mosquitto_passwd -U mosquitto/pwfile




10. Run Docker with conf file. 
```
sudo systemctl restart docker
sudo docker run -it --name mosquitto_open3 -p 1883:1883 -p 8883:8883 -v $(pwd)/mosquitto:/mosquitto/ eclipse-mosquitto
```
sudo docker run -it --name mosquitto_open5 -p 1883:1883 -p 8883:8883 -e MOSQUITTO_USERNAME=mosquittopw -e MOSQUITTO_PASSWORD=mosquittopw -v $(pwd)/mosquitto:/mosquitto/ eclipse-mosquitto

XX. Run with TLS/SSL
sudo docker run -it --name mosquitto_open15239 -p 1883:1883 -p 8883:8883 -v $(pwd)/mosquitto:/mosquitto/ eclipse-mosquitto



# Create and run Mosquitto using CentOS 7 Image

- Create instance with CentOS 7 image
- Follow these steps to update a file for use of yum. https://dev.to/franzwong/fix-cannot-find-a-valid-baseurl-for-repo-in-centos-1h07
- https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-the-mosquitto-mqtt-messaging-broker-on-centos-7
- Run

  ```
  sudo yum -y install epel-release
  sudo yum -y install mosquitto
  sudo systemctl start mosquitto
  sudo systemctl enable mosquitto
  ```

- Firewall settings
  ```
  sudo firewall-cmd --permanent --add-service=http
  sudo firewall-cmd --permanent --add-port=1883/tcp
  sudo firewall-cmd --reload
  ```

- Test. Open two terminals.
  ```
  mosquitto_sub -h localhost -t test
  mosquitto_pub -h localhost -t test -m "hello world"
  ```


- PW file. Username is in cmnd, password will be prompted and added (Herken....)
  ```
  sudo mosquitto_passwd -c /etc/mosquitto/passwd bob
  ```

- Config file. Remove first, create new
  ```
  sudo rm /etc/mosquitto/mosquitto.conf
  sudo nano /etc/mosquitto/mosquitto.conf

  listener 1883
  allow_anonymous false
  password_file /etc/mosquitto/passwd
  #require_certificate true
  ```

- Restart
  ```
  sudo systemctl restart mosquitto
  ```

- Test with credentials
  ```
  mosquitto_sub -h localhost -t test -u "bob" -P "password"
  mosquitto_pub -h localhost -t "test" -m "hello world" -u "bob" -P "password"


# Keys. Public IP should be added to public DNS. 
  ```
  sudo yum -y install certbot
  sudo certbot certonly --standalone
  ```

- Use: mosquitto-demo.cooldemo.org

- Create Cron job to create new certificates every day
```
sudo EDITOR=nano crontab -e
15 3 * * * certbot renew --noninteractive --post-hook "systemctl restart mosquitto"
```


