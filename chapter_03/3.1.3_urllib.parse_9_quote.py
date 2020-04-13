from urllib.parse import quote

keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)

# result= (scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
# scheme='http' ://前面--协议
# netloc='www.baidu.com' 第一个/符号前面--域名
# path='/index.html' 访问路径
# params='user' 分号;后面--参数
# query='id=5' 问号?后面--查询条件，一般用作GET类型的url
# fragment='comment' 井号#后面--锚点