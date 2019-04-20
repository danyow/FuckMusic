from urllib import parse,request
import json


textmod={'ids':[440208476],'br':'128000'}
textmod = parse.urlencode(textmod)
print(textmod)
#输出内容:user=admin&password=admin
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url='http://music.163.com/weapi/song/enhance/player/url'
url='%s%s%s' % (url,'?',textmod)
req = request.Request(url=url,headers=header_dict)
res = request.urlopen(req)
res = res.read()
print(res)

# obj = json.loads(res)
# for track in obj['result']['tracks']:
    # print(track['name'])
# print(obj)
#输出内容(python3默认获取到的是16进制'bytes'类型数据 Unicode编码，如果如需可读输出则需decode解码成对应编码):b'\xe7\x99\xbb\xe5\xbd\x95\xe6\x88\x90\xe5\x8a\x9f'
print(res.decode(encoding='utf-8'))
#输出内容:登录成功