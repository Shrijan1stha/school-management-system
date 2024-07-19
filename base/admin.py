from django.contrib import admin
from .models import User, Student, Teacher, Classes, DayOfWeek, Schedule, AcademicRecord, Exam, Grade, Attendence

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Classes)
admin.site.register(DayOfWeek)
admin.site.register(Schedule)
admin.site.register(AcademicRecord)
admin.site.register(Exam)
admin.site.register(Grade)
admin.site.register(Attendence)