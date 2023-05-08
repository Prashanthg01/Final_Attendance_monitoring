# attendance/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Attendance


def home(request):
    num_students = Student.objects.count()
    num_branch_ece = Student.objects.filter(branch='ECE').count()
    num_branch_cse = Student.objects.filter(branch='CSE').count()
    num_branch_ise = Student.objects.filter(branch='ISE').count()
    num_branch_mech = Student.objects.filter(branch='MEC').count()
    num_branch_civil = Student.objects.filter(branch='CIVIL').count()
    num_gender_male = Student.objects.filter(gender='MALE').count()
    num_gender_female = Student.objects.filter(gender='FEMALE').count()
    num_gender_others = Student.objects.filter(gender='OTHERS').count()
    num_section = Student.objects.count()
    num_sem = Student.objects.count()
    academic_year = request.GET.get('academic_year')
    semister = request.GET.get('semister')
    section = request.GET.get('section')
    branch = request.GET.get('branch')
    students = Student.objects.filter(academic_year=academic_year, semister=semister, section=section, branch=branch)
    attendance_records = []
    subject_code = ''
    session = ''
    datee = ''
    branch = ''

    if request.method == 'POST':
        subject_code = request.POST.get('subject_code')
        session = request.POST.get('session')
        datee = request.POST.get('datee')
        for student in students:
            is_present = request.POST.get(f'student-{student.id}', False)
            roll_number = student.roll_number
            academic_year = student.academic_year
            semister = student.semister
            branch = student.branch
            section = student.section
            Attendance.objects.create(student=student, roll_number=roll_number, section=section, branch=branch, academic_year=academic_year, semister=semister, status=is_present, subject_code=subject_code, session=session, datee=datee)
        messages.success(request, 'Attendance has been submitted successfully!')
        return redirect('home')

    if subject_code and session and datee:
        attendance_records = Attendance.objects.filter(subject_code=subject_code, session=session, datee=datee)
    
    return render(request, 'attendance/home.html', {
        'students': students,
        'attendance_records': attendance_records,
        'subject_code': subject_code,
        'datee': datee,
        'session': session,
        'num_students': num_students,
        'num_section': num_section,
        'num_sem': num_sem,
        'num_branch_ece': num_branch_ece,
        'num_branch_cse': num_branch_cse,
        'num_branch_ise': num_branch_ise,
        'num_branch_mech': num_branch_mech,
        'num_branch_civil': num_branch_civil,
        'num_gender_male': num_gender_male,
        'num_gender_female': num_gender_female,
        'num_gender_others': num_gender_others
    })

def result(request):
    if request.method == 'POST':
        subject_code = request.POST.get('subject_code')
        roll_number = request.POST.get('roll_number')
        attendances = Attendance.objects.filter(subject_code=subject_code, roll_number=roll_number)
        num_presents = attendances.filter(status=True).count()
        num_absents = attendances.filter(status=False).count()
        context = {'attendances': attendances, 'subject_code': subject_code, 'roll_number': roll_number, 
                   'num_presents': num_presents, 'num_absents': num_absents}
        return render(request, 'attendance/result.html', context)
    return render(request, 'attendance/result.html')

def classresult(request):
    if request.method == 'POST':
        subject_code = request.POST.get('subject_code')
        session = request.POST.get('session')
        datee = request.POST.get('datee')
        attendances = Attendance.objects.filter(subject_code=subject_code, session=session, datee=datee)
        return render(request, 'attendance/classresult.html', {'attendances': attendances, 'session': session, 'datee': datee})
    return render(request, 'attendance/classresult.html')

def attendance_by_month(request):
    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        semister = request.POST.get('semister')
        academic_year = request.POST.get('academic_year')
        branch = request.POST.get('branch')
        attendances = Attendance.objects.filter(datee__range=[start_date, end_date], branch=branch, academic_year=academic_year, semister=semister).order_by('-datee')
        return render(request, 'attendance/month.html', {
            'attendances': attendances,
            'start_date': start_date,
            'end_date': end_date
        })
    return render(request, 'attendance/month.html')
