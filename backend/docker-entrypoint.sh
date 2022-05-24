#!/bin/sh
apk update

#The following is needed for mysqlclient
apk add mariadb-dev
apk add build-base
apk add mariadb-client

#The following is needed for djoser
apk add libffi-dev

#Install pip and requirements
apk add --update py3-pip
pip install pipenv
pipenv install --system

#Wait for DB to activate
./wait-for.sh db:3306

#Create the main database if it does not exist
mysql -h db -u root -p${DATABASE_PASSWORD} -e "CREATE DATABASE IF NOT EXISTS robots"

#Create the tables. Django can handle exceptions if they are already created
python manage.py makemigrations && python manage.py migrate

#Change the sql document to handle already created database entries if it can't.  Import the mock data.
sed -e 's/insert into/insert ignore into/gI' < ${DATABASE_DATA} | mysql -h db -u root -p${DATABASE_PASSWORD} robots

#Create the superuser.  Flag and continue if unable
python manage.py createsuperuser --noinput || echo 'cannot create admin user'

#Start the server
python manage.py runserver 0.0.0.0:8000