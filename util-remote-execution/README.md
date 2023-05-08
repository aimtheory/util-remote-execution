# Remote Execution Utility
This is a simple script that will accept a list of server IP addresses or hostnames and execute a script on each of them remotely.

## Usage
```
usage: main.py [-h] -u USERNAME -k KEYFILE [-s SERVERFILE] [-d DOMAIN] [-r START STOP] [-sd SUBDOMAIN]

Upgrade remote Linux servers via SSH

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        SSH username
  -k KEYFILE, --keyfile KEYFILE
                        SSH private key file path
  -s SERVERFILE, --serverfile SERVERFILE
                        Server list file path
  -d DOMAIN, --domain DOMAIN
                        Domain name
  -r START STOP, --range START STOP
                        Range of integer values as hostnames
  -sd SUBDOMAIN, --subdomain SUBDOMAIN
                        Subdomain name
```