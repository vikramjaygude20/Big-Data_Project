# Group Name :- Big Data Learners
# Teammates  :- Mitul Kamdar
# Teammates  :- Vikram Jaygude
# Date       :- 12/11/ 2018

from bs4 import BeautifulSoup
import requests
import pymysql


connection = pymysql.connect(user='crawlplaystore', password='crawlplaystore', host='10.103.92.251', database='crawlplaystore')
# Create a cursor which are bound to the connection of entire lifetime of database session
r = connection.cursor()

def attrib(Application_Name, Hyperlink):
    r.execute("INSERT INTO FossBytes_Data(Application_Name,Hyperlink) values(%s,%s)", (Application_Name, Hyperlink))    # Query to insert data into database FossBytes_Data
    r.connection.commit()             # This method sends a COMMIT statement to the MySQL server, committing the current transaction.

#  Create variables to store collected data
source = requests.get('https://fossbytes.com/essential-free-best-android-apps/').text          #To get the page source of website FossBytes
soup = BeautifulSoup(source, 'lxml')                                                           # Parse the contents of page source of Google playstore placed in source and store the contents in soup


for s in soup.findAll('div', {'class': 'td-pb-span8 td-main-content'}):                 #for loop to iterate with division whoose class is "td-pb-span8 td-main-content"
    for v in s.findAll('h3'):                                                           #for loop to iterate with Header3( h3)
        Application_Name = v.text                                                        #Stores the application name in variable  Application_Name
        Hyperlink = v.a.get('href')                                                      #Stores the hyperlink in variable Hyperlink
        attrib(Application_Name, Hyperlink)                                              # Calls and store Application_Name, Hyperlink in database
        print(Application_Name, Hyperlink)                                               # Print the content on console


    connection.close()                                                            # Close database connection
    r.close()                                                                     # Cursor close