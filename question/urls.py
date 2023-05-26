from django.urls import path
from .views import question_api, api_routes, question_restore, recommended_question
# question_upvote, question_downvote

urlpatterns = [
    path('', api_routes, name='api-routes'),
    path('question/<slug:slug>', question_api, name='question-slug'),
    path('question', question_api, name='question'),
    path('question-restore/<slug:slug>', question_restore, name='question-restore'),
    path('recommended-question', recommended_question, name='recommended-question'),
    # path('question-upvote/<slug:slug>', question_upvote, name='question_upvote'),
    # path('question-downvote/<slug:slug>', question_downvote, name='question_downvote'),
]    
