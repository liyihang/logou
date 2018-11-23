import requests
from bs4 import BeautifulSoup
import pymysql
import re

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "",
    "database": "lagou",
    "charset": "utf8"
}
def crwalDetail(id):
    url = 'https://www.lagou.com/jobs/%s.html' % id
    d_headers = {
        'Host': 'www.lagou.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'

    }
    d_result = requests.get(url, headers=d_headers)
    soup = BeautifulSoup(d_result.content, 'html.parser')

    job_bt = soup.find('dd', attrs={'class': 'job_bt'})
    if job_bt != None:

        data = re.sub(r'<.*?>','',str(job_bt))

        file = open('java.txt','a',encoding='utf-8')
        file.write(data)

def main():
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT positionIdInLagou FROM `lagoujava` GROUP by positionIdInLagou"
    cursor.execute(sql)
    res = cursor.fetchall()

    for i in res:
        crwalDetail(i)
        print("写入第"+str(i)+"家公司信息")



if __name__ == '__main__':
    main()
