# start from this file if you want to use only one command

import os
import sys

# use for create dir with time
from datetime import datetime

# insert mutiple host to ping at once
hosts = ['imgru.com', 'yandex.ru']
# hosts = ['google.com']

for host in hosts:

    # change to from that we cane read and can create
    time = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    # cut .com out use only domain
    hostname = host.split('.')[0] + '/' + str(time)
    directory = host + '/' + str(time)

    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Create new directory: /", directory)

    print('ping -c 6 ' + host + " > " + directory + '/ping.txt')
    os.system('ping -c 6 ' + host + " > " + directory + '/ping.txt')

    print("traceroute -I "+host + " >> " + directory + "/traceroute.txt")
    os.system("traceroute -I "+host + " >> " + directory + "/traceroute.txt")

    print("Create " + directory + " Successfully")

    print("Start Scarping")
    os.system('python3 location.py ' + directory + "/traceroute.txt")

    print("Ploting Map")
    os.system('python3 map.py ' + directory + "/traceroute.txt_location")
