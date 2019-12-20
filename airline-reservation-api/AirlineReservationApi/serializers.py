from django.contrib.auth.models import User,Group
from rest_framework import serializers
from django.forms import widgets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']

# 회원가입 API
class RegisterSerializer(serializers.Serializer):
    pk = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    main_address = serializers.CharField(max_length=500)
    sub_address = serializers.CharField(max_length=500)
    company = serializers.CharField(max_length=200)
    depart =  serializers.CharField(max_length=200)
    position = serializers.CharField(max_length=200)

#운항스케쥴 API
class AirscheduleSerializer(serializers.Serializer):
    pk = serializers.ReadOnlyField()
    arrival_time = serializers.DateTimeField()
    departure_time = serializers.DateTimeField()
    navigation_section = serializers.CharField(max_length=500)
    operating_time = serializers.CharField(max_length=100)
    airplane_type = serializers.CharField(max_length=100)


def restore_object(self, attrs, instance=None):
    if instance:
        instance.name = attrs.get('name',instance.name)
        instance.password = attrs.get('password',instance.password)
        instance.main_address = attrs.get('main_address',instance.main_address)
        instance.sub_address = attrs.get('sub_address', instance.sub_address)
        instance.company = attrs.get('company', instance.company)
        instance.depart = attrs.get('depart', instance.depart)
        instance.position = attrs.get('position', instance.position)
        instance.arrival_time = attrs.get('arrival_time',instance.arrival_time)
        instance.departure_time = attrs.get('departure_time',instance.departure_time)
        instance.navigation_time = attrs.get('navigation_time', instance.navigation_time)
        instance.operating_time = attrs.get('operation_time', instance.operating_time)
        instance.airplane_type = attrs.get('airplane_type', instance.airplane_type)
        return instance
        return Register(**attrs)





