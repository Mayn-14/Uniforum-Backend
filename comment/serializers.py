from rest_framework import serializers
from .models import QuestionComment, AnswerComment

class questionCommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name')
    user_image = serializers.ImageField(source='user.picture')
    class Meta:
        model = QuestionComment
        fields = '__all__'

class answerCommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name')
    user_image = serializers.ImageField(source='user.picture')
    class Meta:
        model = AnswerComment
        fields = '__all__'