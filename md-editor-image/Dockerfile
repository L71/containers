
# Container to serve up the markdown editor from
# https://github.com/jbt/markdown-editor

FROM alpine:latest

# tar file of https://github.com/jbt/markdown-editor
# files will be unpacked into /markdown-editor/
ADD markdown-editor.tgz /

# add darkhttpd and also disable pretty much any other command
# in the image
RUN apk add darkhttpd \
  && chmod -x /bin/*

USER nobody
EXPOSE 8080

CMD [ "/usr/bin/darkhttpd", "/markdown-editor", "--port", "8080" ]
