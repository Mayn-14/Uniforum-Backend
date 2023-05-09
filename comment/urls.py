from django.urls import path
from .views import questionComment_api, answerComment_api, questionComment_upvote, questionComment_downvote, answerComment_upvote, answerComment_downvote
# question_upvote, question_downvote

urlpatterns = [
    path('question-comment/<int:id>', questionComment_api, name='questionComment-api'),
    path('answer-comment/<int:id>', answerComment_api, name='answerComment-api'),
    path('question-comment-upvote/<int:id>', questionComment_upvote, name='questionComment-upvote'),
    path('question-comment-downvote/<int:id>', questionComment_downvote, name='questionComment-downvote'),
    path('answer-comment-upvote/<int:id>', answerComment_upvote, name='answerComment-upvote'),
    path('answer-comment-downvote/<int:id>', answerComment_downvote, name='answerComment-downvote'),
]    
