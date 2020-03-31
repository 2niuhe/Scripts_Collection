import time
import requests
from requests_toolbelt import  MultipartEncoder
import requests
import logging
from bs4 import BeautifulSoup
import time
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('pronpic.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s  - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
logger.info('You can find this written in pornpic.log')


def get_token_cookie():
    r = requests.get("https://www.privacypic.com/")
    soup = BeautifulSoup(r.text,'lxml')
    token = soup.findAll('script', {'data-cfasync': 'false'})[-1].text.split(';')[6].split('=')[-1][2:-1]
    print(token)
    cookie = r.cookies
    return  [token,cookie]

def upload_pic(src,token):
    time_stamp = str(int(time.time() * 1000))
    m = MultipartEncoder(
        fields={
            "source":src,
            "type": "url",
            "action": "upload",
            "timestamp": time_stamp,
            "auth_token": token[0],
            "nsfw": "1"
        }
    )
    headers = {
        'authority': 'www.privacypic.com',
        'accept': 'application/json',
        'sec-fetch-dest': 'empty',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'dnt': '1',
        'content-type': m.content_type,
        'origin': 'https://www.privacypic.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://www.privacypic.com/json',
        "timestamp": time_stamp,
        'nsfw':'1',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': str(token[1]),
    }
    response = requests.post('https://www.privacypic.com/json', headers=headers, data=m)
    print(response.text)
    if response.status_code == 200:
        logger.info("上传图片成功")
        return response.json()['image']['image']['url']
