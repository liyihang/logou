from pyecharts import Funnel
from string import punctuation
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
    geo = Funnel("拉钩全前端招聘公司数", "data by lidoudou", title_color="white",
              title_top="bottom",title_pos="center", width=1000,
              height=600, background_color='#BFEFFF')
    attr, value = geo.cast(data)

    for index ,item in enumerate(value):
        if item > 200:
            value[index] =200
    geo.add("", attr, value, visual_range=[0, 200], maptype='china', visual_text_color="#fff",
            symbol_size=30, is_visualmap=True)
    geo.render("拉钩全国前端招聘公司数.html")  # 生成html文件

def replacePunctuations(line):
    for ch in line:
        # 这里直接用了string的标点符号库。将标点符号替换成空格
        if ch in punctuation:
            line = line.replace(ch, " ")
        return line

# 对文本的每一行计算词频的函数
def processLine(line, wordCounts):
    # 用空格替换标点符号
    line = replacePunctuations(line)
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1

def drawGeo():
    infile = open("3.txt", 'r')
    count = 50
    words = []
    data = []

    # 建立用于计算词频的空字典
    wordCounts = {}
    for line in infile:
        processLine(line.lower(), wordCounts)  # 这里line.lower()的作用是将大写替换成小写，方便统计词频
    # 从字典中获取数据对
    pairs = list(wordCounts.items())
    # 列表中的数据对交换位置,数据对排序
    items = [[x, y] for (y, x) in pairs]
    items.sort()
    # 因为sort()函数是从小到大排列，所以range是从最后一项开始取
    for i in range(len(items) - 1, len(items) - count - 1, -1):
        data =  items[i][1] + "\t" + str(items[i][0])
        print(data)

if __name__ == '__main__':
    drawGeo()