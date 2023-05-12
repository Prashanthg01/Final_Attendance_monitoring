# attendance/admin.py
from django.contrib import admin
from .models import Student, Attendance, IA_marks

admin.site.register(Student)
admin.site.register(IA_marks)
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'status', 'date')
