from django.contrib import admin
from .models import User, Student, Teacher, Classes, DayOfWeek, Schedule, AcademicRecord, Exam, Grade, Attendence, Subject, Assignment, AssignmentSubmission, Section, ClassSection

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
admin.site.register(Subject)
admin.site.register(Assignment)
admin.site.register(AssignmentSubmission)
admin.site.register(Section)
admin.site.register(ClassSection)