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