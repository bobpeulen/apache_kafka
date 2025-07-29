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
- Click on "Secured with Auth?" and add your username and password stored in OCI Vault

- Optionally, add Schema registry, etc.
- Click validate and submit.


<img width="996" height="836" alt="image" src="https://github.com/user-attachments/assets/c15dcb0e-1b76-48ba-95c1-38bc26553234" />
