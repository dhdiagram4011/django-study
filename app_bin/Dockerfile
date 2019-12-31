FROM ubuntu:18.04
MAINTAINER dhdiagram<dhdiagram@gmail.com>
CMD mkdir /var/www/django
add ./django-app.tar /var/www/django
RUN apt-get update -y
RUN apt-get install -y nginx
RUN apt-get install -y vim
RUN apt-get install -y python3-dev python3-venv python3-pip libmysqlclient-dev python-dev libssl-dev libffi-dev libxml2-dev
CMD sudo useradd -b /home -m -s /bin/bash django
CMD sudo usermod -a -G www-data django
CMD usermod -a -G www-data ubuntu
CMD mkdir /var/www/django && cd /var/www/django && tar xvf django-app.tar
CMD cd /var/www/django
CMD sudo python3 -m venv /var/www/django/venv
CMD sudo chown -R django:www-data /var/www/django
CMD sudo chmod -R g+w /var/www/django
CMD pip install -r /var/www/django/requirements.txt
CMD pip install uwsgi
RUN pip3 install pymysql
RUN pip3 install mysqlclient
CMD sudo systemctl enable uwsgi && systemctl enable uwsgi && systemctl restart nginx
EXPOSE 8000
EXPOSE 3306


