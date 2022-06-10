from django.urls import path

from . import views

urlpatterns = [
    path('addstudent', views.addstudent, name = 'addstudent'),
    path('', views.home_main, name = 'homemain'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('searchattendence/', views.searchAttendence, name='searchattendence'),
    path('account/', views.facultyProfile, name='account'),
    path('updateStudentRedirect/', views.updateStudentRedirect, name='updateStudentRedirect'),
    path('updateStudent/', views.updateStudent, name='updateStudent'),
    path('attendence/', views.takeAttendence, name='attendence'),
]