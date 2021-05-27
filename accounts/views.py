
from rest_framework import serializers, status
from .models import Student, Teacher, TeacherAdmin, StudentAdmin
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .serializers import UserSerializer, StudentUserSerializer, StudentAdminSerializer, TeacherAdminSerializer, TeacherUserSerializer, UserDetailSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@login_required(login_url='/login')
def home(request):
    current_user = request.user
    user = User.objects.get(pk=current_user.id)
    params = {
        'user': user
    }
    return render(request, "home.html", params)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Successfully")
            return redirect('home')
        else:
            messages.error(request, "User Name or Password was incorrect")
            return render(request, "login.html")

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Logged Out Successfully")
    return redirect('login_page')


@login_required(login_url='/login')
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='MasterAdmin')
            user.groups.add(group)
            messages.success(request, "Account Is Created Successfully")
            return redirect('home')

    params = {
        'form': form
    }
    return render(request, "register.html", params)


@login_required(login_url='/login')
def register_teacher_admin(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='TeacherAdmin')
            user.groups.add(group)
            TeacherAdmin.objects.create(user=user,)
            messages.success(request, "Account Is Created Successfully")
            return redirect('home')

    params = {
        'form': form
    }
    return render(request, "teacher_admin_register.html", params)


@login_required(login_url='/login')
def register_student_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='StudentUser')
            user.groups.add(group)
            Student.objects.create(user=user,)
            messages.success(request, "Account Is Created Successfully")
            return redirect('home')

    params = {
        'form': form
    }
    return render(request, "student_user_register.html", params)


@login_required(login_url='/login')
def register_student_admin(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='StudentAdmin')
            user.groups.add(group)
            StudentAdmin.objects.create(user=user,)
            messages.success(request, "Account Is Created Successfully")
            return redirect('home')

    params = {
        'form': form
    }
    return render(request, "student_admin_register.html", params)


@login_required(login_url='/login')
def register_teacher_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='StudentAdmin')
            user.groups.add(group)
            Teacher.objects.create(user=user,)
            messages.success(request, "Account Is Created Successfully")
            return redirect('home')

    params = {
        'form': form
    }
    return render(request, "teacher_user_register.html", params)


@login_required(login_url='/login')
def view_students(request):
    users = User.objects.filter(groups__name='StudentUser')
    params = {
        'users': users
    }
    return render(request, 'student_users.html', params)


@login_required(login_url='/login')
def view_student_admin(request):
    users = User.objects.filter(groups__name='StudentAdmin')
    params = {
        'users': users
    }
    return render(request, 'student_admins.html', params)


@login_required(login_url='/login')
def view_teachers(request):
    users = User.objects.filter(groups__name='TeacherUser')
    params = {
        'users': users
    }
    return render(request, 'teacher_users.html', params)


@login_required(login_url='/login')
def view_teacher_admin(request):
    users = User.objects.filter(groups__name='TeacherAdmin')
    params = {
        'users': users
    }
    return render(request, 'teacher_admins.html', params)


@login_required(login_url='/login')
def view_master_admins(request):
    users = User.objects.filter(groups__name='MasterAdmin')
    params = {
        'users': users
    }
    return render(request, 'master_admins.html', params)


"this is for Delete Users"


@login_required(login_url='/login')
def delete_user(request, id):
    if request.method == 'POST':
        obj = User.objects.get(pk=id)
        obj.delete()
        messages.warning(request, "Successfully Deleted")
        return HttpResponseRedirect('/')


@login_required(login_url='/login')
def update_user(request, id):
    if request.method == 'POST':
        obj = User.objects.get(pk=id)
        form = CreateUserForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, " Information Updated Successfully")
            return redirect('home')
    else:
        obj = User.objects.get(pk=id)
        form = CreateUserForm(request.POST, instance=obj)
    params = {
        'form': form,
        'user': obj
    }
    return render(request, 'update_user.html', params)


@login_required(login_url='/login')
def user_profile(request):
    current_user = request.user
    user = User.objects.get(pk=current_user.id)
    params = {
        'user': user
    }
    return render(request, 'user_profile.html', params)


" REST API Views  "


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_user_list(request):
    if request.method == 'GET':
        user = User.objects.filter(groups__name='StudentUser')
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_admin_list(request):
    if request.method == 'GET':
        user = User.objects.filter(groups__name='StudentAdmin')
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def teacher_user_list(request):
    if request.method == 'GET':
        user = User.objects.filter(groups__name='TeacherUser')
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def teacher_admin_list(request):
    if request.method == 'GET':
        user = User.objects.filter(groups__name='TeacherAdmin')
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_user_reg(request):
    if request.method == 'POST':
        serializer = StudentUserSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully registered new user"
            data['username'] = user.username
            data['email'] = user.email
            return Response(serializer.data, status=201)
        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_admin_reg(request):
    if request.method == 'POST':
        serializer = StudentAdminSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully registered new user"
            data['username'] = user.username
            data['email'] = user.email
            return Response(serializer.data, status=201)
        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def teacher_user_reg(request):
    if request.method == 'POST':
        serializer = TeacherUserSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully registered new user"
            data['username'] = user.username
            data['email'] = user.email
            return Response(serializer.data, status=201)
        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def teacher_admin_reg(request):
    if request.method == 'POST':
        serializer = TeacherAdminSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully registered new user"
            data['username'] = user.username
            data['email'] = user.email
            return Response(serializer.data, status=201)
        else:
            data = serializer.errors
        return Response(data)


"""
GET USER using primary key

 """


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def user_details(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserDetailSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
