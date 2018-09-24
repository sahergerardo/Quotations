#!/bin/bash
domain_name=`cat /tmp/domain_name`
sudo /opt/bitnami/ctlscript.sh stop
sudo lego --accept-tos --email="doesntwork@atall.com" --domains="$domain_name" --path="/etc/lego" run
sudo mv /opt/bitnami/apache2/conf/server.crt /opt/bitnami/apache2/conf/server.crt.old
sudo mv /opt/bitnami/apache2/conf/server.key /opt/bitnami/apache2/conf/server.key.old
sudo mv /opt/bitnami/apache2/conf/server.csr /opt/bitnami/apache2/conf/server.csr.old
sudo ln -s "/etc/lego/certificates/$domain_name.key" /opt/bitnami/apache2/conf/server.key
sudo ln -s "/etc/lego/certificates/$domain_name.crt" /opt/bitnami/apache2/conf/server.crt
sudo chown root:root /opt/bitnami/apache2/conf/server*
sudo chmod 600 /opt/bitnami/apache2/conf/server*
sudo /opt/bitnami/ctlscript.sh start
sed -i -e  "s/domainplaceholder/$domain_name/g" /home/bitnami/renew-certificate.sh
sudo cp /home/bitnami/renew-certificate.sh /etc/lego/renew-certificate.sh
sudo chmod +x /etc/lego/renew-certificate.sh
