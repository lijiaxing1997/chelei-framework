from lib.Base_module import Base_module
from colorama import Fore
from prettytable import PrettyTable
import nmap

class Portscan(Base_module):
    def __init__(self):
        options = [
            ['target_ips', '/', '目标地址，可用逗号隔开或是用1.1.1.1-4,1.1.1.0/24格式'],
            ['target_ports', '/', '目标端口，使用逗号隔开或是使用22-88，默认使用top端口列表'],
        ]

        moudle_description = {
            'version': 'v1.0',
            'author': 'Gr33k',
            'completion_time': '2019.09.03',
            'name': '端口批量扫描',
        }
        super().__init__(moudle_description,options)
        self.version = moudle_description['version']
        self.author = moudle_description['author']
        self.completion_time = moudle_description['completion_time']
        self.name = moudle_description['name']
        self.options = super().return_options(options)
        self.variables = super().return_variables(options)


    def nmap_scan(self,tgtHost,tgtPort):
        table = PrettyTable(["目标地址", "端口", "名称", "状态"])
        nmScan = nmap.PortScanner()
        if tgtPort == None:
            results = nmScan.scan(hosts=tgtHost)
        else:
            results = nmScan.scan(hosts=tgtHost, ports=tgtPort)
        scan_hosts = results['scan'].keys()
        host_flag = 0
        for host in scan_hosts:
            try:
                scan_ports = results['scan'][host]['tcp'].keys()
            except:
                continue
            for port in scan_ports:
                state = results['scan'][host]['tcp'][port]['state']
                name = results['scan'][host]['tcp'][port]['name']
                if host_flag == 0:
                    table.add_row([host,port,name,state])
                    host_flag = 1
                else:
                    table.add_row(['',port,name,state])
            host_flag = 0
        print(table)

    def start(self):
        target_ips = []
        if self.variables['target_ips'] == '/':
            print(Fore.RED + '[-]target_ips是必填的，缺少可执行对象' + Fore.RESET)
            return
        if ',' in self.variables['target_ips']:
            target_ips = self.variables['target_ips'].split(',')
        else:
            target_ips.append(self.variables['target_ips'])
        print(Fore.GREEN + '[+]扫描开始，请等待...' + Fore.RESET)
        for tgtHost in target_ips:
            if self.variables['target_ports'] == '/':
                self.nmap_scan(tgtHost,None)
            else:
                self.nmap_scan(tgtHost,self.variables['target_ports'])


        print(Fore.GREEN + '[+]扫描结束' + Fore.RESET)
