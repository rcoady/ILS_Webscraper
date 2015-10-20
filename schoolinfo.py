from bs4 import BeautifulSoup
import csv
import requests

school_info = []

# This is for testing purposes, eventually will be a list
# school_url = "https://en.wikipedia.org/wiki/Christ_Lutheran_High_School"
school_url = "https://en.wikipedia.org/wiki/Annawan_High_School"
r = requests.get(school_url)
soup = BeautifulSoup(r.content, "html.parser")

# Find for search items
name = soup.find('th', {'class': 'fn org'})
address = soup.find('span', {'class': 'street-address'})
city = soup.find('span', {'class': 'locality'})
state = soup.find('span', {'class': 'region'})
zip_code = soup.find('span', {'class': 'postal-code'})
geo = soup.find('span', {'class': 'geo'})


def schoolname():
    if name:
        school_name = name
        school_name = school_name.text.encode('utf-8')
        school_info.extend([school_name])
    else:
        school_info.extend(["None found"])


# Needs check to see if element is there
def schooladdress():
    if address:
        school_address = address
        school_address = school_address.text.encode('utf-8')
        school_info.extend([school_address])
    else:
        school_info.extend(["None found"])


def schoolcity():
    if city:
        school_city = city
        school_city = school_city.text.encode('utf-8')
        school_info.extend([school_city])
    else:
        school_info.extend(["None found"])


def schoolstate():
    if state:
        school_state = state
        school_state = school_state.text.encode('utf-8')
        school_info.extend([school_state])
    else:
        school_info.extend(["None found"])


# Needs check to see if element is there
def schoolzip():
    if zip_code:
        school_zip = zip_code
        school_zip = school_zip.text.encode('utf-8')
        school_info.extend([school_zip])
    else:
        school_info.extend(["None found"])


# Needs check to see if element is there
def schoolgeo():
    if geo:
        school_geo = geo
        school_geo = school_geo.text.encode('utf-8')
        school_geo = school_geo.split(";")
        latitude = school_geo[0]
        longitude = school_geo[1]
        school_info.extend([latitude])
        school_info.extend([longitude])
    else:
        school_info.extend(["None found"])


def savetofile():
    with open('schoolinfo.csv', 'wb') as results:
        wr = csv.writer(results, dialect='excel')
        wr.writerow(['School Name', 'Address', 'City', 'State', 'Zip', 'Lat', 'Long'])
        wr.writerow(school_info)
    print 'The list has been printed to schoolinfo.csv'


schoolname()
schooladdress()
schoolcity()
schoolstate()
schoolzip()
schoolgeo()
savetofile()
