from django.shortcuts import render,redirect
from .models import *
from .forms import *

def home(request):
    table = todoform()
    val = activity.objects.all()

    if request.method == 'POST':
        table = todoform(request.POST)
        if table.is_valid():
            table.save()
        return redirect('/')

    return render(request,'task/home.html',{'context':val ,'form':table})

def update_task(request,pk):
    item = activity.objects.get(id=pk) 

    form = todoform(instance=item)

    if request.method=="POST":
        form = todoform(request.POST,instance=item)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request,'task/update.html',{'form':form})

def delete(request,pk):
    item = activity.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/') 

       
    return render(request,'task/delete.html',{'item':item})


