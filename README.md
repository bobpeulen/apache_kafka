# apache_kafka


# Run RabbitMQ usind Docker

1. Create an instance with Oracle Linux 7. Run

see: https://www.svix.com/resources/guides/rabbitmq-docker-setup-guide/

  ```
  sudo yum install docker-engine docker-cli
  sudo systemctl enable --now docker
  ```

2. Check whether Docker is running
  
  ```
  systemctl status docker
  ````

3. Pull docker
```
sudo docker pull rabbitmq:3-management
```

3. Default user
```
sudo docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

4. Go to http://[PUBLIC IP]::15672/

-------- END


```
sudo docker run -d \
--restart always \
--hostname rabbitmq-demo.bobpeulen.com \
-p 8080:15672 -p 5672:5672 \
-e RABBITMQ_DEFAULT_USER=bobpeulen \
-e RABBITMQ_DEFAULT_PASS=Blabla1991!! \
-v /home/opc/rabbitmq/enabled_plugins:/etc/rabbitmq/enabled_plugins \
-v /home/opc/rabbitmq/:/var/lib/rabbitmq \
--name rabbitmq \
rabbitmq:3-management
```






xxxx








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
-p 8080:15672 -p 5672:5672 \
-e RABBITMQ_DEFAULT_USER=bobpeulen \
-e RABBITMQ_DEFAULT_PASS=Blabla1991!! \
-v /home/opc/rabbitmq/enabled_plugins:/etc/rabbitmq/enabled_plugins \
-v /home/opc/rabbitmq/:/var/lib/rabbitmq \
--name rabbitmq \
rabbitmq:3-management
```


```
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --reload
```

   
