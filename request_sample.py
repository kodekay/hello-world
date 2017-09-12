import requests
result = requests.get("http://info.cern.ch/hypertext/WWW/TheProject.html")
result.status_code
result.headers
print (result.headers)
c = result.content
print (c)
from bs4 import BeautifulSoup
soup = BeautifulSoup(c, "html.parser")
samples = soup.find_all("body")
print (samples)
print (soup.prettify())

