import urllib.parse
import urllib.request

'''urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
            * , cafile = None, capath = None, cadefault = False, context = None): '''

data = bytes(urllib.parse.urlencode({'hello': 'world'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)

print(response.read())


