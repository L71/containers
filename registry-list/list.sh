#!/bin/bash

# settings: takes registry URL in variable "registry" as input.
# only one parameter.
# echo ${QUERY_STRING##*=}

# env
# echo

registry=${QUERY_STRING}

if [ -z "${registry}" ]; then
	echo "missing parameters."
	exit 0
fi

echo "Content-type: text/plain"
echo
echo
figlet images
echo
echo "registry: ${registry}"
echo

/usr/local/bin/registry_list.sh ${registry}


