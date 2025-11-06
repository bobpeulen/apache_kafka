Use Kafka CLI on Oracle Linux 9



# Install Java
- sudo yum install java


- sudo yum install java-21-openjdk -y
- sudo nano /etc/profile.d/java.sh
  ```
  export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-21.0.9.0.10-1.0.1.el9.x86_64
  export PATH=$PATH:$JAVA_HOME/bin
  ```
- source /etc/profile.d/java.sh
- echo $JAVA_HOME


# Install Kafka:
- wget https://dlcdn.apache.org/kafka/4.1.0/kafka_2.13-4.1.0.tgz
- tar -xzf kafka_2.13-4.1.0.tgz
- cd kafka_2.13-4.1.0/

Test connection
````
bin/kafka-topics.sh --create --topic my_topic_1 --bootstrap-server bootstrap-clstr-u8udqubajizcuv58.kafka.eu-frankfurt-1.oci.oraclecloud.com:9093
````
