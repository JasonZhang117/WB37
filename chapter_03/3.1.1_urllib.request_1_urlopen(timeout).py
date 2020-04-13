import socket
import urllib.request
import urllib.error

'''urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
            * , cafile = None, capath = None, cadefault = False, context = None): '''
try:     
    response = urllib.request.urlopen('https://www.python.org', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print(e)

