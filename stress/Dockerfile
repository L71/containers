FROM debian:buster-slim
RUN apt-get update
RUN apt-get install -y stress
USER nobody

# default: Use up one CPU and run for 300s/5min.
# args to the container will replace these defaults
# info: see stress(1) or run the container with --help.
CMD ["-c", "1", "-t", "300"]
ENTRYPOINT ["/usr/bin/stress"]

