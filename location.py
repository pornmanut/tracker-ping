import os
import sys
import re

import requests
import time
import urllib.request
from bs4 import BeautifulSoup

args = sys.argv
if len(args) <= 1:
    print("need more arugment")
    sys.exit()


target = args[1]
ip4 = []
table = []
if os.path.exists(target):
    with open(target) as fo:
        print("reading from "+fo.name)
        for line in fo:
            mask = re.search('(?:[0-9]{1,3}\.){3}[0-9]{1,3}', line)
            if mask:
                ip4.append(line[mask.start(): mask.end()])
# i don't know how to handle when not response
# next version we will find out
# for ip in ip4:
    # page = requests.get('https://checkip.thaiware.com/?ip='+ip)


for ip in ip4:
    url = 'https://checkip.thaiware.com/?ip='+ip
    print("reading "+url)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    location = []

    for link in soup.find_all('td', {"class": "detail right_col"}):
        location.append(link.get_text())
    print("location " + str(location))
    table.append(location)

result = target+'_table'
print("Writing to "+result)
with open(result, 'w') as fo:
    cnt = 0  # we don't need target
    for ta in table:
        if cnt == 0:
            cnt = 1
            continue
        s = ' '
        line = s.join(ta) + '\n'
        fo.write(line)

cnt = 0  # we don't need target
store = []
for ta in table:
    if cnt == 0:
        cnt = 1
        continue

    if str(ta[5]) == '0' and str(ta[6]) == '0':
        continue

    line = ta[5]+' '+ta[6] + '\n'
    store.append(line)

print(str(store))
position = []

for word in store:
    if word not in position:
        position.append(word)

result = target+'_location'
print("Writing to "+result)

with open(result, 'w') as fo:
    for p in position:
        fo.write(p)
