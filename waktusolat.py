import requests
import xml.etree.ElementTree as ET
import click

@click.command()
@click.argument('zone')
def waktu_solat(zone):
    response = requests.get('http://www2.e-solat.gov.my/xml/today/?zon='+str(zone))
    html = response.content

    root = ET.fromstring(html)

    for channel in root.iter('channel'):
        kawasan = channel.find('link').text

    jadual = []

    for item in root.iter('item'):
        title = item[0].text
        desc = item[1].text
        waktu = [title, desc]
        jadual.append(waktu)

    print "Waktu solat bagi kawasan %s" % kawasan
    for solat, masa in jadual:
        print solat, masa


if '__main__' == __name__:
    waktu_solat()
