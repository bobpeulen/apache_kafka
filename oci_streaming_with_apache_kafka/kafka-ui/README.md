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
sudo docker run -it -p 8081:8081 \
-e SCHEMA_REGISTRY_KAFKASTORE_BOOTSTRAP_SERVERS="SASL_SSL://bootstrap-clstr-x.kafka.eu-frankfurt-1.oci.oraclecloud.com:9092" \
-e SCHEMA_REGISTRY_KAFKASTORE_SECURITY_PROTOCOL=SASL_SSL \
-e SCHEMA_REGISTRY_KAFKASTORE_SASL_MECHANISM=SCRAM-SHA-512 \
-e SCHEMA_REGISTRY_KAFKASTORE_SASL_JAAS_CONFIG='org.apache.kafka.common.security.scram.ScramLoginModule required username="super-user-x" password="xxx";' \
-e SCHEMA_REGISTRY_HOST_NAME=localhost \
-e SCHEMA_REGISTRY_LISTENERS=http://localhost:8081 \
confluentinc/cp-schema-registry:8.0.0
```







