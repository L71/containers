
## dnsmasq.leases web server

Presenting the dnsmasq lease lists via a rest API using Flask

Required: Python (3.8 tested) with virtualenv:s 

Setup & run for test:

    $ git clone ...  
    $ cd dnsmasq-api
    $ virtualenv flask
    New python executable in flask/bin/python
    Installing setuptools............................done.
    Installing pip...................done.
    $ flask/bin/pip3 install flask
    $ ./index.py

The code expects the dnsmasq.leases file to be available in $PWD/data

## endpoints

`/dnsmasq/api/v1.0/leases` return full lease list

`/dnsmasq/api/v1.0/leases/by-name/<hostname>` return exact match of host names

`/dnsmasq/api/v1.0/leases/by-mac/<mac address>` return substring matched MAC adresses

`/dnsmasq/api/v1.0/leases/by-ip/<ip address>` return substring matched IP addresses


 