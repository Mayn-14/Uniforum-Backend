from django.contrib import admin
from .models import QuestionComment, AnswerComment

@admin.register(QuestionComment)
class questionCommentAdmin(admin.ModelAdmin):
    fields = ("message", "user", "question", "parent")
    list_display = ("message", "upvote_count", "downvote_count","totalvote", "isdeleted", "created_at", "updated_at", "user",  "question", "parent")
    list_filter = ("isdeleted",)
    search_fields = ("message__startswith",)
    ordering = ("message",)

    def __str__(self):
        return self.message
    
@admin.register(AnswerComment)
class answerCommentAdmin(admin.ModelAdmin):
    fields = ("message", "user", "answer", "parent")
    list_display = ("message", "upvote_count", "downvote_count", "totalvote", "isdeleted", "created_at", "updated_at", "user",  "answer", "parent")
    list_filter = ("isdeleted",)
    search_fields = ("message__startswith",)
    ordering = ("message",)

    def __str__(self):
        return self.message
    
