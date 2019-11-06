#encoding:utf8
import pickle
import os
from colorama import Style,Fore
from lib.Base_module import Base_module
from prettytable import PrettyTable


MODULES = {}
MODULE_TYPES = []
MODULE_TYPE = ''
MODULE = Base_module({'version':'','author':'','completion_time':'','name':''},[])
MODULE_NAME = ""
IS_SELECT = 0


def start_init():
    print(Fore.GREEN + '[+]正在初始化程序...请稍等' + Fore.RESET)
    if os.path.exists("temp"):
        pass
    else:
        if os.system('mkdir temp') == 0:
            pass
        else:
            print(Fore.RED + "[-] 初始化temp目录失败，请手动在项目根目录创建")
    for root, dirs, files in os.walk(os.path.split(os.path.realpath(__file__))[0] + '/lib'):
        for dir in dirs:
            MODULE_TYPES.append(dir)
    while 1:
        if '__pycache__' in MODULE_TYPES:
            MODULE_TYPES.remove('__pycache__')
        else:
            break
    for module_type in MODULE_TYPES:
        into_modules = {}
        class_module_names = []
        for root,dir,files in os.walk(os.path.split(os.path.realpath(__file__))[0] + '/lib/' + module_type): #./lib/brute/
            for file in files:
                class_module_names.append(file.replace(".py","")) #['Brute_ftp','Brute_mysql','Brute_ssh]
            break
        with open(os.path.split(os.path.realpath(__file__))[0] + '/init_module.py','w+') as f:
            title = 'import os\nimport pickle\n'
            content = ''
            for class_module_name in class_module_names:
                title = title + 'from lib.'+ module_type + '.' + class_module_name + ' import ' + class_module_name + '\n'
                content = content + class_module_name.lower() + '= ' + class_module_name + '()\n' + class_module_name.lower() +'_module = pickle.dumps(' + class_module_name.lower() + ')\n' + 'f =  open(os.path.split(os.path.realpath(__file__))[0] + \'/temp/' + class_module_name.lower() + '.module\',\'wb\')\n' + 'f.write('+ class_module_name.lower() +'_module)\nf.close()\n\n'
            f.truncate()
            f.write(title + '\n')
            f.write(content)
            f.close()
        if os.path.isfile(os.path.split(os.path.realpath(__file__))[0] + '/init_module.py'):
            if os.system("python3 " + os.path.split(os.path.realpath(__file__))[0] + '/init_module.py') == 0:
                for modules in os.walk(os.path.split(os.path.realpath(__file__))[0] + '/temp/'):
                    for module in modules[2]:
                        module_file = open(os.path.split(os.path.realpath(__file__))[0] + '/temp/' + module,'rb')
                        module = pickle.load(module_file)
                        into_modules[str(module.__class__.__name__)] = module
        MODULES[module_type] = into_modules
        with open(os.path.split(os.path.realpath(__file__))[0] + '/init_module.py', 'w+') as f:
            f.truncate()
            f.write('')
            f.close()
        os.system('rm -rf '+ os.path.split(os.path.realpath(__file__))[0] + '/temp/*')
    if os.system('python3 ' + os.path.split(os.path.realpath(__file__))[0] + '/webserver/manage.py migrate >> event_log.txt') == 0:
        return
    else:
        print(Fore.RED + '[-]程序初始化失败,请检查event_log.txt' + Fore.RESET)

def banner():
    print(Style.BRIGHT + ' _____  _   _  _____ _      _____ _____ ')
    print(Style.BRIGHT + '/  __ \| | | ||  ___| |    |  ___|_   _|')
    print(Style.BRIGHT + '| /  \/| |_| || |__ | |    | |__   | |  ')
    print(Style.BRIGHT + '| |    |  _  ||  __|| |    |  __|  | |  ')
    print(Style.BRIGHT + '| \__/\| | | || |___| |____| |___ _| |_ ')
    print(Style.BRIGHT + ' \____/\_| |_/\____/\_____/\____/ \___/ ')
    print(Style.BRIGHT + '                                        渗透工具套件v1.0 By:Gr33k')
    table = PrettyTable(border=False)
    table.header = False
    for module_type in MODULES.keys():
        table.add_row(['\t[------', module_type + ' ' + str(MODULES[module_type].keys().__len__()) + ' 个', '------]'])
    table.add_row(['\t[------',' show modules  查看模块 ','------]'])
    print(Fore.GREEN)
    print(table)
    print(Style.RESET_ALL)


def show_modules():
    print()
    print(Style.BRIGHT + '使用方法：use <模块目录>/<模块指令>')
    print(Style.BRIGHT + Fore.GREEN)
    table = PrettyTable(['模块目录','指令','模块名称'],border=False)
    for M in MODULES.keys():
        table.add_row([M + ':','',''])
        for module in MODULES[M].keys():
            table.add_row(['',MODULES[M][module].__class__.__name__,MODULES[M][module].name])
    print(table)
    print(Style.RESET_ALL)


def in_module_menu(handle:list):
    global MODULE
    global IS_SELECT
    global MODULE_NAME
    if handle[0] == "set" and handle.__len__() == 3:
        if handle[1] in MODULE.variables.keys():
            MODULE.set_variable(handle[1],handle[2])
            #variables[handle[1]] = handle[2]
        else:
            print(Fore.RED + '[-]未找到变量' + Style.RESET_ALL)
            return
    elif handle[0] == "back":
        IS_SELECT = 0
        MODULE = Base_module({'version':'','author':'','completion_time':'','name':''},[])
        MODULE_NAME = ""
    elif handle[0] == "start":
        MODULE.start()
    elif handle[0] == "show" and handle[1] == "options":
        MODULE.show_options()
    else:
        print(Fore.RED + '[-]未找到命令' + Style.RESET_ALL)


def main():
    global MODULE
    global IS_SELECT
    global MODULE_NAME
    global MODULE_TYPE
    start_init()
    banner()
    while True:
        if MODULE_NAME == "":
            command = input("Gr33k>")
        else:
            command = input("Gr33k>" + Style.BRIGHT + Fore.RED + '(' + MODULE_TYPE + '/' + MODULE_NAME + ')>' + Style.RESET_ALL)
        handle = command.split(" ")
        if command == "":
            continue
        elif command == "exit":
            os._exit(0)
        elif command == "show modules":
            show_modules()
        elif handle[0] == "use" and handle.__len__() == 2:
            module_type = handle[1].split('/')[0]
            module_name = handle[1].split('/')[1]
            try:
                if module_name in MODULES[module_type].keys():
                    MODULE_NAME = str(MODULES[module_type][module_name].__class__.__name__)
                    MODULE = MODULES[module_type][module_name]
                    MODULE_TYPE = module_type
                    IS_SELECT = 1
                else:
                    print(Fore.RED + '[-]找不到该模块' + Style.RESET_ALL)
            except:
                print(Fore.RED + '[-]找不到该模块' + Style.RESET_ALL)
        elif IS_SELECT == 1:
            in_module_menu(handle)
        else:
            print(Fore.RED + '[-]未找到命令' + Style.RESET_ALL)


if __name__ == '__main__':
    main()
