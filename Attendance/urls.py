from django.urls import path
from .views import * # Import the necessary view classes

urlpatterns = [
    path('departments/', DepartmentAPI.as_view(), name='department'),
    path('students/', StudentAPI.as_view(), name='student'),
    path('Course/',CourseAPI.as_view(),name='course'),
    path('Attendance_log/',Attendance_logAPI.as_view(),name='Attendance_log'),
    path('departments/<int:id>/', DepartmentAPI.as_view(), name='department-api'),
    path('Course/<int:id>/', CourseAPI.as_view(), name='course-api'),
    path('Students/<int:id>/', StudentAPI.as_view(), name='student-api'),
    path('Attendance_log/<int:id>/', Attendance_logAPI.as_view(), name='Attendance_log-api'),


    # Other URL patterns
]
