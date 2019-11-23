sudo dnf -y update
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo groupadd docker
sudo usermod -aG docker $USER
sudo dnf -y install --nobest docker-ce
sudo systemctl enable docker
sudo systemctl start docker
curl -s https://api.github.com/repos/docker/compose/releases/latest \
  | grep browser_download_url \
  | grep docker-compose-Linux-x86_64 \
  | cut -d '"' -f 4 \
  | wget -qi -
sudo chmod +x docker-compose-Linux-x86_64
sudo mv docker-compose-Linux-x86_64 /usr/local/bin/docker-compose