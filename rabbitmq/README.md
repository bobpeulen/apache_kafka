# Run RabbitMQ using Docker

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
sudo docker run -d --name rabbitmq2 -p 5672:5672 -p 15672:15672 -p 8883:8883 rabbitmq:3-management
```

4. Go to http://[PUBLIC IP]::15672/


5. Test using CMD.
curl -i -u guest:guest http://150.136.15.87:15672/api/vhosts

```
curl -s -u guest:guest -H "Accept: application/json" -H "Content-Type:application/json" -X POST -d'{  ^
    "vhost": "/", ^
    "name": "amq.direct", ^
    "properties": { ^
        "delivery_mode": 2, ^
        "headers": {} ^
    }, ^
    "routing_key": "kpnthings", ^
    "delivery_mode": "1", ^
    "payload":"{'example:'payloadx'}", ^
    "headers": {}, ^
    "props": {}, ^
    "payload_encoding": "string" ^
}' http://150.136.15.87:15672/api/exchanges/%2F/amq.direct/publish

```


```
curl -XPOST -d'{"properties":{},"routing_key":"kpnthings","payload":"my body","payload_encoding":"string"}' https://guest:guest@150.136.15.87:15672/api/exchanges/vhost/amq.default/publish
```
5. Review queues available.
```
curl -i -u guest:guest http://150.136.15.87:15672/api/queues
```
6. Create new vhost
```
curl -i -u guest:guest -H "content-type:application/json" -XPUT http://150.136.15.87:15672/api/vhosts/foo
```

7. Create an exchange, add binding to queue. Publish.
```
curl -i -H "Content-Type:application/json" -X POST -u guest:guest http://150.136.15.87:15672/api/exchanges/foo/amq.direct/publish -d'{"properties":{},"routing_key":"testqueue","payload":"my body","payload_encoding":"string"}'
```	
[]
[]
[]
[]
[]

curl -u guest:guest -i -H "Content-Type:application/json" -X PUT http://150.136.15.87:15672/api///exchanges/kpnthingsexchange/publish -d'{"properties":{},"routing_key":"kpnthings","payload":"my body","payload_encoding":"string"}'


curl -s -u guest:guest -H "Content-Type:application/json" -X POST -d'{"vhost": "/",  "name": "amq.direct",   "properties": { "delivery_mode": 2, "headers": {}}, "routing_key": "testqueue", "delivery_mode": "1", "payload":"{'example:'payloadx'}", "headers": {}, "props": {}, "payload_encoding": "string"}' http://150.136.15.87:15672/api/exchanges/foo/amq.direct/publish







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

   
