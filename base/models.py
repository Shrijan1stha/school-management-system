from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.core.exceptions import ValidationError

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group)
    password = models.CharField(max_length=300)
    username = models.CharField(max_length=300, default='username')
    phone_no = models.IntegerField(unique=True,null=True)
    address = models.CharField(max_length=300,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_no', 'address']

class Classes(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
    
class Section(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class ClassSection(models.Model):
    class_name = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)
    section_name = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.class_name}-{self.section_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True, null=True)
    class_section = models.ForeignKey(ClassSection, on_delete=models.SET_NULL, null=True)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=200)

    def __str__(self):
        if self.middle_name is None:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = 'student'

class Subject(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(unique=True)
    email = models.EmailField(unique=True,max_length=200)
    classes = models.ManyToManyField(ClassSection)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        if self.middle_name is None:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = 'teacher'

class DayOfWeek(models.Model):
    name = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    ])

    def __str__(self):
        return self.name

class Schedule(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL,null=True)
    days_of_week = models.ManyToManyField(DayOfWeek)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        if self.teacher.middle_name is None:
            return f'{self.teacher.first_name} {self.teacher.last_name}'
        else:
            return f'{self.teacher.first_name} {self.teacher.middle_name} {self.teacher.last_name}'
    
class AcademicRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL,null=True)
    classes = models.ForeignKey(Classes, on_delete=models.SET_NULL,null=True)
    records = models.TextField()

    def __str__(self):
        return str(self.student)
    
class Exam(models.Model):
    exam_subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    exam_date = models.DateField()
    exam_time = models.TimeField()

    def __str__(self):
        return self.exam_subject.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)
    grade = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student} - {self.exam} - {self.grade}"
    
class Attendence(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    date = models.DateField()

    status = models.CharField(max_length=10, choices=[
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    ])

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"
    
class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_date = models.DateField()
    due_date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    class_assigned = models.ForeignKey(ClassSection, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title} class-{self.class_assigned}"
    
    def clean(self):
        if self.due_date < self.assigned_date:
            raise ValidationError('Submission date cannot be before assigned date')
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_date = models.DateField(null=True, blank=True)
    grade = models.CharField(max_length=5, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.assignment.title} - {self.student.first_name} {self.student.last_name}"