# 笑话集中营
import requests         # 导入requests库
import re               # 导入正则表达式库

domain = 'http://www.jokeji.cn/'


def print_joke(joke):
        if '<A' in joke and '</A>' in joke:
                start = joke.index('<A')
                end = joke.index('</A>')
                exception_str = joke[start:end + 4]
                joke = joke.replace(exception_str,'')
        # if '<IMG' in joke:
        #         start = joke.index('<IMG')
        #         end = joke.index(start,'>')
        #         img_str = joke[start:end + 1]
        #         joke = joke.replace(img_str,'')
        if "<BR>" in joke:
                joke_array = joke.split("<BR>")
                for context in joke_array:
                        print(context)


def find_jokes(content):
        reg = r'<P>[0-9]、(.+?)</P>'
        joke_re = re.compile(reg)
        jokes = re.findall(joke_re, content)
        return jokes


def search_jokes_by_link(link_url):
        joke_content = requests.get(link_url)  # 访问第一个链接
        joke_content.encoding = 'gbk'
        return joke_content.text


def get_joke_list(joke_text):
        joke_list = re.findall('/jokehtml/[\w]+/[0-9]+.htm', joke_text)  # 使用正则表达式找到所有笑话页面的链接
        return joke_list


def get_joke_page():
        print();


if __name__ == '__main__':

        jokePage = requests.get('http://www.jokeji.cn/list.htm')
        #jokePage = requests.get('http://www.jokeji.cn/list_1.htm')
        jokePage.encoding = 'gbk'

        jokeList = get_joke_list(jokePage.text)  # 使用正则表达式找到所有笑话页面的链接

        print(jokeList)

        for jokeLink in jokeList:

                link = domain + jokeLink

                content = search_jokes_by_link(link)

                jokes = find_jokes(content)

                for joke in jokes:  # 循环打印笑话
                        print_joke(joke)
                        print()                 # 打印一个换行

        # for jokeLink in jokeList:
        #         jokeContent = requests.get('http://www.jokeji.cn/' + jokeLink)      # 访问第一个链接
        #         jokeContent.encoding = 'gbk'
        #         jokes = re.findall('<P>[0-9].*</P>', jokeContent.text)
        #         for joke in jokes:          # 循环打印笑话
        #                 print(joke)
        #                 print()                 # 打印一个换行

