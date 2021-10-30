from django.shortcuts import render,redirect
from student import forms
from student import models
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request,'home.html')


def afterlogin(request):
    students=models.student.objects.all()
    absentlist=[]
    for st in students:
        absentst=models.absentStudent.objects.filter(studentId=st.id)
        absentlist.append(absentst)

    return render(request,'adminhome.html',{'data':zip(students,absentlist)})

def registerAbsent(request):
    absentform=forms.absentStudentForm()
    mydict={'absentform':absentform}
    if request.method =='POST':
        absentform=forms.absentStudentForm(request.POST)
        if absentform.is_valid() :
            absentform.save()
                    # return HttpResponseRedirect(reverse('regAbsent'),mydict)
        return render(request,'successfuly.html')
    return render(request,'absentRegister.html',context=mydict)


def monthabsentSearch(request,month):
    reqmonth=month
    absentlist=models.absentStudent.objects.filter(month=reqmonth)
    students=[]
    for abs in absentlist:
        absentstudent=models.student.objects.filter(id=abs.studentId_id)
        students.append(absentstudent)
    return render (request,'monthabsent.html',{'data':zip(students,absentlist)})

def deleteabsent(request,pk):
    absentst=models.absentStudent.objects.get(id=pk)
    absentst.delete()
    return render(request,'deletesuccess.html')
