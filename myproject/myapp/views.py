from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

# Create your views here.

def home(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            form.save()  
            print("saved !")
            return redirect("/home")
    else:  
        form = StudentForm()  
    return render(request,'home.html', {'form':form})  

def show(request):  
    stu = Student.objects.all()  
    return render(request,"show.html", {'stu':stu})  

def updatedata(request, id):
    stu = Student.objects.get(id=id)  
    if request.method == "POST":  
        form = StudentForm(request.POST, instance=stu)  
        if form.is_valid():  
            form.save()  
            print("saved !")
            return redirect("/show")
    else:  
        form = StudentForm(instance=stu)  
    return render(request,'home.html', {'form':form})  

def destroy(request, id):  
    stu = Student.objects.get(id=id)  
    stu.delete()  
    return redirect("/show")  