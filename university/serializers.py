from .models import School, Department, Programme, Student
from rest_framework import serializers

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        object = School
        fields = '__all__'

class DepartmentSerialzer(serializers.ModelSerializer):
    class Meta:
        object = Department
        fields = '__all__'

class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        object = Programme
        feilds = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        object = Student
        fields = '__all__'
