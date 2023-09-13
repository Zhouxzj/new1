# import wad.detection
# det = wad.detection.Detector()
# url = input()
# print(det.detect(url))
import re

import requests
# import whois
#
# domain = "yale.edu"
# w = whois.whois(domain)
# print(w)

# ss = 'I love you, do you?'
# res = re.match(r'((\w)+(\W))+', ss)
# res = re.subn(r'you', 'her', ss)
# res = re.findall(r'(\w+)', ss)
# pt = re.compile(r'(\w+)')
# res = pt.findall(ss)
# print(res)
# ping_ss = 'Reply from 220.181.57.216: bytes=32 time=3ms TTL=47'
# res = re.search(r'(time=)(\d+\w+)+(.)+TTL', ping_ss)
# print(len(res.group()))
# print(res.group(2))
# from bs4 import BeautifulSoup
#
# bs1 = BeautifulSoup('<b><!--This is comment--></b>', 'html.parser')
# print(type(bs1.find('b').string))
# print(bs1.find('b').string)
from bs4 import BeautifulSoup

# ht = requests.get('https://www.douban.com')
# bs = BeautifulSoup(ht.content, 'html.parser')
# res = bs.find(text=re.compile('说句话'))
# for one in res.parent.parent.next_siblings:
#     print(one)
# for one in res.parent.parent.previous_siblings:
#     print(one)
# 不起作用

# from lxml import html
# text = requests.get('https://baike.baidu.com/item/%E8%8B%B9%E6%9E%9C/14822460?fr=ge_ala').text
# print(type(text))
# h1 = html.fromstring(text)
# print(type(h1))
# htEle = h1.xpath('/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]')[0]
# print(htEle.text)
# print(htEle.attrib)
# print(htEle.get('class'))
# print(htEle.keys())
# print(htEle.values())
# print(type(htEle))

# str1 = 'hello!'
# str2 = 'My name\'s Zmjjkk'
# with open('try.txt', 'wt') as f:
#     f.write(str1)
#     print('\nI\'m happy', file=f)
#
# with open('try.txt', 'a') as f:
#     f.write(str2)
#
# with open('try.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
#     print(text)
#
# f = open('try.txt', 'r')
# print(f.name)
# print(f.closed)
# print(f.encoding)
# f.close()
# print(f.closed)

# with open('try.txt', 'r') as f1:
#     print(f1.readable())
#     print(f1.writable())
#     print(f1.readline())
#     print(f1.readline())
#     print(f1.readlines())
#     print(f1.tell())
#     print(f1.read())
#     f1.seek(0)
#     print(f1.readlines())

# with open('try.txt', 'a+') as f:
#     f.write('new line')
#     f.writelines(['a', 'b', 'c'])
#     print(f.read())
#     f.flush()
#     print(f.read())


# import pickle
# l1 = [1,3,5,7]
# with open('l1.pkl', 'wb') as f1:
#     pickle.dump(l1,f1)
#
# with open('l1.pkl', 'rb') as f2:
#     l2 = pickle.load(f2)
#     print(l2)
# 序列化：将保存在对象中的内存转换为可以在磁盘上存储的信息
#
# cities = ['Beijing', 'Shanghai', 'Shenzhen', 'Tianjing']
# print([city for city in cities if city.startswith(('S', 'N'))])
# #
# s1 = 'aaabbcc'
# # print(s1.find('aaa'))
# # print(s1.find('abc'))
# # print(s1.find('bb'))
# # print(s1.find('dd'))
# import cv2
#
# img1 = cv2.imread("gift.png")
# result1 = cv2.resize(img1, (400, 400))
# img2 = cv2.imread("521.png")
# result2 = cv2.resize(img2, (400, 400))
# assert img1 is not None, "file could not be read, check with os.path.exists()"
# assert img2 is not None, "file could not be read, check with os.path.exists()"
# dst = cv2.addWeighted(result1, 0.3, result2, 0.7, 0)
# cv2.imshow('dst', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# from urllib.request import  urlopen
# from io import StringIO
# import csv
# data = urlopen("https://raw.githubusercontent.com/jasonong/List-of-US-States/master/states.csv").read().decode()
# dataFile = StringIO(data)
# dictReader = csv.DictReader(dataFile)
# print(dictReader.fieldnames)
# for row in dictReader:
#     print(row)
# import csv
#
# res_list = [['A', 'B', 'C'], [1, 2, 3], [4, 5, 6], [9, 0, 8]]
# with open('SAMPLE.csv', 'a') as csv_file:
#     writer = csv.writer(csv_file, delimiter=',')
#     # writer.writerows(res_list) 该方法会把列表中的每个列表作为一行再写入，但会对可迭代对象如字符串造成一些影响，ex：写入['I WILL']
#     # 会变成I, ,W,I,L,L
#     for line in res_list:
#         writer.writerow(line)
#     # 直接写入一行，接受一个可迭代对象作为参数
print("hello world")
print(0)
