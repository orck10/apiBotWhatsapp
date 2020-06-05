from ubuntu

RUN apt-get update -y
RUN apt-get install apache2 -y
RUN apt-get install libapache2-mod-wsgi -y

ADD 000-default.conf /etc/apache2/sites-available/000-default.conf