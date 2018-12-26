import random

import requests
import sys
import io
import re
import os
import time
from urllib import request as rr

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

# 登录后才能访问的网页
url = 'http://www.icourse8.com/'
# 浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'_cliid=UjXEFI0xRWOMURij; _lastEnterDay=2018-12-26; _siteStatId=cb4f38e5-c9d6-486d-88bf-e0f4fca11e8c; _siteStatDay=20181226; _siteStatRedirectUv=redirectUv_16779352; _siteStatVisitorType=visitorType_16779352; lastLoginTime16779352146=2018-12-26; loginMemberCacct=jf16072768; loginMemberAcct=jaychou114118; _FSESSIONID=86tUGBB-LS0OeHkl; tabSwitch=0; _pdDay_285_0=20181226; _pdDay_256_0=20181226; _pdDay_294_0=20181226; _pdDay_368_0=20181226; _pdDay_743_0=20181226; _pdDay_877_0=20181226; _siteStatVisit=visit_16779352; _siteStatVisitTime=1545835071860'
# 设置请求头
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
# 把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

root_pattern = '<td class="formMiddleCenter formMiddleCenter323 " valign="top">([\s\S]*?)</td>'
href_pattern = "<a hidefocus='true' href='([\s\S]*?)' target='_blank'>"

in_html_title_pattern = '<head><title>([\s\S]*?)</title>'
# in_html_time_pattern = "课时：</td> <td valign='top' class='propValue g_minor' > <span>([\s\S]*?)</span>"
in_html_time_pattern = '<span>(\d*)小时[\s\S]*?</span>'
in_html_url_pattern = 'https://pan.baidu.com/s/[\s\S]*?</span>'
in_html_code_pattern = '<span>([a-zA-Z0-9]{4})</span>'
course_img_url_prefix = 'src="//16779352.s21i.faiusr.com/4/'
in_html_img_pattern = course_img_url_prefix + '[\s\S]*?.png'
course_list = []
for x in range(1, 619, 20):
    # 在发送get请求时带上请求头和cookies
    resp = requests.get(url, headers=headers, cookies=cookies)
    # 拿到网页内容
    content = resp.content.decode('utf-8')

    # 解析网页内容
    # course_content = re.findall(root_pattern, content)
    course_content_list = re.findall(href_pattern, content)
    course_content_list = course_content_list[:-1]
    url_list = list(map(lambda s: url + s, course_content_list))
    for url_in in url_list:
        # 在发送get请求时带上请求头和cookies
        resp_in = requests.get(url_in, headers=headers, cookies=cookies)
        # 拿到网页内容
        content_in = resp_in.content.decode('utf-8')
        content_in = content_in.replace('\r\n', '')
        # 获取云盘链接，密码，图片，title，类型，时长
        pan_url = re.findall(in_html_url_pattern, content_in)
        video_title = re.findall(in_html_title_pattern, content_in)
        video_code = re.findall(in_html_code_pattern, content_in)
        video_img = re.findall(in_html_img_pattern, content_in)
        video_time = re.findall(in_html_time_pattern, content_in)
        video_info = {'video_title': video_title[0].strip(), 'pan_url': pan_url[0][:-7],
                      'video_code': video_code[0], 'video_time': video_time[0] + '小时',
                      'video_img': video_img}
        course_list.append(video_info)
        print(video_info)
        # sleep
        time.sleep(random.randint(0,5))
    index = 1
    for course in course_list:
        os.mkdir(course['video_title'])
        path = course['video_title']
        with open(course['video_title'] + '.txt', "wb") as f:
            f.write(str(course))
            f.close()
        for img in course['video_img']:
            rr.urlretrieve(img, path + u"/%d.jpg" % index)
            print(u"成功保存第%d张图片" % index)
            index += 1




    # 下载图片并保存到本地
    def download(_url, file_name):
        if (_url == None):  # 地址若为None则pass
            pass
        result = rr.urlopen(_url)  # 打开链接

        if (result.getcode() != 200):  # 如果链接不正常则pass
            pass
        else:
            data = result.read()  # 链接正常的话则进行下载
            with open(file_name, "wb") as f:
                f.write(data)
                f.close()

a = 1
