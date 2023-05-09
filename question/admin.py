from django.contrib import admin
from .models import Question

@admin.register(Question)
class questionAdmin(admin.ModelAdmin):
    fields = ("question", "user")
    list_display = ("question", "question_slug", "views", "answer_count", "isdeleted", "deleted_at", "created_at", "user")
    list_filter = ("isdeleted",)
    search_fields = ("question__startswith",)
    ordering = ("question",)

    def __str__(self):
        return self.question
