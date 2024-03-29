#!flask/bin/python3
from flask import Flask, jsonify, make_response
from time import asctime, localtime, gmtime
from ipaddress import ip_network
import os

app = Flask(__name__)

leasefile = "data/dnsmasq.leases"

# will match leases with this network
if "MATCH_NETWORKS" in os.environ :
    match_networks = os.environ["MATCH_NETWORKS"]
    cidrs = match_networks.split()
else :
    cidrs =["0.0.0.0/0"]

# network CIDR list to network objects
def cidrs_to_networks(cidrs) :
    networks = []  
    for cidr in cidrs :
        networks.append(ip_network(cidr))
    return networks

# load dnsmasq leases file and parse it
def parse_leases() :
    with open(leasefile, "r") as f :
        lines = f.read()
    leases = []
    for line in lines.splitlines() :
        ( ts, mac, ip, hostname, id ) = line.split()
        ts_localtime = asctime(localtime(int(ts)))
        ts_utctime = asctime(gmtime(int(ts)))

        # match with list of known networks
        for network in networks :
            if ip_network(ip).subnet_of(network) :
                network = network.exploded
                break
            else :
                network = "0.0.0.0/0"

        leases.append( { "ip": ip, "network": network, "mac": mac, "hostname": hostname, "expires": ts, "expires_local": ts_localtime, "expires_utc": ts_utctime } )
    return(leases)

# fail!
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# get full list of leases
@app.route('/dnsmasq/api/v1.0/leases', methods=['GET'])
def index():
    return jsonify(parse_leases())

# by IP address (does substring matching)
@app.route('/dnsmasq/api/v1.0/search/ip/<ipaddress>', methods=['GET'])
def search_ip(ipaddress):
    matches = []
    leases = parse_leases()
    for host in leases :
        if ipaddress in host["ip"] :
            matches.append(host)
    return(jsonify(matches))

# by IP address (exact)
@app.route('/dnsmasq/api/v1.0/exact/ip/<ipaddress>', methods=['GET'])
def exact_ip(ipaddress):
    matches = []
    leases = parse_leases()
    for host in leases :
        if ipaddress == host["ip"] :
            matches.append(host)
    return(jsonify(matches))

# by hostname (substring search, not case sensitive)
@app.route('/dnsmasq/api/v1.0/search/name/<hostname>', methods=['GET'])
def search_name(hostname):
    matches = []
    leases = parse_leases()
    for host in leases :
        if hostname.lower() in host["hostname"].lower() :
            matches.append(host)
    return(jsonify(matches))

# by hostname (exact matching, not case sensitive)
@app.route('/dnsmasq/api/v1.0/exact/name/<hostname>', methods=['GET'])
def exact_name(hostname):
    matches = []
    leases = parse_leases()
    for host in leases :
        if hostname.lower() == host["hostname"].lower() :
            matches.append(host)
    return(jsonify(matches))

# search MAC address (does substring matching, not case sensitive)
# no separate exact function needed; no risk of ambiguity if a full MAC address is asked for.
@app.route('/dnsmasq/api/v1.0/exact/mac/<mac>', methods=['GET'])
def exact_mac(mac):
    matches = []
    leases = parse_leases()
    for host in leases :
        if mac.lower() == host["mac"].lower() :
            matches.append(host)
    return(jsonify(matches))

@app.route('/dnsmasq/api/v1.0/search/mac/<mac>', methods=['GET'])
def search_mac(mac):
    matches = []
    leases = parse_leases()
    for host in leases :
        if mac.lower() in host["mac"].lower() :
            matches.append(host)
    return(jsonify(matches))

if __name__ == '__main__':
    networks = cidrs_to_networks(cidrs)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True  # always pretty-print json
    app.run(host="0.0.0.0")
    
