from bs4 import BeautifulSoup
import csv
import requests

# Website that is being scraped
url = "https://en.wikipedia.org/wiki/List_of_high_schools_in_Illinois"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
county_list = []
school_list = []


# Goes through the page and pulls out all of the county Id's


def countysearch():
    for tag in soup.findAll('span', id =lambda x: x and x.endswith('_County')):
        tag = tag.get('id')
        tag = tag.encode('utf-8')
        county_list.extend([tag])

# For each county it pulls out each school name and city


def schoolsearch():
    for county in county_list:
        county_span = soup.find('span', {'id': county})
        county_ul = county_span.parent.find_next_sibling()
        for item in county_ul.findAll('li'):
            school = item.text.encode('utf-8')
            school = school.split(',')
            temp_list = []
            school_name = school[0]
            temp_list.extend([school_name])

            # Accounts for schools that do not have a city listed
            try:
                city = school[1].strip()
                temp_list.extend([city])
            except IndexError:
                temp_list.extend(["No city listed"])
            school_list.extend([temp_list])

# Saves data to a csv file with headers


def savetofile():
    with open('schools.csv', 'wb') as results:
        writer = csv.writer(results)
        writer.writerow(['School Name', 'City'])
        writer.writerows(school_list)
    print 'The list has been printed to schools.csv'

countysearch()
schoolsearch()
savetofile()
