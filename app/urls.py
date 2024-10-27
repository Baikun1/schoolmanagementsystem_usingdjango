from django.urls import path

from . import views
urlpatterns =[
    path('',views.home,name='home'),
    path('department/create/', views.department_create, name='department_create'),
    path('subject/create/', views.subject_create, name='subject_create'),
    path('teacher/create/', views.teacher_create, name='teacher_create'),
    path('student/create/', views.student_create, name='student_create'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
]