# docker build -t dnsmasq-api -f Dockerfile .
# 
FROM python:3.8-alpine
# install stuff
RUN apk add -U py3-virtualenv \ 
    && virtualenv flask \
    && flask/bin/pip3 install flask 

VOLUME /data

EXPOSE 5000

COPY index.py /

USER 2001:2001

CMD /index.py
