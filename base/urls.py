from django.urls import path
from .views import login, group_listing, register,logout , StudentApiView, TeacherApiView, ClassApiView, ScheduleApiView, AcademicRecordApiView, ExamApiView, GradeApiView, AttendenceApiView, SubjectApiView, AssignmentApiView, AssignmentSubmissionApiView

urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('roles/',group_listing),
    path('logout/', logout, name='logout'),

    path('student/',StudentApiView.as_view({'get':'list','post':'create'}),name='student'),
    path('student/<int:pk>/',StudentApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='student-detail'),
    path('teacher/',TeacherApiView.as_view({'get':'list','post':'create'}),name='teacher'),
    path('teacher/<int:pk>/',TeacherApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='teacher-detail'),
    path('class/',ClassApiView.as_view({'get':'list','post':'create'}),name='class'),
    path('class/<int:pk>/',ClassApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='class-detail'),
    path('schedule/',ScheduleApiView.as_view({'get':'list','post':'create'}),name='schedule'),
    path('schedule/<int:pk>/',ScheduleApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='schedule-detail'),
    path('academic-records/',AcademicRecordApiView.as_view({'get':'list','post':'create'}),name='academic-record'),
    path('academic-records/<int:pk>/',AcademicRecordApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='academic-record-detail'),
    path('exam/',ExamApiView.as_view({'get':'list','post':'create'}),name='exam'),
    path('exam/<int:pk>/',ExamApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='exam-detail'),
    path('grade/',GradeApiView.as_view({'get':'list','post':'create'}),name='grade'),
    path('grade/<int:pk>/',GradeApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='grade-detail'),
    path('attendence/',AttendenceApiView.as_view({'get':'list','post':'create'}),name='attendence'),
    path('attendence/<int:pk>/',AttendenceApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='attendence-detail'),
    path('subject/',SubjectApiView.as_view({'get':'list','post':'create'}),name='subject'),
    path('subject/<int:pk>/',SubjectApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='subject-detail'),
    path('assignment/',AssignmentApiView.as_view({'get':'list','post':'create'}),name='assignment'),
    path('assignment/<int:pk>/',AssignmentApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='assignment-detail'),
    path('assignment/submission/',AssignmentSubmissionApiView.as_view({'get':'list','post':'create'}),name='assignment-submission'),
    path('assignment/submission/<int:pk>/',AssignmentSubmissionApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='assignment-submission-detail'),
]