from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.db.models.fields import CharField

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, )
    name = models.CharField(max_length=200, null=True)
    student_id = models.CharField(max_length=20, null=True, unique=True)
    dep = models.CharField(max_length=20, null=True)
    sem = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.TextField(max_length=200, null=True)
    cgpa = models.FloatField(max_length=200, null=True)

    def __str__(self):
        return self.user.username


class StudentAdmin(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, )
    name = models.CharField(max_length=200, null=True)
    student_id = models.CharField(max_length=20, null=True, unique=True)
    dep = models.CharField(max_length=20, null=True)
    sem = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.TextField(max_length=200, null=True)
    cgpa = models.FloatField(max_length=200, null=True)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE,)
    name = models.CharField(max_length=200, null=True)
    teacher_id = models.CharField(max_length=200, null=True, unique=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.user.username


class TeacherAdmin(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE,)
    name = models.CharField(max_length=200, null=True)
    teacher_id = models.CharField(max_length=200, null=True, unique=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.user.username


class Book(models.Model):
    name = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=50, null=True)
    for_class = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.name
