# attendance/admin.py
from django.contrib import admin
from .models import Student, Attendance

admin.site.register(Student)
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'status', 'date')
