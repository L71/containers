
### squid-alpine

This is a bare-minimum Alpine Linux image with Squid proxy installed.

Built for and only tested with the pihole-squid thingie in this repository
on 32bit ARM (like 32bit RaspberryPiOS) which the Ubuntu/squid image didn't support.

Build:
    docker build -t squid-alpine:latest .

Then adjust the pihole-squid `docker-compose.yml` file to use it.

