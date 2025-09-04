# Run Node-RED on OCI

- Create instance in public subnet, Oracle Linux 8 image
- Add 1880 as port in subnet security list

- First install Node.js. Run to list available modules for Node.js
  ```
  cd .. ## make sure to be in home directory
  sudo dnf module list --all nodejs
  ```

- Review latest version and change number in below. Run to install.
  ```
  sudo dnf module enable nodejs:20
  sudo dnf module install nodejs
  node -v ### to review version
  ```

- Next. Run to install Git, clone Node RED repo and install dependencies.
  ```
  sudo yum install git
  sudo npm install -g grunt-cli
  sudo git clone https://github.com/node-red/node-red.git
  cd node-red
  sudo npm install
  grunt build
  ```

- Firewall and setenforce
  ```
  sudo firewall-cmd --permanent --add-port=1880/tcp
  sudo firewall-cmd --reload
  sudo setenforce 0
  ```
 
- Start Node-RED. In the 'node-red' directory:
  ```
  npm start

  ```

- Open on "http://<public ip>:1880
    Eg. http://150.136.150.209:1880/
 
- Start on boot
  ```
  sudo npm install -g pm2
  pm2 start /home/opc/node-red -- -v
  ```
-  Add credentials to settings file. The file is located at "/home/opc/.node-red/settings.js". First will prompt for pw.
  ```
  sudo npm install -g --unsafe-perm node-red
  node-red bob hash-pw
  ```

- Add the newly created password to the settings file.


# Add PostgreSQL as target

- Install 'digitaloak/node-red-contrib-digitaloak-postgresql' in Node-RED using manage palette
- Create table in postgresql db.

```
CREATE TABLE kpnthings_latlong (
  battery VARCHAR(255),
  acc_x  FLOAT,
  acc_y  FLOAT,
  acc_z  FLOAT,
  lat  FLOAT,
  long  FLOAT
);
```
- Full function. After Converter to JSON Object. msg.payload refers to that.
```
var battery = msg.payload[0].vs
var acc_x = msg.payload[1].v
var acc_y = msg.payload[2].v
var acc_z = msg.payload[3].v
var lat = msg.payload[4].v
var long = msg.payload[5].v
msg.query = `INSERT INTO kpnthings_latlong (battery, acc_x, acc_y, acc_z, lat, long) VALUES (` + battery + `,` + acc_x + `,` + acc_y + `,` + acc_z + `,` + lat + `,` + long + `)` 
return msg;
```

![image](https://github.com/user-attachments/assets/a2f996b2-c5a7-4f61-b36b-0fb8f954f681)
![image](https://github.com/user-attachments/assets/50ccaac6-c682-45a7-8285-8c5f9d599e21)
![image](https://github.com/user-attachments/assets/568e23b3-0c4f-4fdf-9593-2969bd290f71)









