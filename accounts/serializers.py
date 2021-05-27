from rest_framework import serializers
from django.contrib.auth.models import Group, User
from .models import Student, Teacher, TeacherAdmin, StudentAdmin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name', 'email', 'groups')


class StudentUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        group = Group.objects.get(name='StudentUser')
        user.groups.add(group)
        Student.objects.create(user=user,)
        return user


class StudentAdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        group = Group.objects.get(name='StudentAdmin')
        user.groups.add(group)
        Student.objects.create(user=user,)
        return user


class TeacherUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        group = Group.objects.get(name='TeacherUser')
        user.groups.add(group)
        Student.objects.create(user=user,)
        return user


class TeacherAdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        group = Group.objects.get(name='TeacherAdmin')
        user.groups.add(group)
        Student.objects.create(user=user,)
        return user
