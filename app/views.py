from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import DepartmentForm, SubjectForm, TeacherForm, StudentForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import LoginForm
from .models import Student, Teacher

def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            teacher = Teacher.objects.filter(email=email).first()
            if teacher and teacher.password == password:  
                request.session['user_role'] = 'teacher'
                request.session['user_id'] = teacher.id
                return redirect('teacher_dashboard')

            student = Student.objects.filter(email=email).first()
            if student and student.password == password: 
                request.session['user_role'] = 'student'
                request.session['user_id'] = student.id
                return redirect('student_dashboard')

            messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, 'home.html', {'form': form})

def teacher_dashboard(request):
    
    teacher_id = request.session.get('user_id')
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'teacher_dashboard.html', {'teacher': teacher})

def student_dashboard(request):
    student_id = request.session.get('user_id')
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_dashboard.html', {'student': student})


def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list') 
    else:
        form = DepartmentForm()
    return render(request, 'department_form.html', {'form': form})

def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'subject_form.html', {'form': form})

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teacher_form.html', {'form': form})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})
