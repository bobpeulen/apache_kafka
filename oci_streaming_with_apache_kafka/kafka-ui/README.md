# Deploy Kafka UI for OCI Streaming with Apache Kafka

- Using: https://github.com/provectus/kafka-ui
- Oracle Linux 9, deployed in public subnet, with OSAK cluster in same VCN, private subnet
- Open ports in security lists

## Install and run Docker

- Install Docker
  ```
  sudo yum install -y yum-utils  
  sudo yum-config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo
  sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
  ```

- Start Docker
  ```
  sudo systemctl start docker
  ```

## Open Port and Run Kafka UI

  ```
  sudo firewall-cmd --permanent --add-port=8080/tcp
  sudo firewall-cmd --reload 
  sudo docker run -it -p 8080:8080 -e DYNAMIC_CONFIG_ENABLED=true provectuslabs/kafka-ui
  ```

## Open Kafka UI
- Open Kafka UI on http://[Public URL]:8080
- Add your SASL-SCRAM Bootstrap URL as Bootstrap server
- Use SASL/SCARM-512 and SASL_SSL as protocol
- Click on "Secured with Auth?" and add your username and password stored in OCI Vault (Secret content)

- Optionally, add Schema registry, etc.
- Click validate and submit.


<img width="996" height="836" alt="image" src="https://github.com/user-attachments/assets/c15dcb0e-1b76-48ba-95c1-38bc26553234" />

## Test Schema registry
- Open port (not sure is needed)
  ```
  sudo firewall-cmd --permanent --add-port=8081/tcp
  ```
  
```
sudo docker run -p 8081:8081 -d  \
  --net=host \
  --name=schema-registry \
  -e SCHEMA_REGISTRY_KAFKASTORE_BOOTSTRAP_SERVERS=SASL_SSL://bootstrap-clstr-u8udqubajizcuv58.kafka.eu-frankfurt-1.oci.oraclecloud.com:9092 \
  -e SCHEMA_REGISTRY_HOST_NAME=localhost \
  -e SCHEMA_REGISTRY_LISTENERS=http://localhost:8081 \
  -e SCHEMA_REGISTRY_DEBUG=true \
  confluentinc/cp-schema-registry:8.0.0
```





- Create a schema-registry-compose.yaml file with below and run:
  ```
  sudo docker compose -f schema-registry-compose.yaml up -d
  ```
- .yaml file:
  
  ```
  version: '1'
  
  services:
    kafka-schema-registry:
      image: confluentinc/cp-schema-registry
      hostname: kafka-schema-registry
      container_name: kafka-schema-registry
      ports:
        - "8081:8081"
      environment:
        SCHEMA_REGISTRY_HOST_NAME: kafka-schema-registry
        SCHEMA_REGISTRY_KAFKASTORE_BOOTSTRAP_SERVERS: 'PLAINTEXT://kafka:29092'
        SCHEMA_REGISTRY_LISTENERS: http://0.0.0.0:8081
  ```

<img width="644" height="383" alt="image" src="https://github.com/user-attachments/assets/e1f1020c-e110-4efd-a4f4-3386cae1c380" />


