from bs4 import BeautifulSoup
import csv
import requests

url = "https://en.wikipedia.org/wiki/List_of_high_schools_in_Illinois"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
school_list = []

# List of All counties in Illinois ##
# There has to be an easier way of doing this ##
county_list = ['Adams', 'Alexander', 'Bond', 'Boone', 'Brown', 'Bureau', 'Calhoun',
               'Carroll', 'Cass', 'Champaign', 'Christian', 'Clark', 'Clay', 'Clinton', 'Coles', 'Cook',
               'Crawford', 'Cumberland', 'DeKalb', 'DeWitt', 'Douglas', 'DuPage', 'Edgar', 'Edwards',
               'Effingham', 'Fayette', 'Ford', 'Franklin', 'Fulton', 'Gallatin', 'Greene', 'Grundy',
               'Hamilton', 'Hancock', 'Hardin', 'Henderson', 'Henry', 'Iroquois', 'Jackson', 'Jasper',
               'Jefferson', 'Jersey', 'Jo_Daviess', 'Johnson', 'Kane', 'Kankakee', 'Kendall', 'Knox',
               'LaSalle', 'Lake', 'Lawrence', 'Lee', 'Livingston', 'Logan', 'Macon', 'Macoupin',
               'Madison', 'Marion', 'Marshall', 'Mason', 'Massac', 'McDonough', 'McHenry', 'McLean',
               'Menard', 'Mercer', 'Monroe', 'Montgomery', 'Morgan', 'Ogle', 'Peoria', 'Perry', 'Piatt',
               'Pike', 'Pope', 'Pulaski', 'Putnam', 'Randolph', 'Richland', 'Rock_Island', 'St._Clair',
               'Saline', 'Sangamon', 'Schuyler', 'Scott', 'Shelby', 'Stark', 'Stephenson', 'Tazewell',
               'Union', 'Vermilion', 'Wabash', 'Warren', 'Washington', 'Wayne', 'White', 'Whiteside',
               'Will', 'Williamson', 'Winnebago', 'Woodford']

# Appends _County to the end of each element of the county list
county_list = [element + '_County' for element in county_list]


def schoolsearch():
    for county in county_list:
        county_span = soup.find('span', {'id': county})
        county_ul = county_span.parent.find_next_sibling()
        for item in county_ul.findAll('li'):
            school = item.text.encode('utf-8')
            school_list.extend([school])


def savetofile():
    with open('schools.csv', 'wb') as results:
        wr = csv.writer(results, dialect='excel')
        wr.writerow(['School Name', 'City'])
        for item in school_list:
            wr.writerow([item])
    print 'The list has been printed to schools.csv'


schoolsearch()
savetofile()
