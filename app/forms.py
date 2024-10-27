from django import forms
from .models import Department, Subject, Teacher, Student

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'code', 'description']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'code', 'description', 'department']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name', 'last_name', 'email', 'phone_number', 'department', 'subjects', 'date_joined', 'profile_picture'
        ]
        widgets = {
            'subjects': forms.CheckboxSelectMultiple() 
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'email',
            'roll_number',
            'department',
            'subjects',
            'date_of_birth',
            'profile_picture',
            'required_document'
        ]
        widgets = {
            'subjects': forms.CheckboxSelectMultiple(),

        }
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)