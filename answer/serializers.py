from rest_framework import serializers
from .models import Answer

class answerSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name')
    user_image = serializers.ImageField(source='user.picture')
    class Meta:
        model = Answer
        fields = '__all__'
