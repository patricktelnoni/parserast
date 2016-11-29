'''
from HTMLParser import HTMLParser
from bs4 import BeautifulSoupup
import pyesprima
'''
from bs4 import BeautifulSoup
import bleach, pyesprima, urllib, mysql.connector, time
cnx     = mysql.connector.connect(user='root', database='malicia')
cursor  = cnx.cursor()
query   = ("SELECT landing_ip FROM landing_ip" )

cursor.execute(query)
file    = open('tokenizedjsraw.txt', 'w')
start = time.time()
for domain in cursor:
    try:
        page    = urllib.urlopen(str(domain[0]))
        result  = page.read()
        soup    = BeautifulSoup(str(result), "html5lib")

        for i in soup.find_all('script'):
            clean = bleach.clean(i, tags=[], strip=True)
            tulis = pyesprima.parse(str(clean), loc=True)
            file.write(str(clean))
        break
    except Exception as e:
        print e

end = time.time()
print(end - start)
file.close()
