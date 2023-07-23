#/bin/bash

curl -LO https://github.com/prometheus/prometheus/releases/download/v2.38.0/prometheus-2.38.0.linux-amd64.tar.gz

tar -xvf prometheus-2.38.0.linux-amd64.tar.gz

sudo mv prometheus-2.38.0.linux-amd64/prometheus /usr/local/bin/prometheus
sudo mv prometheus-2.38.0.linux-amd64/promtool /usr/local/bin/promtool

sudo mkdir /etc/prometheus

sudo mv prometheus-2.38.0.linux-amd64/prometheus.yml /etc/prometheus/prometheus.yml
sudo mv prometheus-2.38.0.linux-amd64/consoles /etc/prometheus
sudo mv prometheus-2.38.0.linux-amd64/console_libraries /etc/prometheus

# directory where prometheus will store data
sudo mkdir /var/lib/prometheus

sudo addgroup --system prometheus
sudo adduser --shell /sbin/nologin --system --group prometheus

# ATTENTION: complete this file! 
sudo vim /etc/systemd/system/prometheus.service


# give right permissions to prometheus user
sudo chown -R prometheus:prometheus /var/log/prometheus
sudo chown -R prometheus:prometheus /etc/prometheus
sudo chown -R prometheus:prometheus /var/lib/prometheus
sudo chown -R prometheus:prometheus /usr/local/bin/prometheus
sudo chown -R prometheus:prometheus /usr/local/bin/promtool

sudo systemctl daemon-reload
sudo systemctl start prometheus
sudo systemctl enable prometheus

# in case of debugging, run $ sudo journalctl -u prometheus