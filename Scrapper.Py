import urllib.request
from bs4 import BeautifulSoup




#with urllib.request.urlopen(https://sfbay.craigslist.org/) as response:
    #html = response.read()

#deffine sfbay Craigslist as the url to open. Print it out.

url = urllib.request.urlopen('https://sfbay.craigslist.org/')
print(url.read())
