#!/bin/sh

# include parse_yaml function
. settings/parse_yaml.sh

# read yaml file
eval $(parse_yaml settings/config.yml "config_")

# creating virtual envs
sudo -u ${USERNAME} virtualenv env-shopify
sudo -u ${USERNAME} virtualenv env-shopify-auth

#installing requirments
sudo -u ${USERNAME} env-shopify/bin/pip install -r shopify/requirements.pip
sudo -u ${USERNAME} env-shopify-auth/bin/pip install -r shopify_auth/requirements.pip

# removing old containers
docker stop shopify_db shopify_auth_db
docker rm shopify_db shopify_auth_db


# creating database
docker run --name shopify_db -e POSTGRES_PASSWORD=$config_shopify_database_password \
-e POSTGRES_USER=$config_shopify_database_user -e POSTGRES_DB=$config_shopify_database_name \
-p $config_shopify_database_port:5432 -d postgres

docker run --name shopify_auth_db -e POSTGRES_PASSWORD=$config_shopify_auth_database_password \
-e POSTGRES_USER=$config_shopify_auth_database_user -e POSTGRES_DB=$config_shopify_auth_database_name \
-p $config_shopify_auth_database_port:5432 -d postgres

sleep 5

# creating migrations
sudo -u ${USERNAME} env-shopify/bin/python shopify/manage.py migrate
sudo -u ${USERNAME} env-shopify-auth/bin/python shopify_auth/manage.py migrate

# running servres in backround
sudo -u ${USERNAME} env-shopify/bin/python shopify/manage.py runserver 8000&
sudo -u ${USERNAME} env-shopify-auth/bin/python shopify_auth/manage.py runserver 8080&