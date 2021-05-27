
from os import name
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("login", views.login_page, name='login_page'),
    path("logout", views.logout_user, name='logout_user'),
    path("register", views.register, name='register'),

    path("register/student_admin", views.register_student_admin,
         name='register_student_admin'),
    path("register/student_user", views.register_student_user,
         name='register_student_user'),
    path("register/teacher_admin", views.register_teacher_admin,
         name='register_teacher_admin'),
    path("register/teacher_user", views.register_teacher_user,
         name='register_teacher_user'),
    path("student_users", views.view_students,
         name='student_users'),
    path("student_admins", views.view_student_admin,
         name='student_admins'),
    path("teacher_users", views.view_teachers,
         name='teacher_users'),
    path("teacher_admins", views.view_teacher_admin,
         name='teacher_admins'),

    path("master_admins", views.view_master_admins,
         name='master_admins'),
    path("delete/<int:id>/", views.delete_user,
         name='delete_users'),

    path("update/<int:id>/", views.update_user,
         name='update_user'),
    path('profile/', views.user_profile, name='user_profile'),

    path('restapi/student_user_list',
         views.student_user_list, name='student_user_list'),
    path('restapi/student_user_reg',
         views.student_user_reg, name='student_user_reg'),

    path('restapi/student_admin_list',
         views.student_admin_list, name='student_admin_list'),

    path('restapi/student_admin_reg',
         views.student_admin_reg, name='student_admin_reg'),

    path('restapi/teacher_user_list',
         views.teacher_user_list, name='teacher_user_list'),
    path('restapi/teacher_user_reg',
         views.teacher_user_reg, name='teacher_user_reg'),

    path('restapi/teacher_admin_list',
         views.teacher_admin_list, name='teacher_admin_list'),

    path('restapi/teacher_admin_reg',
         views.teacher_admin_reg, name='teacher_admin_reg'),
    path('restapi/user_details/<int:pk>',
         views.user_details, name='user_details'),



]
