# url = https://pic.netbian.com/4kfengjing/
import requests
import os
from bs4 import BeautifulSoup

# 获取网页图片
urls = ["https://pic.netbian.com/4kfengjing/"] + [f"https://pic.netbian.com/4kfengjing/index_{i}.html"
                                                  for i in range(2, 212)]
for url in urls:
    r = requests.get(url)
    r.encoding = "gbk"
    html = r.text
    # print(html)

    soup = BeautifulSoup(html, "html.parser")
    imgs = soup.find_all("img")
    for img in imgs:
        src = img["src"]
        if "/uploads/" not in src:
            continue
        src = f"https://pic.netbian.com{src}"
        print(src)

        # 首先得到图片的本地文件地址
        filename = os.path.basename(src)
        with open(f"风景图片/{filename}", "wb") as f:
            r_img = requests.get(src)
            f.write(r_img.content)

