# Run Node-RED on OCI

- Create instance in public subnet, Oracle Linux image
- Add 1880 as port in subnet security list
- https://apexapps.oracle.com/pls/apex/r/dbpm/livelabs/run-workshop?p210_wid=805&p210_wec=&session=454482293547

- Run

  ```npm install n -g
  sudo yum install -y oracle-nodejs-release-el7 oracle-release-el7
  sudo yum update oracle-nodejs-release-el7
  sudo yum install nodejs
  sudo yum install git
  sudo npm install -g grunt-cli
  git clone https://github.com/node-red/node-red.git
  cd node-red
  npm install
  grunt build
  ```

- Firewall
  ```
  sudo firewall-cmd --permanent --add-port=1880/tcp
  sudo systemctl start firewalld
  ```

- Upgrade Node.js
  ```
  node -v  #reviews version
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash    #installs
  nvm install 18
  nvm use 18

  
- Start Node-RED. In the 'node-red' directory:
  ```
  npm start

  ```


