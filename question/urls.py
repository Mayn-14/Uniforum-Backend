from django.urls import path
from .views import question_api, api_routes, question_restore
# question_upvote, question_downvote

urlpatterns = [
    path('', api_routes, name='api-routes'),
    path('question/<slug:slug>', question_api, name='question-slug'),
    path('questions/', question_api, name='question'),
    path('question-restore/<slug:slug>', question_restore, name='question-restore'),
    # path('question-upvote/<slug:slug>', question_upvote, name='question_upvote'),
    # path('question-downvote/<slug:slug>', question_downvote, name='question_downvote'),
]    
