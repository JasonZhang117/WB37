from urllib import request, error

try:
    response = request.urlopen('https://cuiqingai.com/index.htm')
except error.URLError as e:
    print(e.reason)