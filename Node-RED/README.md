# Run Node-RED on OCI

- Create instance in public subnet, Oracle Linux 8 image
- Add 1880 as port in subnet security list
- https://apexapps.oracle.com/pls/apex/r/dbpm/livelabs/run-workshop?p210_wid=805&p210_wec=&session=454482293547
- https://yum.oracle.com/oracle-linux-nodejs.html#EnablingReposOL8

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
- TO DO. Add credentials to (hidden) settings file. The file is located at "/home/opc/.node-red/settings.js". First will prompt for pw.
  ```
  sudo npm install -g --unsafe-perm node-red
  node-red bob hash-pw


# Add PostgreSQL as target

- Install 'node-red-contrib-postgresql' in the 'manage palette'

# Add ADW as target
- See https://blogs.oracle.com/developers/post/interacting-with-your-oracle-on-prem-and-autonomous-db-instances-from-node-red
- Install 'node-red-contrib-oracledb-mod' in the node red UI
- run 'npm install oracledb' in terminal
- run 'sudo npm install' in terminal. This will use the package.json
- https://docs.oracle.com/en/database/oracle/oracle-database/21/lacli/install-instant-client-using-rpm.html

## Copy file
```
scp -i private_key.pem C:\Users\Bob\Downloads\instantclient-basic-linux.x64-23.5.0.24.07.zip opc@150.136.150.209:/home/opc/node-red
scp -i private_key.pem C:\Users\Bob\Downloads\Wallet_DZNPH3ELWCQZTK63.zip opc@150.136.150.209:/home/opc/node-red/oracle/instantclient_23_5/network/admin
export LD_LIBRARY_PATH=/home/opc/node-red/oracle/instantclient_23_5:$LD_LIBRARY_PATH
```

- Change env variables
```
export ORACLE_HOME=/home/opc/.node-red/oracle/instantclient_23_5
export LD_LIBRARY_PATH=/home/opc/.node-red/oracle/instantclient_23_5
export TNS_ADMIN=/home/opc/.node-red/oracle/instantclient_23_5/network/admin

export TNS_ADMIN=/opt/oracle/your_config_dir
node myapp.js

```



