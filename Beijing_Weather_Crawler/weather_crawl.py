import requests
import pandas as pd

url = "https://tianqi.2345.com/Pc/GetHistory"
# 获得路径：network---文件---Headers---General---Request_URL(截取?之前的)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36'
}


# 应对反爬机制

def crawl_table(year, month):
    # 提供年份，月份作为网页ajax请求参数爬取对应的表格数据，这个任务面对的是动态网页，会随时根据请求更新
    params = {
        "areaInfo[areaId]": 54511,
        "areaInfo[areaType]": 2,
        "date[year]": year,
        "date[month]": month
    }
    # 构造ajax的请求和参数字段用以搜索指定年和月份的天气信息

    response = requests.get(url, headers=headers, params=params)
    # 得到的response含有几个字典，结构类似{"code":, "msg":, "data"}
    data = response.json()["data"]
    # 将response字典转化为json字段，是一段网页代码
    data_frame = pd.read_html(data)[0]
    # 利用pandas库里的read_html来解析网页代码
    # print(data_frame.head())----可以打印data_frame的头部几个数据
    return data_frame


df_list = []
for year in range(2013, 2023):
    for month in range(1, 13):
        print("爬取：", year, month)
        # 检查是否每个月都已经爬取成功
        df = crawl_table(year, month)
        df_list.append(df)

pd.concat(df_list).to_excel("北京近十年天气数据.xlsx", index=False)
