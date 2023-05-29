from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import F
from .models import Answer
from .serializers import answerSerializer
from rest_framework_simplejwt.backends import TokenBackend
from customUser.models import Account
from question.models import Question


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def answer_api(request, id=None):
    # if request.method == 'GET':
    #     if slug is not None:
    #         answer = Answer.objects.get(question_slug=slug)
    #         answer.views=F("views") + 1
    #         answer.save()
    #         answer.refresh_from_db()
    #         serializer = answerSerializer(question)
    #         return Response(serializer.data)

    #     question = Answer.objects.all()
    #     answer = answerSerializer(question, many=True)
    #     return Response(serializer.data)

    if request.method == 'POST':
        question = Question.objects.get(id=request.data['question'])
        question.answer_count = F('answer_count') + 1
        question.save()
        serializer = answerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Answer Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        answer = Answer.objects.get(id=id)
        serializer = answerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Answer Updated'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        answer = Answer.objects.filter(id=id).update(isdeleted=True)
        return Response({'msg': 'Answer Deleted'})
    

@api_view(['PUT'])
def answer_restore(request, id=None):
    if request.method == 'PUT':
        question = Answer.objects.filter(id=id).update(isdeleted=False)
        return Response({'msg': 'Answer Restored'})

@api_view(['PUT'])
def answer_upvote(request, id=None):
    answer = Answer.objects.get(id=id)
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
    user_id = valid_data['user_id']
    user = Account.objects.get(id=user_id)
    if not answer.upvote.through.objects.filter(account_id=user).exists():
        answer.upvote.add(user)
        answer.upvote_count = F("upvote_count") + 1
        answer.totalvote = F("totalvote") + 1
        answer.save()
        answer.refresh_from_db()
        return Response({'msg': 'answer upvoted'})
    else:
        answer.upvote.remove(user)
        answer.upvote_count = F("upvote_count") - 1
        answer.totalvote = F("totalvote") - 1
        answer.save()
        answer.refresh_from_db()
    return Response({'msg': 'answer upvoted undo'})
        

@api_view(['PUT'])
def answer_downvote(request, id=None):
    answer = Answer.objects.get(id=id)
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
    user_id = valid_data['user_id']
    user = Account.objects.get(id=user_id)
    if not answer.downvote.through.objects.filter(account_id=user).exists():
        answer.downvote.add(user)
        answer.downvote_count = F("downvote_count") + 1
        answer.totalvote = F("totalvote") + 1
        answer.save()
        answer.refresh_from_db()
        return Response({'msg': 'answer downvoted'})
    else:
        answer.downvote.remove(user)
        answer.downvote_count = F("downvote_count") - 1
        answer.totalvote = F("totalvote") - 1
        answer.save()
        answer.refresh_from_db()
    return Response({'msg': 'answer downvoted undo'})
        