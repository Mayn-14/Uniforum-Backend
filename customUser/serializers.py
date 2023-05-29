from rest_framework import serializers
from .models import Account
from university.serializers import ProgrammeSerializer

class AccountSerializer(serializers.ModelSerializer):
    roll_no = serializers.CharField(source='studentDetail.roll_no', read_only=True)
    programme = serializers.CharField(source='studentDetail.programme.programme_name', read_only=True)
    dept = serializers.CharField(source='studentDetail.programme.dept.department_name', read_only=True)
    school = serializers.CharField(source='studentDetail.programme.dept.school.school_name', read_only=True)
    class Meta:
        model = Account
        fields = [  'email',
                    'name',
                    'date_of_birth',
                    'picture',
                    'aboutme',
                    'followercount',
                    'followingcount',
                    'roll_no',
                    'programme',
                    'dept',
                    'school',
                    ]