
# Alpine based darkhttpd minimal web server
# 
# serves documents on port 8080 from /htdocs in container, runs server as nobody
#
# docker build -t darkhttpd . 
# docker run --restart=unless-stopped -p 8080:8080 -v /tmp/htdocs:/htdocs --name=darkhttpd darkhttpd:latest

FROM alpine:latest

# install darkhttpd 
RUN apk add darkhttpd \
  && mkdir /htdocs \
  && chmod -x /bin/*

EXPOSE 8080
USER nobody
CMD ["/usr/bin/darkhttpd","/htdocs","--port","8080"]

