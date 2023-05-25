from django.db import models
from customUser.models import Account
from question.models import Question
from django.utils import timezone
from ckeditor.fields import RichTextField

class Answer(models.Model):
    message = RichTextField()
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)
    totalvote = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    isdeleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    upvote = models.ManyToManyField(Account, related_name="upvote_answer")
    downvote = models.ManyToManyField(Account, related_name="downvote_answer")

    class Meta:
        ordering = ["-upvote_count"]
    

    def __str__(self):
        return self.message

    # def __iter__(self):
    #     return [
    #         self.message,
    #         self.upvote_count,
    #         self.downvote_count,
    #         self.totalvote,
    #         self.views,
    #         self.isdeleted,
    #         self.created_at,
    #         self.updated_at,
    #         self.user,
    #         self.question,
    #         self.upvote,
    #         self.downvote,
    #     ]

