# to run django files : cd ccn
# python3 manage.py runserver

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings
from .models import  Module
from django.db.models import Q
from django.contrib import messages

def index(request):
    return render(request,'website/index.html')

def module(request):

    module_contains = Module.objects.all()

    return render(request,'website/module1.html',{ 'module_contains' : module_contains})

def dynamic(request,model_class, mod_no, sub_modno):

    print(model_class, mod_no, sub_modno)

    details = Module.objects.filter(Q(module_options=model_class) & Q(module_numbering=mod_no) & Q(module_subtitle_numbering=sub_modno))

    return render(request,'website/dynamic.html',{'details':details})

def module2(request):
    return render(request,'website/module2.html')

def module3(request):
    return render(request,'website/module3.html')

def module4(request):
    return render(request,'website/module4.html')

def module5(request):
    return render(request,'website/module5.html')

def module6(request):
    return render(request,'website/module6.html')

def search(request):

    query=request.GET['query']
    query = query.lower().replace(" " , '')

    if query == '':
        messages.success(request, 'Enter a Search Query!')
        return redirect('index')

    elif query == 'module1':
        return redirect('module')
    
    elif query == 'module2':
        return redirect('module2')
    
    elif query == 'module3':
        return redirect('module3')

    elif query == 'module4':
        return redirect('module4')
    
    elif query == 'module5':
        return redirect('module5')
    
    elif query == 'module6':
        return redirect('module6')

    else :
        module_details = Module.objects.filter(Q(module_numbering_title__icontains=query) | Q(module_numbering_subtitle__icontains=query))

    return render(request,'website/search.html',{'module_details': module_details,'query': query })