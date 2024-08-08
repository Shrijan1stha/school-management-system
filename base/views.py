from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User, Student, Teacher, Classes, Schedule, AcademicRecord, Exam, Grade, Attendence, Subject, Assignment, AssignmentSubmission
from .serializers import UserSerializer, GroupSerializer, StudentSerializer, TeacherSerializer, ClassSerializer, ScheduleSerializer, AcademicRecordSerializer, ExamSerializer, GradeSerializer, AttendenceSerializer, SubjectSerializer, AssignmentSerializer, AssignmentSubmissionSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, DjangoModelPermissions, IsAuthenticated
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAdminUser

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email,password=password)
    if user == None:
        return Response('Invalid Credentials!')
    else:
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def group_listing(request):
    objs = Group.objects.all()
    serializer = GroupSerializer(objs, many=True)
    return Response(serializer.data)
    
@api_view(['POSt'])
@permission_classes([IsAuthenticated, IsAdminUser])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')
        hash_password = make_password(password)
        a = serializer.save()
        a.password = hash_password
        a.save()
        return Response('User Created!')
    else:
        return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        request.user.auth_token.delete()
        return Response({"detail": "Successfully logged out."}, status=200)
    except:
        return Response({"detail": "Something went wrong."}, status=400)

class StudentApiView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filterset_fields = []
    search_fields = ['first_name', 'last_name', 'academic_record']

class TeacherApiView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    search_fields = ['first_name','middle_name','last_name','phone_number']

class ClassApiView(ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class ScheduleApiView(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filterset_fields = ['teacher', 'days_of_week']

class AcademicRecordApiView(ModelViewSet):
    queryset = AcademicRecord.objects.all()
    serializer_class = AcademicRecordSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filterset_fields = ['student','classes']
    search_fields = ['records']

class ExamApiView(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filterset_fields = ['exam_subject']
    search_fields = ['exam_subject']

class GradeApiView(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filterset_fields = ['student','exam']

class AttendenceApiView(ModelViewSet):
    queryset = Attendence.objects.all()
    serializer_class = AttendenceSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filterset_fields = ['date', 'status', 'student']

class SubjectApiView(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class AssignmentApiView(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentSubmissionApiView(ModelViewSet):
    queryset = AssignmentSubmission.objects.all()
    serializer_class = AssignmentSubmissionSerializer