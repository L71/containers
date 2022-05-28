
### dnsmasq.leases web server

Presenting the dnsmasq lease lists via a rest API using Flask

Required: Python (3.8 tested) with virtualenv:s 

Setup:

    $ git clone ...  
    $ cd dnsmasq-api
    $ virtualenv flask
    New python executable in flask/bin/python
    Installing setuptools............................done.
    Installing pip...................done.
    $ flask/bin/pip3 install flask

The code expects the dnsmasq.leases file to be available in $PWD/data
