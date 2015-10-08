from bs4 import BeautifulSoup
import csv
import requests


school_info = []

## This is for testing purposes, eventually will be a list ##
school_url = "https://en.wikipedia.org/wiki/Christ_Lutheran_High_School"
#school_url = "https://en.wikipedia.org/wiki/Annawan_High_School"
r = requests.get(school_url)
soup = BeautifulSoup(r.content, "html.parser")

## Find for search items
name = soup.find('th', {'class' : 'fn org'})
address = soup.find('span', {'class': 'street-address'})
city = soup.find('span', {'class' : 'locality'})
state = soup.find('span', {'class' : 'region'})
zip = soup.find('span', {'class' : 'postal-code'})
geo = soup.find('span', {'class' : 'geo'})



def schoolName():
	if name:
		school_name = name
		school_name = school_name.text.encode('utf-8')
		school_info.extend([school_name])
	else:
		school_info.extend(["None found"])

#Needs check to see if element is there	
def schoolAddress():
	if address:
		school_address = address
		school_address = school_address.text.encode('utf-8')
		school_info.extend([school_address])
	else:
		school_info.extend(["None found"])
	
def schoolCity():
	if city:
		school_city = city
		school_city = school_city.text.encode('utf-8')
		school_info.extend([school_city])
	else:
		school_info.extend(["None found"])
	
def schoolState():
	if state:
		school_state = state
		school_state = school_state.text.encode('utf-8')
		school_info.extend([school_state])
	else:
		school_info.extend(["None found"])

#Needs check to see if element is there
def schoolZip():
	if zip:
		school_zip = zip
		school_zip = school_zip.text.encode('utf-8')
		school_info.extend([school_zip])
	else:
		school_info.extend(["None found"])
		

#Needs check to see if element is there	
def schoolGeo():
	if geo:
		school_geo = geo
		school_geo = school_geo.text.encode('utf-8')
		school_geo = school_geo.split(";")
		lat = school_geo[0]
		long = school_geo[1]
		school_info.extend([lat])
		school_info.extend([long])
	else:
		school_info.extend(["None found"])
		

def saveToFile():
	with open('schoolinfo.csv', 'wb') as results:
		wr = csv.writer(results, dialect = 'excel')
		wr.writerow(['School Name', 'Address', 'City', 'State', 'Zip', 'Lat', 'Long'])
		wr.writerow(school_info)
	print 'The list has been printed to schoolinfo.csv'
	
		
	
schoolName()
schoolAddress()
schoolCity()
schoolState()
schoolZip()
schoolGeo()
saveToFile()