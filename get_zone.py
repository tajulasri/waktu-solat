import requests
import re
from bs4 import BeautifulSoup
import json

def get_zone(page):
    base_url = 'http://www2.e-solat.gov.my/zon-waktusolat.php?PageNo=' + str(page)
    text = requests.request('GET', base_url).content

    soup = BeautifulSoup(text, 'html.parser')
    return soup.findAll('td', class_='tabletext', attrs={'valign': 'top', 'align': 'left'})

pattern = re.compile(r'\w{2,3}\d{1,2}',re.S|re.I)
zones = list()

for page in range(1,4):
    zone = get_zone(page)
    for code in zone:
        match = re.search(pattern,code.text)
        if match:
            zones.append(match.group(0))


with open('zone.dump','a+') as file:
    for zone in zones:
        file.writelines(zone+"\n")