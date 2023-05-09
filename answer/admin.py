from django.contrib import admin
from .models import Answer

@admin.register(Answer)
class answerAdmin(admin.ModelAdmin):
    fields = ("message", "user", "question")
    list_display = ("message", "upvote_count", "downvote_count","totalvote", "views", "isdeleted", "created_at", "updated_at", "user", "question")
    list_filter = ("isdeleted",)
    search_fields = ("message__startswith",)
    ordering = ("message",)

    def __str__(self):
        return self.answer