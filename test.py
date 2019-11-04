import pickle

class A():

     def __init__(self):
         pass

     def print_str(self):
         print('666')

# a = A()
with open('a.pickle','rb') as f:
    data = f.read()
    a = pickle.loads(data)
    a.print_str()