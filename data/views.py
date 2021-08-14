from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UnitForm
from .models import *
# Create your views here.



def index(request):
    return render(request,'dataBase/index.html')

def welcome(request):
    return render(request,'dataBase/welcome.html')


def about(request):
    return render(request,'dataBase/about.html')


#def createUnit(request):
 #   form = UnitForm()
  #  context ={'form':form}
   # return render(request,'dataBase/main.html',context)

def createUnit(request):
    form = UnitForm()
    if request.method == 'POST':
		#print('Printing POST:', request.POST)
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}        
    return render(request, 'dataBase/main.html', context)



def updateUnit(request):
    form = UnitForm()
    context = {'form':form}

    return render(request, 'dataBase/update.html', context)
 
def deleteUnit(request):
   
    if request.method == "POST":
        Unit.delete()
        return redirect('/')
        
    
    context = {'item':Unit}
    return render(request, 'dataBase/delete.html', context)