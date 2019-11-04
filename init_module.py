import os
import pickle
from lib.exploit.Struts2 import Struts2

struts2= Struts2()
struts2_module = pickle.dumps(struts2)
f =  open(os.path.split(os.path.realpath(__file__))[0] + '/temp/struts2.module','wb')
f.write(struts2_module)
f.close()

