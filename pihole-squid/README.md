### Pi-hole + Squid proxy deployment

This docker-compose setup provides a squid proxy paired with a Pi-hole DNS blocker, intended to act as a network filter for web browsers without tinkering with the DNS for an entire network.

The squid config file is in `etc-squid/squid.conf` and points the squid proxy DNS to the Pi-hole container. 

The Pi-hole web management interface is exposed on port 8128. \
The squid proxy can be accessed by browser clients on the squid default port 3128.

By default there is a random password for the pihole admin login generated at deploy time, you can reset it by running the pihole password change command in the Pi-hole container after deploying it:

`docker exec -it pihole pihole -a -p`

The password can also be set directly in the docker-compose.yml file.

The deployment is using the network 10.55.55.0/29 internally. If this is changed remember to update the squid.conf file to point to the new IP of the Pi-hole container.

### containers

The deployment will by default use these containers from Docker Hub:

`pihole/pihole:latest` \
`ubuntu/squid:latest` 

This should work in most cases. The Ubuntu Squid container has no 32bit ARM support so if you want to run this on for example 32bit RaspberryPiOS you need to find another squid container.
