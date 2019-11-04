#encoding:utf8
from colorama import Style,Fore,init
from prettytable import PrettyTable

class Option():
    variable:str
    value:str
    description:str

    def __init__(self,variable:str,value:str,description:str):
        self.variable = variable
        self.value = value
        self.description = description

class Base_module():
    version:str
    author:str
    completion_time:str
    name:str
    options:list
    variables:dict

    def __init__(self,module_description:dict,options:list):
        self.version = module_description['version']
        self.author = module_description['author']
        self.completion_time = module_description['completion_time']
        self.name = module_description['name']
        self.options = []
        self.variables = {}


    def __del__(self):
        pass

    # def init_variable(self,options:list):
    #     for option in options:
    #         self.variables[option[0]] = option[1]
    #         self.options.append(Option(option[0],option[1],option[2]))

    def return_options(self,options:list):
        for option in options:
            self.options.append(Option(option[0], option[1], option[2]))
        return self.options

    def return_variables(self,options:list):
        for option in options:
            self.variables[option[0]] = option[1]
        return self.variables


    def set_variable(self,variable:str,value:str):
        if variable in self.variables.keys():
            self.variables[variable] = value
        else:
            print(Fore.RED + '[-]没有对应的变量名，请检查输入')

    def show_options(self):
        print()
        print(Style.BRIGHT + 'version:' + self.version)
        print(Style.BRIGHT + 'author:' + self.author)
        print(Style.BRIGHT + 'completion_time:' + self.completion_time)
        print()
        table = PrettyTable(["变量名", "值","描述"])
        for option in self.options:
            table.add_row([option.variable,self.variables[option.variable],option.description])
        print(table)

    def start(self):
        pass


