# Group Name :- Big Data Learners
# Teammates  :- Mitul Kamdar
# Teammates  :- Vikram Jaygude
# Date       :- 12/11/ 2018

# Import libraries
from bs4 import BeautifulSoup                     #Python package for parsing HTML and XML documents
import requests                                   #Python library  for handling requests and URL HANDLING
import pymysql                                    #Python library for handling database


# Make Database Connections
# User is CrawlPlaystore
# Password is CrawlPlaystore
# Server is 10.103.92.251 in Marshall university
# Name of the database is crawlplaystore
connection = pymysql.connect(user='crawlplaystore', password='crawlplaystore', host='10.103.92.251', database='crawlplaystore')
# Create a cursor which are bound to the connection of entire lifetime of database session
r = connection.cursor()

#  Create variables to store collected data
def attrib(Application_Rank, Application_Name, Hyperlink):
    r.execute("INSERT INTO Website_App_Brain(Application_Rank,Application_Name,Hyperlink) values(%s,%s,%s)", (Application_Rank, Application_Name, Hyperlink))      # Query to insert data into database Google_Playstore_Data
    r.connection.commit()                      # This method sends a COMMIT statement to the MySQL server, committing the current transaction.

source = requests.get('https://www.appbrain.com/stats/google-play-rankings').text              #To get the page source of AppBrain page source
soup = BeautifulSoup(source, 'lxml')                                                           #Parse the contents of page source of AppBrain placed in source and store the contents in soup

for s in soup.findAll('div', {'class': 'data-table-container topmargin-m'}):          # for loop to iterate with division whoose class is data-table-container topmargin-m
    for v in s.table.tbody.findAll('tr'):                                             # for loop to iterate with table row
        Application_Rank = v.td.text                                                  # Stores the Rank in variable  Application_Name
        #category = v.td.a.text
        #ratings =  v.td.a.text
        for u in v.findAll('td', {'class': 'ranking-app-cell'}):                      # for loop to iterate with table data whoose class is ranking-app-cell
            Application_Name = u.a.text                                               # Stores the application name in variable  Application_Name
            Hyperlink = u.a.get('href')                                               #Stores the hyperlink in variable Hyperlink
            attrib(Application_Rank, Application_Name, Hyperlink)                     #Calls and store Application_Name, Hyperlink, DocumentID in database
            print(Application_Rank, 'Name:', Application_Name, 'href:', Hyperlink)     # Print the content on console

      #category = v.a.text
    #print(s.prettify())

    connection.close()                   # Close database connection
    r.close()                            # Cursor close