# stop if there's an error (apparently there are gotchas with this)
set -e

# update
sudo apt-get update
sudo apt-get upgrade

# get pip
sudo apt-get -y install python-pip

# get postgres
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
sudo apt-get install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get install postgresql-9.3

# get migration library
sudo apt-get install python-psycopg2
sudo pip install yoyo-migrations

# create db user (what users exist at this point? what are their passwords?)
sudo -u postgres createuser vagrant --createdb

# create database
createdb album_credits

# run migrations
yoyo apply --database postgresql:///album_credits ./migrations
