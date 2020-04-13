from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'http://jianshu.com/search?q=python&page=1&type=collections'))

from urllib.request import urlopen

rp = RobotFileParser()
rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('*', 'http://jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'http://jianshu.com/search?q=python&page=1&type=collections'))
