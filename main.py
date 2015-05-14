#!/usr/env python
# -*- coding:utf-8 -*-
from sys import argv

import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
	issue_number = argv[1]
	url = 'http://importpython.com/newsletter/no/%s/' % issue_number
	
	req = requests.get(url)
	soup = BeautifulSoup(req.content)
	td_content = soup.find("td", class_="content")

	read_titles = td_content.find_all("div", class_="subtitle")#, attrs={"style": "font-family:Helvetica, Arial, sans-serif;font-size:16px;font-weight:600;color:#2469A0"})
	contents = td_content.find_all("div", class_="body-text", attrs={"style": "font-family:Helvetica, Arial, sans-serif;font-size:14px;line-height:20px;text-align:left;color:#333333"})
		
	md = u'---\nlayout: post_page\ntitle: %s번 이슈\n---\n\n###읽을거리' % issue_number

	for idx, title in enumerate(read_titles):
		a_tag = title.find('a')
		link = a_tag['href'] if a_tag['href'] != '' else '#'
		title = a_tag.next.strip() 
		content = contents[idx].next.strip()
		md += u'\n<a href="'+link+'" target="_blank">'+title+'</a>\n\n'+content+'\n'
	
	md += u'\n<br />\n\n* 의역, 오역이 다소 심합니다. 개선 사항이 있으면 풀리퀘스트를 날려주세요.\n\n'
	md += u'* 원문은 <a href="http://importpython.com/newletter/no/%s" target="_blank">ImportPython</a>에서 확인할 수 있습니다.' % issue_number

	with open('Issue-%s.md' % issue_number, 'wb') as f:
		f.write(md.encode('utf-8'))