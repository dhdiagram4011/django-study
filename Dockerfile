FROM python:3.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python-dev python3-dev python3-pip libmysqlclient wget git nginx \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /var/www/django
RUN mkdir /var/www/django/runs
RUN mkdir /var/www/django/logs
RUN mkdir /var/www/django/ini

RUN git clone https://github.com/dhdiagram4011/Airline-Ticketing-System.git
COPY /Users/Airline-Ticketing-System/Airline-Ticketing-System/requirements.txt ./
COPY /Users/Airline-Ticketing-System/uwsgi.ini /var/www/django/uwsgi.ini
RUN pip3 install -r requirements.txt
RUN useradd -b /home -m -s /bin/bash django
RUN usermod -a -G www-data django
RUN chwon -R django:www-data /var/www/django
RUN chown -R g+w /var/www/dango
RUN pip3 install uwsgi
COPY /Users/Airline-Ticketing-System/uwsgi.service /etc/systemd/system/uwsgi.service
RUN systemctl enable uwsgi && systemctl start uswgi
COPY /Users/Airline-Ticketing-System/default /etc/nginx/sites-available/default
RUN systemctl enable nginx && systemctl start nginx

EXPOSE 8000
EXPOSE 3306

