from django.urls import path
from attendance.views import home, result, classresult, attendance_by_month, add_student, take_attendance

urlpatterns = [
    path('', home, name='home'),
    path('result/', result, name='result'),
    path('classresult/', classresult, name='classresult'),
    path('monthlyresult/', attendance_by_month, name='attendance_by_month'),
    path('Update_ia_marks/', add_student, name='add_student'),
    path('student_attendance/', take_attendance, name='take_attendance' ),
]
