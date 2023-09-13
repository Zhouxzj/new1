import requests
from bs4 import BeautifulSoup
import selenium

url = "http://www.crazyant.net"

r = requests.get(url)

print(r.text)