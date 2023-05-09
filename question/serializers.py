from rest_framework import serializers
from .models import Question
from answer.serializers import answerSerializer

class questionSerializer(serializers.ModelSerializer):
    answers = answerSerializer(many=True, read_only=True)
    user_name = serializers.CharField(source='user.name')
    user_image = serializers.ImageField(source='user.picture')
    class Meta:
        model = Question
        fields = ['id', 'question', 'question_slug', 'views', 'follow_count', 'answer_count', 'isdeleted', 'deleted_at', 'created_at', 'user', 'user_name', 'user_image', 'answers']
        read_only_fields = ['id',]
