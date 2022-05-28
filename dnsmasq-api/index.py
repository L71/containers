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

    leases = {}  
    for line in lines.splitlines() :
        ( ts, mac, ip, hostname, id ) = line.split()
        ts_localtime = asctime(localtime(int(ts)))
        ts_utctime = asctime(gmtime(int(ts)))

        leases[ip] = { "ip": ip, "mac": mac, "hostname": hostname, "expires": ts, "expires_local": ts_localtime, "expires_utc": ts_utctime } 

        for network in networks :
            if ip_network(ip).subnet_of(network) :
                leases[ip]["network"] = network.exploded
                break
            else :
                leases[ip]["network"] = "0.0.0.0/0"

    return(leases)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# get full list
@app.route('/dnsmasq/api/v1.0/leases', methods=['GET'])
def index():
    return jsonify(parse_leases())

# by IP address
@app.route('/dnsmasq/api/v1.0/leases/by-ip/<ipaddress>', methods=['GET'])
def by_ip(ipaddress):
    leases = parse_leases()
    if ipaddress in leases :
        return(jsonify(leases[ipaddress]))
    else :
        return make_response(jsonify({'error': 'Not found'}), 404)

# by hostname
@app.route('/dnsmasq/api/v1.0/leases/by-name/<hostname>', methods=['GET'])
def by_name(hostname):
    matches = []
    leases = parse_leases()
    for ip, data in leases.items() :
        # print(ip, data)
        if data["hostname"] == hostname :
            matches.append(data)

    if matches != [] :
        return(jsonify(matches))
    else :
        return make_response(jsonify({'error': 'Not found'}), 404)

# by MAC address
@app.route('/dnsmasq/api/v1.0/leases/by-mac/<mac>', methods=['GET'])
def by_mac(mac):
    leases = parse_leases()
    for ip, data in leases.items() :
        # print(ip, data)
        if data["mac"] == mac :
            return(jsonify(data))
    # falltrough if not found
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    networks = cidrs_to_networks(cidrs)
    # print(networks)
    app.run(debug=True, host="0.0.0.0")
    
