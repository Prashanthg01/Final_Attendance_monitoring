# attendance/models.py
from django.db import models

class Student(models.Model):
    BRANCH_CHOICES = [
        ('ECE', 'Electronics and Communication Engineering'),
        ('CSE', 'Computer Science Engineering'),
        ('ISE', 'Information Science Engineering'),
        ('MEC', 'Mechanical Engineering'),
        ('CIVIL', 'Civil Engineering')
    ]
    GENDER_CHOICE = [
        ('MALE', 'male'),
        ('FEMALE', 'female'),
        ('OTHERS', 'others')
    ]
    SEMESTER_CHOICE = [
        ('1SEM', '1st sem'),
        ('2SEM', '2nd sem'),
        ('3SEM', '3rd sem'),
        ('4SEM', '4th sem'),
        ('5SEM', '5th sem'),
        ('6SEM', '6th sem'),
        ('7SEM', '7th sem'),
        ('8SEM', '8th sem')
    ]
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICE)
    guardian_name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=50)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    academic_year = models.CharField(max_length=50)
    semister = models.CharField(max_length=20, choices=SEMESTER_CHOICE)
    section = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    guardian_phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class Attendance(models.Model):
    BRANCH_CHOICES = [
        ('ECE', 'Electronics and Communication Engineering'),
        ('CSE', 'Computer Science Engineering'),
        ('ISE', 'Information Science Engineering'),
        ('MEC', 'Mechanical Engineering'),
        ('CIVIL', 'Civil Engineering')
    ]
    SEMESTER_CHOICE = [
        ('1SEM', '1st sem'),
        ('2SEM', '2nd sem'),
        ('3SEM', '3rd sem'),
        ('4SEM', '4th sem'),
        ('5SEM', '5th sem'),
        ('6SEM', '6th sem'),
        ('7SEM', '7th sem'),
        ('8SEM', '8th sem')
    ]
    CLASS_CHOICES = (
        ('1', 'Class 1'),
        ('2', 'Class 2'),
        ('3', 'Class 3'),
        # add more choices as needed
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    datee = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    subject_code = models.CharField(max_length=255)
    session = models.CharField(max_length=20)
    roll_number = models.CharField(max_length=50)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    academic_year = models.CharField(max_length=50)
    semister = models.CharField(max_length=20, choices=SEMESTER_CHOICE)
    section = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.student.name} - {self.date}'
