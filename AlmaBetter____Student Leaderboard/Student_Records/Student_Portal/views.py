from django.shortcuts import render
from django.contrib import messages
from Student_Portal.models import AddStudent
from django.db.models import Sum


# Create your views here.
def home(request):
    return render(request, "Home.html")


def add(request):
    return render(request, "Add-student-record.html")

def leaderboard(request):
    addstudent = AddStudent.objects.all()
    return render(request, "Student-Leaderboard.html",{'addstudent':addstudent})

def added(request):
    if request.method == "POST":
        Tmarks = []
        Name = request.POST['Name']
        Rollno = request.POST['Rollno']
        Math = int(request.POST['Math'])
        print(Math)
        Physics = int(request.POST['Physics'])
        Chemistry = int(request.POST['Chemistry'])
        Tmarks = Math + Physics + Chemistry
        print(Tmarks)
        Percentage = round((Tmarks/300)*100,2)
        print(Percentage)
        clog = AddStudent(Chemistry = Chemistry,Physics = Physics, Math = Math,Rollno= Rollno,Name=Name,Tmarks=Tmarks,Percentage=Percentage)
        clog.save()
    return render(request, "Add-student-record.html")   
 