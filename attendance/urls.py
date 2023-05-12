from django.urls import path
from attendance.views import home, result, classresult, attendance_by_month, add_student

urlpatterns = [
    path('', home, name='home'),
    path('result/', result, name='result'),
    path('classresult/', classresult, name='classresult'),
    path('monthlyresult/', attendance_by_month, name='attendance_by_month'),
    path('add_student/', add_student, name='add_student'),
]
