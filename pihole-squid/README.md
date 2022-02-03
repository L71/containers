# Pi-hole + Squid proxy deployment

This docker-compose setup provides a squid proxy paired with a Pi-hole DNS blocker, intended to act as a network filter for web browsers without tinkering with the DNS for an entire network.

The squid config file is in `etc-squid/squid.conf` and points the squid proxy DNS to the Pi-hole container. 

The Pi-hole web management interface is exposed on port 8128. \
The squid proxy can be accessed by browser clients on the squid default port 3128.

There is a random password for the pihole admin login generated at deploy time, you can reset it
by running the pihole password change command in the Pi-hole container:

    docker exec -it pihole pihole -a -p


