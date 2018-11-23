from pyecharts import Funnel
from pyecharts import Geo
import pymysql

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "",
    "database": "lagou",
    "charset": "utf8"
}

#设置漏斗图
def drawFunnel():
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT city,COUNT(city) as num FROM `lagouqd` group BY city ORDER BY num desc"
    cursor.execute(sql)
    res = cursor.fetchall()
    data = list(res)
    geo = Geo("拉钩全前端招聘公司分布", "data by lidoudou", title_color="white",
              title_top="bottom",title_pos="center", width=1000,
              height=600, background_color='#BFEFFF')
    attr, value = geo.cast(data)

    for index ,item in enumerate(value):
        if item > 200:
            value[index] =200
    geo.add('拉钩全国前端招聘公司分布',attr,value, visual_range=[0, 200],
            symbol_size=30, is_visualmap=True,is_piecewise=False,visual_type="size",
    visual_split_number=10,)
    geo.render("拉钩全国前端招聘公司分布.html")  # 生成html文件


def drawtext():
    lst = []
    file = open('./4.txt',encoding='utf-8')
    for line in file:
        string = line.split()
        data = tuple(string)
        lst.append(data)
    return lst



def drawGeo():
    data = drawtext()
    geo = Funnel(
        "全栈招聘企业技术栈",
        "data from lidoudou",
        title_color="#fff",
        title_pos="center",
        title_top="bottom",
        width=1200,
        height=600,
        background_color="blue",

    )
    attr, value = geo.cast(data)

    geo.add("",attr,value,visual_range=[0, 200],maptype="china",symbol_size=35,
            is_visualmap=True)
    geo.render('全栈技术栈.html')


if __name__ == '__main__':
    drawGeo()
    drawFunnel()