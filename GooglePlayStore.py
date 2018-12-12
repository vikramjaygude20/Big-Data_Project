# Group Name :- Big Data Learners
# Teammates  :- Mitul Kamdar
# Teammates  :- Vikram Jaygude
# Date       :- 12/11/ 2018

# Import libraries

from bs4 import BeautifulSoup          #Python package for parsing HTML and XML documents
import requests                        #Python library  for handling requests and URL HANDLING
import pymysql                         #Python library for handling database


# Make Database Connections
# User is CrawlPlaystore
# Password is CrawlPlaystore
# Server is 10.103.92.251 in Marshall university
# Name of the database is crawlplaystore
connection = pymysql.connect(user='crawlplaystore', password='crawlplaystore', host='10.103.92.251', database='crawlplaystore')
# Create a cursor which are bound to the connection of entire lifetime of database session
r = connection.cursor()

#  Create variables to store collected data
def attrib(Application_Name, Hyperlink, DocumentID):
    r.execute("INSERT INTO Google_Playstore_Data(Application_Name,Hyperlink,DocumentID) values(%s,%s,%s)", (Application_Name, Hyperlink, DocumentID))    # Query to insert data into database Google_Playstore_Data
    r.connection.commit()             # This method sends a COMMIT statement to the MySQL server, committing the current transaction.


source = requests.get('https://play.google.com/store/apps/collection/topselling_free').text               #To get the page source of Google playstore page
soup = BeautifulSoup(source, 'html.parser')                                        # Parse the contents of page source of Google playstore placed in source


for s in soup.findAll('div', {'class': 'card no-rationale square-cover apps small'}):         #for loop to iterate with division whoose class is card no-rationale square-cover apps small
    Application_Name = s.div.div.a.get('aria-label')                                          #Stores the application name in variable  Application_Name
    Hyperlink = s.a.get('href')                                                               #Stores the hyperlink in variable Hyperlink
    DocumentID = s.get('data-docid')
    #select * from table --- docid
    #How to fetch data from mysql and render on python page
    #if(this.docid == mysqlfetched.docid ){
    # date update}
    #else
    #call attrib

    attrib(Application_Name, Hyperlink, DocumentID)                                         #Calls and store Application_Name, Hyperlink, DocumentID in database
    print('name:',Application_Name,'href:', Hyperlink,'docid:',DocumentID)                  # Print the content on console

connection.close()
r.close()                                                                     # Cursor close