from django import forms
from . import models
from django.contrib.auth.models import User

class studentForm(forms.ModelForm):
    class Meta:
        model=models.student
        fields=['fullname']

class classNumberForm(forms.ModelForm):
    class Meta:
        model=models.classNumber
        fields=['classname']
class absentStudentForm(forms.ModelForm):
    class Meta:
        model=models.absentStudent
        fields=['day','month','year','description','delay','studentId']        
        labels={'description':'توضیحات','delay':'تاخیر یا غیبت','studentId':'نام دانش آموز'}
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        labels={'username':'نام کاربری','password':'رمز ورود'}
        widgets = {
        'password': forms.PasswordInput()
        }
