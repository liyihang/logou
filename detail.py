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
        'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords'
                   '=&suginput=',
        'Origin': 'https://www.lagou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Cookie': 'JSESSIONID=ABAAABAAAGFABEFE8A2337F3BAF09DBCC0A8594ED74C6C0; user_trace_token=20180122215242-849e2a04-ff7b-11e7-a5c6-5254005c3644; LGUID=20180122215242-849e3549-ff7b-11e7-a5c6-5254005c3644; index_location_city=%E5%8C%97%E4%BA%AC; _gat=1; TG-TRACK-CODE=index_navigation; _gid=GA1.2.1188502030.1516629163; _ga=GA1.2.667506246.1516629163; LGSID=20180122215242-849e3278-ff7b-11e7-a5c6-5254005c3644; LGRID=20180122230310-5c6292b3-ff85-11e7-a5d5-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516629163,1516629182; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516633389; SEARCH_ID=8d3793ec834f4b0e8e680572b83eb968'
    }
    d_result = requests.get(url, headers=d_headers)
    soup = BeautifulSoup(d_result.content, 'html.parser')

    job_bt = soup.find('dd', attrs={'class': 'job_bt'})
    if job_bt != None:

        data = re.sub(r'<.*?>','',str(job_bt))

        file = open('./2.txt','a',encoding='utf-8')
        file.write(data)

def main():
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT positionIdInLagou FROM `lagou` GROUP by positionIdInLagou"
    cursor.execute(sql)
    res = cursor.fetchall()

    for i in res:
        crwalDetail(i)
        print("写入第"+str(i)+"家公司信息")



if __name__ == '__main__':
    main()
