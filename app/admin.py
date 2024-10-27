from django.contrib import admin
from .models import Department, Subject, Teacher, Student

admin.site.register(Department)
admin.site.register(Subject)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('department', 'date_joined')
    filter_horizontal = ('subjects',)  # Enables a better UI for many-to-many fields

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'roll_number', 'department')
    search_fields = ('first_name', 'last_name', 'email', 'roll_number')
    list_filter = ('department',)
    filter_horizontal = ('subjects',)
