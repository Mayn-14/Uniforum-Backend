from django.urls import path
from .views import answer_api, answer_restore, answer_upvote, answer_downvote


urlpatterns = [
    path('answer/<int:id>', answer_api, name='answer_api'),
    path('answer-restore/<int:id>', answer_restore, name='answer-restore'),
    path('answer-upvote/<int:id>', answer_upvote, name='answer-upvote'),
    path('answer-downvote/<int:id>', answer_downvote, name='answer-downvote'),
]    
