# logou
拉钩相关职务招聘，地区分析，技能图谱

#职位抓取
文件夹下的lagou.py 是抓取职位及相关信息的

#获取职位详情
detail.py 获取职位的岗位要求和岗位职责

#抽离技能
formart.py 是从文本中抽离相关岗位技能

#相关技能的词频统计

analysis.py 是从抽离的技能中统计技能词频

#可视化展示
datavisualization.py 是相关岗位技能的可视化展示
因为很多岗位默认北京，所以企业的分布不是很准确。还有一个pyechart的GEO生成地图默认带了经纬度，这个还没有处理