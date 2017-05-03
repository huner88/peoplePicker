# -*- coding: utf-8 -*-
import requests 
from bs4 import BeautifulSoup,NavigableString
import urllib,urllib2,cookielib
import string
import mechanize
import sys
import os
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib2  
import datetime  

import urllib2,urllib,cookielib  
  
#设置cookie  
cookiejar= cookielib.CookieJar()  
cookie=urllib2.HTTPCookieProcessor(cookiejar)  
opener= urllib2.build_opener(cookie,urllib2.HTTPHandler())  
urllib2.install_opener(opener)  
  
#账号信息  
email=raw_input('输入邮箱')  
password=raw_input('输入密码')  
domain='renren.com'#域名  
url='http://www.renren.com/SysHome.do'#可以通过审查元素得到  
#httpfox抓取数据包信息, 其中headers和domain 可有可无 postdata里面很多元素；最主要的用户名密码  
#d对付反爬虫  
headers={  
   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'  
    }  
data={  
    'email' : email,  
    'password' : password,  
    'domain': domain  
    }  
#编码data  
postdata = urllib.urlencode(data)  
  
  
#发起请求  
req=urllib2.Request(url,postdata,headers)  
#获取源码  
print urllib2.urlopen(req).read()  


searchPhoneNum = raw_input('Enter phone number to search: ')

strUrl =("http://www.soudianhua.com/Phone.aspx?number=%s" % (searchPhoneNum))
req = urllib2.Request(strUrl) 

response = urllib2.urlopen(req)  
the_page = response.read() 

soup = BeautifulSoup(the_page)
a = soup.findAll('span',{'id':'cityname'})
print "***********************************************"
for b in a:
    c = ''.join(b.findAll(text=True))
    data = c.strip()
    print "This phone number belong to city of:" + data



