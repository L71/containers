### skopeo-alpine

Alpine image that just provides the skopeo command, for use where it is not easily available otherwise.

Any custom CA trust certificate .crt file found in the build directory will be included in the image. 

    $ docker build -t skopeo-alpine -f Dockerfile.Alpine .
    $ docker run --rm skopeo-alpine inspect docker://registry-server:port/some-image:tag


