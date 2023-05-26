from rest_framework import serializers
from .models import QuestionComment, AnswerComment

class questionCommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name')
    user_image = serializers.ImageField(source='user.picture')
    # hasUpvoted = serializers.BooleanField(source='has_upvoted')
    # hasDownvoted = serializers.BooleanField(source='has_downvoted')
    class Meta:
        model = QuestionComment
        fields = '__all__'

class answerCommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name')
    user_image = serializers.ImageField(source='user.picture')
    # hasUpvoted = serializers.BooleanField(source='has_upvoted')
    # hasDownvoted = serializers.BooleanField(source='has_downvoted')
    class Meta:
        model = AnswerComment
        fields = '__all__'