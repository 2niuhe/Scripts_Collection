## 网易云音乐歌手词云

> 功能：根据网易云音乐上歌手的id号生成歌手热门50首歌词的词云

**版本：Python3.5版本**

**requirement**:
> beautifulsoup4==4.6.0  
jieba==0.39  
requests==2.18.4  
scipy==1.0.0  
wordcloud==1.4.1  
matplotlib==2.1.2  


### 使用：  
`pip install -r requirements.txt`
歌手id号获取示范（红圈内）：     
![金玟岐的id号](http://ww1.sinaimg.cn/large/005LvakSly1fq5l0aebwgj30e009tacf.jpg)     
修改Config.py中的参数：   
`SINGER = 893259           # 歌手id号 `        
配置完后：     
`python run.py`


### 结果示意图  
![爱打游戏的金大哥](http://ww1.sinaimg.cn/large/005LvakSly1fq5l5kalnfj311y0lcn98.jpg)


