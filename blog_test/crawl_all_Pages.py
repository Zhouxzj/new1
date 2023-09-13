import requests
import re
from bs4 import BeautifulSoup

from utils import urlManager

root_url = "http://www.crazyant.net"

urls = urlManager.UrlManager()
urls.add_new_url(root_url)

fout = open("crawl_all_Pages.txt","w")
while urls.has_new_url():
    curr_nrl = urls.get_url()
    r = requests.get(curr_nrl, timeout=10)
    if r.status_code != 200:
        print("error, return status_code is not 200", curr_nrl)
        continue
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.title.string

    fout.write("%s\t%s\n"%(curr_nrl, title))
    #方便快速看到数据，将数据刷到磁盘里
    fout.flush()
    print("success: %s, %s, %d"%(curr_nrl, title, len(urls.new_urls)))

    links = soup.find_all("a")
    for link in links:
        href = link.get("href")
        if href is None:
            continue

        #正则表达式
        pattern = r'^http://www.crazyant.net/\d+.html$'
        if re.match(pattern, href):
            urls.add_new_url(href)

fout.close()