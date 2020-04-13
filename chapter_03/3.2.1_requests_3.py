import requests

r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

r = requests.post('http://httpbin.org/post')
print(r.headers)
r = requests.put('http://httpbin.org/put')
print(r.headers)
r = requests.delete('http://httpbin.org/delete')
print(r.headers)
r = requests.head('http://httpbin.org/head')
print(r.headers)
r = requests.options('http://httpbin.org/options')
print(r.headers)
