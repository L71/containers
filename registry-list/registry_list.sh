#!/bin/bash

# script to query a docker registry for the image list
# Args: <https://URL to registry:5000>

[ -z "$1" ] && echo "usage: $0 https://my.regist.ry:5000" && exit 0

# get image list & strip any trailing / from arg1.
URL=${1%/}
images=$( curl --insecure -s -X GET "${URL}/v2/_catalog" | jq -r '.repositories | .[]' | sort )

for image in $images ; do
    # if jq can extract a tag list then print this. if not, skip this image.
    curl --insecure -s -X GET "${URL}/v2/${image}/tags/list" | jq -r '.tags | .[]' 1>/tmp/taglist 2>/dev/null
    rc=$?
    if [ $rc == 0 ]; then
	tags=$( cat /tmp/taglist | sort )
        echo "${image}"
        for tag in $tags ; do
            echo "  ${URL#*//}/$image:$tag"
        done
        echo
    fi
done
