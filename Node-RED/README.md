# Run Node-RED on OCI

- Create instance in public subnet, Oracle Linux 8 image
- Add 1880 as port in subnet security list
- https://apexapps.oracle.com/pls/apex/r/dbpm/livelabs/run-workshop?p210_wid=805&p210_wec=&session=454482293547
- https://yum.oracle.com/oracle-linux-nodejs.html#EnablingReposOL8

- First install Node.js. Run to list available modules for Node.js
  ```
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
  git clone https://github.com/node-red/node-red.git
  cd node-red
  npm install
  grunt build
  ```

- Firewall and setenforce
  ```
  sudo firewall-cmd --permanent --add-port=1880/tcp
  sudo systemctl start firewalld
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

