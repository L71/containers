
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

## output format

The return result (when successful) will be a list of DHCP lease entries. No result found will return an empty list: `[]`

    [
        {
            "expires": "1659894551",
            "expires_local": "Sun Aug  7 19:49:11 2022",
            "expires_utc": "Sun Aug  7 17:49:11 2022",
            "hostname": "hostname",
            "ip": "192.168.0.100",
            "mac": "XX:XX:XX:XX:XX:XX",
            "network": "192.168.0.0/24"
        }
        {
            ... next entry (if any)
        }
    ]

Trying to access a non-existing endpoint will return a not found error on the output and HTTP status 404.

    {
        "error": "Not found"
    }

