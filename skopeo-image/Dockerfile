FROM alpine:3
RUN apk add curl skopeo

# CA certs - copy file and update cert DB
COPY *.crt /usr/local/share/ca-certificates/
RUN update-ca-certificates

# default: run with --help when no other argument specified 
CMD ["--help"]
ENTRYPOINT ["/usr/bin/skopeo"]
