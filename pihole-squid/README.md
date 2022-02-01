# pihole + squid deployment

This docker-compose setup provides a squid proxy paired with a pihole DNS blocker, intended to act as a network filter for web browsers without tinkering with the DNS for an entire network.

The squid config file is in etc-squid/squid.conf and points the squid proxy DNS to the pihole container. 


The pihole management interface is exposed on port 80. \
The squid proxy can be accessed by browser clients on port 8080.

