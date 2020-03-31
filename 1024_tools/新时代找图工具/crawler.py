import requests
from bs4 import BeautifulSoup
import json
import time
from upload import logger


class Random_PornPic():
    def __init__(self, gallery_num):
        self.number = gallery_num
        self.history = self.load_local_his()
        self.gallery_info = list()
# history字典格式，{"gallery_url":gallery_info}
# gallery_info格式   self.gallery_info = {'name':name,
    #                                  'length':length,
    #                                  'gallery_pics':gallery_pics
    #                                  }

    def parse_gallery(self,url):
        if url == "":
            return []
        logger.info("Parsing the gallery")
        try:
            r = requests.get(url,verify=False)
            assert r.status_code == 200
            soup = BeautifulSoup(r.text, 'lxml')
            result = soup.select(".thumbwook > .rel-link")
            result = [x['href'] for x in result]
            return result
        except Exception:
            logger.info("Parse Gallary Failed")
            return []

    # 检查重复
    def check_useful(self, url,limit=20):
        self.history = self.load_local_his()
        if url in self.history:
            return False
        else:
            gallery_pics = self.parse_gallery(url)
            name = url.split('/')[-2]
            length = len(gallery_pics)
            self.gallery_info = {'name':name,
                                 'length':length,
                                 'gallery_pics':gallery_pics
                                 }
            # print(self.gallery_info)
            self.history[url] = self.gallery_info
            self.save_local_his()
            if self.gallery_info['length'] >= limit:
                logger.info(url + " ------- VALID")
                return True
            else:
                return False

    def get_random_gallery(self):
        try:
            r = requests.get("https://www.pornpics.com/random/index.php",verify=False,timeout=30)
            if r.status_code == 200:
                url = r.json()['link']
                logger.info("get random gallery: " + url)
                time.sleep(30)
                return url
        except Exception:
            logger.warning("Fail to get random gallery")
            time.sleep(300)




    def load_local_his(self):
        try:
            with open('./history.json', 'r', encoding='utf-8') as f_toc:
                data = json.load(f_toc)
        except Exception:
            data = dict()
        return data

    def save_local_his(self):
        f_toc = open('./history.json', 'w', encoding='utf-8')
        json.dump(self.history, f_toc, ensure_ascii=False, indent=4)
        f_toc.close()


    def gen_gallery(self):
        i = 0
        while i < self.number:
            url = self.get_random_gallery()
            if self.check_useful(url):
                logger.info("找到一个符合条件的相册")
                with open(self.gallery_info['name'], 'w', encoding='utf-8') as f:
                    f.write('\n'.join(self.gallery_info['gallery_pics']))
                    logger.warning("保存一个相册成功")
                i = i + 1
        logger.info("生成了" + self.number + "个相册")
        return


if __name__ == "__main__":
    Random_PornPic(3).gen_gallery()


