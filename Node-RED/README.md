# Run Node-RED on OCI

- Create instance in public subnet, Ubuntu image
- Add 1880 as port in subnet security list

- Run

  ```
  curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  sudo apt-get install -y nodejs build-essential
  sudo apt-get install npm
  sudo npm install -g --unsafe-perm node-red
  ```


sudo npm install -g --unsafe-perm pm2
pm2 start `which node-red` -- -v
