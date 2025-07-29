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
