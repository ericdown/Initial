import requests
import bs4
from bs4 import BeautifulSoup
 
def getHTMLText(url):
    '''从网络上获取大学排名网页内容'''
    try:
        r = requests.get(url, timeout=30)
        # #如果状态不是200，就会引发HTTPError异常
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 
def fillUnivList(ulist, html):
    '''提取网页内容中信息到合适的数据结构'''
    soup = BeautifulSoup(html, "html.parser")
    # 查找html中tbody标签的所有<tr>子标签
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):            
            tds = tr('td')
            # tds[0].string 是排名，tds[1].string 是学校名称，tds[3].string 是学校的总分
            ulist.append([tds[0].string, tds[1].string, tds[3].string])
 
def printUnivList(ulist, num):
    ''' 打印前 num 名的大学'''
     # {1:{3}^10} 中的 {3} 代表取第三个参数
    tplt = "{0:^10}	{1:{3}^10}	{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288))) # chr(12288) 代表中文空格
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288))) # chr(12288) 代表中文空格
 
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)# 获取大学排名网页内容
    fillUnivList(uinfo, html)#提取网页内容中信息   
    printUnivList(uinfo, 20) #输出结果
 
main()