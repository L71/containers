#!/bin/bash

# script to query a docker registry for the image list
# Args: <https://URL to registry:5000>

[ -z "$1" ] && echo "usage: $0 https://my.regist.ry:5000" && exit 0

# get image list & strip any trailing / from arg1.
URL=${1%/}
images=$( curl --insecure -s -X GET "${URL}/v2/_catalog" | jq -r '.repositories | .[]' | sort )

for image in $images ; do
    tags=$( curl --insecure -s -X GET "${URL}/v2/${image}/tags/list" | jq -r '.tags | .[]' | sort )
    if [ $tags != "" ]; then
        echo "${image}"
        for tag in $tags ; do
            echo "  ${URL#*//}/$image:$tag"
        done
        echo
    fi
done

