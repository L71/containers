
## dnsmasq.leases web server

Presenting the dnsmasq lease lists via a rest API using Flask

NOTE about running Flask this way: https://flask.palletsprojects.com/en/2.1.x/cli/#run-the-development-server 

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

----

## endpoints

`/dnsmasq/api/v1.0/leases` return full lease list

`/dnsmasq/api/v1.0/search/name/<hostname>` return exact match of host names

`/dnsmasq/api/v1.0/exact/name/<hostname>` search host name

`/dnsmasq/api/v1.0/search/mac/<mac address>` return substring matched MAC adresses

`/dnsmasq/api/v1.0/search/ip/<ip address>` return substring matched IP addresses

`/dnsmasq/api/v1.0/exact/ip/<ip address>` return exact IP match

 