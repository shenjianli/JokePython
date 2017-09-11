# 笑话集中营
import requests         # 导入requests库
import re               # 导入正则表达式库
import JokeDB
import time
import UpdateDB

def joke():
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


if __name__ == '__main__':
        # content = '老婆逛街回来，老公看老婆买的：老婆，我很奇怪，你买衣服，化妆品，我理解，你买个菜谱干嘛？老婆：提高一下生活质量呗。老公：照这样说，以后咱家你做菜了？老婆：错！老公：那干嘛呢？！老婆：从今天开始，老娘要按照菜谱点菜，今晚就先来一个‘蟹黄鱼翅’和‘清炖燕窝’吧！老公：啊……<A href="http://www.jokeji.cn/yuanchuangxiaohua/?hyname=%CD%F9%CA%C2%C8%E7%B7%E7" target=_blank>@往事如风</A><br>'
        # if '<A' in content and '</A>' in content:
        #         start = content.index('<A')
        #         end = content.index('</A>')
        #         exception_str = content[start:end + 4]
        #         content = content.replace(exception_str,'')
        #         print(content)




        # jokePage = requests.get('http://www.jokeji.cn/list.htm')
        # # jokePage = requests.get('http://www.jokeji.cn/list_1.htm')
        # jokePage.encoding = 'gbk'
        #
        # jokeList = JokeMain.get_joke_list(jokePage.text)  # 使用正则表达式找到所有笑话页面的链接
        #
        # last_site = UpdateDB.query_mysql_data()
        # print("最近更新的地址是：", last_site)
        # req_list = []
        # for site in jokeList:
        #         if site != last_site:
        #                 req_list.append(site)
        #         else:
        #                 break
        # if len(req_list) != 0:
        #         UpdateDB.insert_mysql_data(req_list[0])
        #         print("本次需要更新的地址：", req_list)
        # else:
        #         print("已经为最新了，不需要更新了")

        datetime = time.strftime("%Y%m%d", time.localtime())
        print(datetime)
        date = '2017-09-08'
        result = JokeDB.query_mysql_data(date)
        print(result)


