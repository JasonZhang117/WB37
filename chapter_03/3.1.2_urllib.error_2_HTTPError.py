from urllib import request, error

try:
    response = request.urlopen('https://cuiqingai.com/index.htm')
except error.HTTPError as e:
    print(e)
    print(e.reason, e.code, e.headers, sep='\n')