#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json
import requests

commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&\
channel=sh&newsid=comos-{}&group=&compress=0&ie=utf-8&\
oe=utf-8&page=1&page_size=20'


#get评论数
def getCommentCount(newsurl):
    m = re.search('doc-i(.*).shtml',newsurl)
    newsid = m.group(1)
    comments = requests.get(commentURL.format(newsid))
    jd = json.loads(comments.text.strip('var data='))
    return jd['result']['count']['total']

#test
if __name__ == "__main__":
    newsurl = 'http://news.sina.com.cn/o/2017-02-27/doc-ifyavwcv9109647.shtml'
    print(getCommentCount(newsurl))


