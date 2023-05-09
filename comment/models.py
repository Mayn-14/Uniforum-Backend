from django.db import models
from customUser.models import Account
from question.models import Question
from answer.models import Answer
from django.utils import timezone


class QuestionComment(models.Model):
    message = models.CharField(max_length=255, null=False)
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)
    totalvote = models.IntegerField(default=0)
    isdeleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="userDetail")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="questionComments")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    upvote = models.ManyToManyField(Account, related_name="upvote_question_comment")
    downvote = models.ManyToManyField(Account, related_name="downvote_question_comment")


    def __str__(self):
        return self.message
    
class AnswerComment(models.Model):
    message = models.CharField(max_length=255, null=False)
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)
    totalvote = models.IntegerField(default=0)
    isdeleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    upvote = models.ManyToManyField(Account, related_name="upvote_answer_comment")
    downvote = models.ManyToManyField(Account, related_name="downvote_answer_comment")


    def __str__(self):
        return self.message
