import requests
from datetime import datetime
from bs4 import BeautifulSoup
from getCommentCount import getCommentCount

def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    result['title'] = soup.select('#artibodyTitle')[0].text
    result['newssource'] =soup.select('.time-source span a')[0].text
    timesource = soup.select('.time-source')[0].contents[0].strip()
    result['dt'] = datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
    result['article'] =' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
    result['editor'] = soup.select('.article-editor')[0].text.lstrip('责任编辑：').strip()
    result['comments'] = getCommentCount(newsurl)
    return result

if __name__ == "__main__":
    newsurl = 'http://news.sina.com.cn/o/2017-02-27/doc-ifyavwcv9109647.shtml'
    print(getNewsDetail(newsurl))