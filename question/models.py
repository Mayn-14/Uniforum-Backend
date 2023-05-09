from django.db import models
from django.template.defaultfilters import slugify
from customUser.models import Account
from django.urls import reverse
from django.utils import timezone

class Question(models.Model):
    question = models.CharField(max_length=255, null=False, unique=True)
    question_slug = models.SlugField(null=True, unique=True)
    views = models.IntegerField(default=0)
    follow_count = models.IntegerField(default=0)
    answer_count = models.IntegerField(default=0)
    isdeleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.question_slug})

    def save(self, *args, **kwargs):  # new
        if not self.question_slug:
            self.question_slug = slugify(self.question)
        return super().save(*args, **kwargs)
