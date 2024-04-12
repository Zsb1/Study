import requests
from bs4 import BeautifulSoup
import time

# url = "https://movie.douban.com/top250?start=0&filter="

headers = {
    "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"""
}

urls = ["https://movie.douban.com/top250?start=%d&filter=" % i
        for i in range(0, 226, 25)
        ]

movies = []


# for url in urls:
#     resp = requests.get(url, headers=headers)
#     soup = BeautifulSoup(resp.text, "html.parser")
#     print("当前网页:", url, resp.status_code)
#
#     movie = {}
#
#     for li in soup.find_all("li"):
#         items = li.find("div", class_="item")
#         if not items:
#             continue
#
#         movie['Tops'] = items.find("div", class_="pic").find("em").get_text()  # 排名
#
#         movie['src'] = li.find("img")["src"]  # 图片地址
#
#         movie['Titles'] = items.find("div", class_="hd").find("span").get_text()  # 电影名
#
#         movie['Directors'] = (items.find("div", class_="bd").find("p").get_text().replace("\n", "")
#                               .replace(" ", "").replace("\xa0", " "))  # 导演和演员
#
#         movie['Score'] = items.find("div", class_="star").find("span", class_="rating_num").get_text()  # 评分
#
#         movie['spans'] = items.find("div", class_="star").find_all("span")[3].text  # 多少人评论
#
#         span_element = items.find("p", class_="quote")  # 简介
#         if span_element:
#             # 如果'span'标签存在，获取其文本内容
#             movie['inq'] = span_element.find("span").get_text()
#         else:
#             # 如果'span'标签不存在，设置'inq'键的值为空字符串
#             movie['inq'] = ""
#
#         movies.append(
#             [movie['Tops'], movie['Titles'], movie['src'], movie['Directors'], movie['Score'], movie['spans'],
#              movie['inq']])
#
#     time.sleep(5)  # 防止爬取太快ip被封  根据网页的robots.txt文件


# with open("movies.txt", "w", encoding="utf8") as file:
#     for i in movies:
#         file.write(str(i))
#         file.write("\n")
# file.close()

def crawl_html(url):
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")
    print("当前网页:", url, resp.status_code)

    html = resp.text
    return html


def parse_content(html):
    soup = BeautifulSoup(html, "html.parser")

    movie = {}

    for li in soup.find_all("li"):
        items = li.find("div", class_="item")
        if not items:
            continue

        movie['Tops'] = items.find("div", class_="pic").find("em").get_text()  # 排名

        movie['src'] = li.find("img")["src"]  # 图片地址

        movie['Titles'] = items.find("div", class_="hd").find("span").get_text()  # 电影名

        movie['Directors'] = (items.find("div", class_="bd").find("p").get_text().replace("\n", "")
                              .replace(" ", "").replace("\xa0", " "))  # 导演和演员

        movie['Score'] = items.find("div", class_="star").find("span", class_="rating_num").get_text()  # 评分

        movie['spans'] = items.find("div", class_="star").find_all("span")[3].text  # 多少人评论

        span_element = items.find("p", class_="quote")  # 简介
        if span_element:
            # 如果'span'标签存在，获取其文本内容
            movie['inq'] = span_element.find("span").get_text()
        else:
            # 如果'span'标签不存在，设置'inq'键的值为空字符串
            movie['inq'] = ""

        movies.append(
            [movie['Tops'], movie['Titles'], movie['src'], movie['Directors'], movie['Score'], movie['spans'],
             movie['inq']])
    time.sleep(5)  # 防止爬取太快ip被封  根据网页的robots.txt文件


def download_to_txt(movies):
    with open("movies.txt", "w", encoding="utf8") as file:
        for i in movies:
            file.write(str(i))
            file.write("\n")
    file.close()


for url in urls:
    html = crawl_html(url)
    parse_content(html)
    download_to_txt(movies)
