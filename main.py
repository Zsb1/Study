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

for url in urls:
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")
    print("当前网页:", url, resp.status_code)
    for li in soup.find_all("li"):
        items = li.find("div", class_="item")
        if not items:
            continue

        Tops = items.find("div", class_="pic").find("em").get_text()  # 排名

        imgs = li.find("img")
        src = imgs["src"]  # 图片地址

        Titles = items.find("div", class_="hd").find("span").get_text()  # 电影名


        Directors = items.find("div", class_="bd").find("p").get_text().strip().replace("\n", "<br/>").replace('<br>',
                                                                                                               '').replace(
            "<br/>                            ", "\t")  # 导演

        Score = items.find("div", class_="star").find("span", class_="rating_num").get_text()  # 评分

        spans = items.find("div", class_="star").find_all("span")

        inq = items.find("p", class_="quote")  # 简介
        if not items.find("p", class_="quote"):
            continue

        print(Tops, Titles, src, Directors, Score, spans[3].text, inq.find("span").get_text())

    time.sleep(5)  # 防止爬取太快ip被封  根据网页的robots.txt文件

'''def get_html(url):
    headers = {
        "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"""
    }
    resp = requests.get(url, headers=headers)
    # soup = BeautifulSoup(resp.text, "html.parser")
    resp.encoding = resp.apparent_encoding

    if resp.status_code == 200:
        html = resp.text
        return html
    else:
        print(resp.status_code)


def parse_html(soup):
    # print("当前网页:", url, resp.status_code)

    movies = []

    for lis in soup.find_all("li"):
        items = lis.find("div", class_="item")
        if not items:
            continue

        movie = {}
        movie['Tops'] = items.find("div", class_="pic").find("em").get_text()  # 排名

        movie['src'] = lis.find("img")["src"]

        movie['Titles'] = items.find("div", class_="hd").find("span").get_text()  # 电影名

        movie['Directors'] = items.find("div", class_="bd").find("p").get_text().strip().replace("\n", "<br/>").replace(
            "<br/>                            ", "\t")  # 导演

        movie['Score'] = items.find("div", class_="star").find("span", class_="rating_num").get_text()  # 评分

        movie['spans'] = items.find("div", class_="star").find_all("span")[3]

        movie['inq'] = items.find("p", class_="quote").find("span", class_="inq").get_text()  # 简介
        if not items.find("p", class_="quote"):
            continue

        movies.append(movie)
    return movies


def print_movie_info(movies):
    for movie in movies:
        print(movie['Tops'], movie['Titles'], movie['src'], movie['Directors'], movie['Score'], movie['inq'])


def add_txt(movies):
    with open("MoviesTop250.txt", "w", encoding="utf8") as f:
        f.write("Top\t电影名\t电影封面\t导演信息\t评分\t简介\n")
        for movie in movies:
            f.write(movie['Tops'])
            f.write(movie['Titles'])
            f.write(movie['src'])
            f.write(movie['Directors'])
            f.write(movie['Score'])
            f.write(movie['inq'])
            f.write("\n")


def fetch_and_print_movie_info():
    urls = ["https://movie.douban.com/top250?start=%d&filter=" % i
            for i in range(0, 226, 25)
            ]

    for url in urls:
        soup = BeautifulSoup(get_html(url), "html.parser")
        movies = parse_html(soup)
        print("当前网页:", url)
        print_movie_info(movies)
        # add_txt(movies)
        time.sleep(5)


fetch_and_print_movie_info()'''
