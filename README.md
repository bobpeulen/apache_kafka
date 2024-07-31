# apache_kafka


# Install RabbitMQ

1. Create an instance with Oracle Linux 7. Run


  ```
  sudo yum install docker-engine docker-cli
  sudo systemctl enable --now docker
  ```

2. Check whether Docker is running
  
  ```
  systemctl status docker
  ````

3. Change the user Docker will use
  ```
  sudo service docker restart
  sudo usermod -a -G docker opc
  ```

4. RabbitMQ. Create directory. 
 ```
 mkdir rabbitmq
 cd rabbitmq
 nano enabled_plugins
 ```
5. Add the below to the enabled_pugins file

 ```
 [rabbitmq_management,rabbitmq_mqtt].
 ```

6. Change permission on file
```
  sudo chmod 777 enabled_plugins
   ```

7. Install RabbitMQ

```
sudo docker run -d \
--restart always \
--hostname rabbitmq-demo.bobpeulen.com \
-p 80:15672 -p 1883:1883 -p 443:15671 \
-e RABBITMQ_DEFAULT_USER=bobpeulen \
-e RABBITMQ_DEFAULT_PASS=Blabla1991!! \
-v /home/opc/rabbitmq/enabled_plugins:/etc/rabbitmq/enabled_plugins \
-v /home/opc/rabbitmq/:/var/lib/rabbitmq \
--name rabbitmq \
rabbitmq:3-management
```

8. 



   
