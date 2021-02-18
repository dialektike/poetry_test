## 아래 파일을 이준범님이 작성한 https://velog.io/@hj8853/Poetry를-사용하여-가상환경-만들기 에서 가져왔습니다.
## 자세한 내용은 윗 링크를 참고해 주세요!

import requests
from bs4 import BeautifulSoup
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://beomi.github.io/beomi.github.io_old/')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'h3 > a'
    )

data = {}

for title in my_titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)