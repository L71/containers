FROM alpine:latest

# packages: 
# lighttpd = web server
# jq, curl needed for registry list script
# figlet just for c00l asc11 art =) 

RUN apk add lighttpd nano bash jq curl figlet \
  && mkdir -p /var/www/localhost/cgi-bin \
  && mkdir -p /usr/local/share/ca-certificates

COPY lighttpd.conf /etc/lighttpd/lighttpd.conf
COPY mod_cgi.conf /etc/lighttpd/mod_cgi.conf
COPY registry_list.sh /usr/local/bin/
COPY list.sh /var/www/localhost/cgi-bin/

# local CA trust cert (not in GIT repo)
COPY home_CA.crt /usr/local/share/ca-certificates/

RUN update-ca-certificates

# launch lighttpd, foreground
CMD /usr/sbin/lighttpd -D -f /etc/lighttpd/lighttpd.conf
