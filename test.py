import os

for modules in os.walk(os.path.split(os.path.realpath(__file__))[0] + '/temp/'):
    print(modules)