
# Docker Registry list web app

This container runs a web server (or, actually, just a CGI script) that takes
one URL as it's parameter - the URL to the registry to list.

It assumes that no authentication is necessary to get the information from
the registry.

Example: 

`http://server:8080/cgi-bin/list.sh?https://registry:5000`

Output:

     _                                 
    (_)_ __ ___   __ _  __ _  ___  ___ 
    | | '_ ` _ \ / _` |/ _` |/ _ \/ __|
    | | | | | | | (_| | (_| |  __/\__ \
    |_|_| |_| |_|\__,_|\__, |\___||___/
                       |___/           
    
    registry: https://registry:5000

    alpine-baseimage
      registry:5000/alpine-baseimage:3.14.2-aarch64-108
      registry:5000/alpine-baseimage:3.14.2-x86_64-108
      registry:5000/alpine-baseimage:3.14.3-aarch64-109
      registry:5000/alpine-baseimage:3.14.3-aarch64-110


Originally built on Alpine 3.15 and made to list the contents of
a local registry running the `docker.io/registry:2` image with no
authentication required for access.

No particular cleanup of parameters is done. Do **NOT** use this on
untrusted networks! 
