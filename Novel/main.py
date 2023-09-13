import requests
from bs4 import BeautifulSoup


def get_novel_chapters():
    root_url = "http://www.89wxw.cn/0_9/"
    r = requests.get(root_url)
    r.encoding = "gbk"
    soup = BeautifulSoup(r.text, "html.parser")

    data = []
    for dd in soup.find_all("dd"):
        link = dd.find("a")
        if not link:
            continue

        data.append(("http://www.89wxw.cn%s" % link['href'], link.get_text()))
    return data


def get_chapter_content(new_url):
    r = requests.get(new_url)
    r.encoding = "gbk"
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.find("div", id='content').get_text()


novel_chapters = get_novel_chapters()
total_cnt = len(novel_chapters)
idx = 0
for chapter in novel_chapters:
    idx += 1
    print(idx, total_cnt)
    url, title = chapter
    with open("%s.txt" % title, "w") as fout:
        fout.write(get_chapter_content(url))
    break
