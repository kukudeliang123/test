import requests
import json
import asyncio
async def func(x):
    print('开始')
    url = ['https://api.seniverse.com/v3/weather/now.json?key=Sr1jDnlQvCW5_0As2&location=成都&language=zh-Hant&unit=c',
           'https://api.seniverse.com/v3/weather/now.json?key=Sr1jDnlQvCW5_0As2&location=重庆&language=zh-Hant&unit=c',
           'https://api.seniverse.com/v3/weather/now.json?key=Sr1jDnlQvCW5_0As2&location=上海&language=zh-Hant&unit=c',
           'https://api.seniverse.com/v3/weather/now.json?key=Sr1jDnlQvCW5_0As2&location=北京&language=zh-Hant&unit=c']
    shuju = requests.get(url[x])
    jieguo = open('c.json', 'w')
    jieguo.write(shuju.text)
    jieguo.close()
    openjson = open('c.json','r',encoding = 'cp936')
    zd_json = json.load(openjson)
    openjson.close()
    print('你所在城市为'+zd_json['results'][0]['location']['name'])
    print('当前温度为'+zd_json['results'][0]['now']['temperature']+'C')
    
task_list = [func(3),func(2),func(1),func(0)]
asyncio.run(asyncio.wait(task_list))
