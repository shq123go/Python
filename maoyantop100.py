'''
import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool

def get_one_page(url):    # 伪装浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 /(Windows NT 10.0; Win64; x64) AppleWebKit537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>'  # 排名
                         '.*?<p.*?"name"><.*?title="(.*?)"'    # 名字
                         '.*?"star">(.*?)</p>'            # 演员
                         '.*?"releasetime">(.*?)</p>'       # 上映时间
                         '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>'   # 评分
                         , re.S)
    res = re.findall(pattern, html)     # 使用正则表达式查找所有，返回list
    for item in res:
        yield {
            'index': item[0],
            'title': item[1],
            'actor': item[2].strip()[3:],
            'time': item[3].strip()[5:],
            'score': item[4] + item[5]
        }

def write_to_file(content):
    with open('result.text','a',encoding = 'utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?+str(offset)'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ =='__main__':
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])
