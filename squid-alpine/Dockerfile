# Alpine-based squid container
#  build:
#  $ docker build -t squid-alpine:latest .

FROM alpine:3

VOLUME /run
VOLUME /sys/fs/cgroup

# install openrc init system and squid, add squid service,
# then make init not try to launch any ttyN.
RUN apk add openrc squid \
  && rc-update add squid \
  && sed -i 's|^tty.*|# &|' /etc/inittab

COPY squid.conf /etc/squid/squid.conf

EXPOSE 3128

CMD /sbin/init
