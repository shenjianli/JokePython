# 笑话集中营
import requests         # 导入requests库
import re               # 导入正则表达式库
jokePage = requests.get('http://www.jokeji.cn/list.htm')
jokeList = re.findall('/jokehtml/[\w]+/[0-9]+.htm',jokePage.text)   # 使用正则表达式找到所有笑话页面的链接
jokePage.encoding = 'gbk'
for jokeLink in jokeList:
        jokeContent = requests.get('http://www.jokeji.cn/' + jokeLink)      # 访问第一个链接
        jokeContent.encoding = 'gbk'
        jokes = re.findall('<P>[0-9].*</P>', jokeContent.text)
        for joke in jokes:          # 循环打印笑话
                print(joke)
                print()                 # 打印一个换行