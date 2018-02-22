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
```
