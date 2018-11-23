from pyecharts import Funnel
import pymysql

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "",
    "database": "lagou",
    "charset": "utf8"
}
def drawpci():
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT city,COUNT(city) as num FROM `lagouqd` group BY city ORDER BY num desc"
    cursor.execute(sql)
    res = cursor.fetchall()
    data = list(res)
    geo = Funnel("拉钩全前端招聘公司数", "data by lidoudou", title_color="#fff",
              title_pos="center", width=1000,
              height=600, background_color='#404a59')
    attr, value = geo.cast(data)
    print(attr,value)
    geo.add("", attr, value, visual_range=[0, 3200], maptype='china', visual_text_color="#fff",
            symbol_size=30, is_visualmap=True)
    geo.render("拉钩全前端招聘公司数.html")  # 生成html文件



if __name__ == '__main__':
    drawpci()