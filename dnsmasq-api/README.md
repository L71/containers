
## dnsmasq.leases web server

Presenting the dnsmasq lease lists via a rest API using Flask

NOTE about running Flask this way: https://flask.palletsprojects.com/en/2.1.x/cli/#run-the-development-server 

Required: Python3 (3.8 and 3.10 used here) with virtualenv:s 

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

`/dnsmasq/api/v1.0/[search|exact]/[name|ip|mac]/<searchstring>` returns either a substring match or the exact match for `searchstring` in hostname, ip address or MAC address of the DHCP client. In all cases matching is done ignoring case and returns lower-case results.

 