#!flask/bin/python3
from flask import Flask, jsonify, make_response
from time import asctime, localtime, gmtime
from ipaddress import ip_network

app = Flask(__name__)

leasefile = "data/dnsmasq.leases"

# will match leases with this network
cidrs =["192.168.0.0/24", "192.168.1.0/24", "192.168.2.0/24"]

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
@app.route('/dnsmasq/api/v1.0/leases/by-ip/<ipaddress>', methods=['GET'])
def by_ip(ipaddress):
    matches = []
    leases = parse_leases()
    for host in leases :
        if ipaddress in host["ip"] :
            matches.append(host)
    return(jsonify(matches))

# by hostname (exact matching, not case sensitive)
@app.route('/dnsmasq/api/v1.0/leases/by-name/<hostname>', methods=['GET'])
def by_name(hostname):
    matches = []
    leases = parse_leases()
    for host in leases :
        if hostname.lower() == host["hostname"].lower() :
            matches.append(host)
    return(jsonify(matches))

# by MAC address (does substring matching)
@app.route('/dnsmasq/api/v1.0/leases/by-mac/<mac>', methods=['GET'])
def by_mac(mac):
    matches = []
    leases = parse_leases()
    for host in leases :
        if mac in host["mac"] :
            matches.append(host)
    return(jsonify(matches))

if __name__ == '__main__':
    networks = cidrs_to_networks(cidrs)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True  # always pretty-print json
    app.run(host="0.0.0.0")
    
