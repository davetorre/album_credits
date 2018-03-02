## Notes
You may have to install git on the vagrant box
```
sudo apt-get install git
```

go.sh creates one user (name: vagrant) with only createdb privledges
To become the all powerful postgres user:
```
sudo -u postgres -i
```

## Where I left off
creating postgres roles
```
create role <name>;


REVOKE CONNECT ON DATABASE your_database FROM PUBLIC;

GRANT CONNECT
ON DATABASE database_name 
TO user_name;


REVOKE ALL
ON ALL TABLES IN SCHEMA public 
FROM PUBLIC;

GRANT SELECT, INSERT, UPDATE, DELETE
ON ALL TABLES IN SCHEMA public 
TO user_name;
```

postgres/vagrant example:
https://wiki.postgresql.org/wiki/PostgreSQL_For_Development_With_Vagrant

