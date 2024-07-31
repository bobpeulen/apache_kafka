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

7. 



   
