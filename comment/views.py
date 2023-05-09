from django.shortcuts import render
from .models import QuestionComment, AnswerComment
from rest_framework.decorators import api_view
from .serializers import questionCommentSerializer, answerCommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from customUser.models import Account
from django.db.models import F


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def questionComment_api(request, id=None):

    if request.method == 'GET':
        question = QuestionComment.objects.filter(question=id)
        serializer = questionCommentSerializer(question, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = questionCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Comment Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        questionComment = QuestionComment.objects.get(id=id)
        serializer = questionCommentSerializer(questionComment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Comment Updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        question = QuestionComment.objects.get(id=id).update(isdeleted=True)
        return Response({'msg': 'Question Deleted'})
    

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def questionComment_upvote(request, id=None):
    questionComment = QuestionComment.objects.get(id=id)
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
    user_id = valid_data['user_id']
    user = Account.objects.get(id=user_id)
    if not questionComment.upvote.exists():
        questionComment.upvote.add(user)
        questionComment.upvote_count = F("upvote_count") + 1
        questionComment.totalvote = F("totalvote") + 1
        questionComment.save()
        questionComment.refresh_from_db()
        return Response({'msg': 'questionComment upvoted'})
    else:
        questionComment.upvote.remove(user)
        questionComment.upvote_count = F("upvote_count") - 1
        questionComment.totalvote = F("totalvote") - 1
        questionComment.save()
        questionComment.refresh_from_db()
    return Response({'msg': 'questionCommnet upvoted undo'})


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def questionComment_downvote(request, id=None):
    questionComment = QuestionComment.objects.get(id=id)
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
    user_id = valid_data['user_id']
    user = Account.objects.get(id=user_id)
    if not questionComment.downvote.exists():
        questionComment.downvote.add(user)
        questionComment.downvote_count = F("downvote_count") + 1
        questionComment.totalvote = F("totalvote") + 1
        questionComment.save()
        questionComment.refresh_from_db()
        return Response({'msg': 'questionComment downvoted'})
    else:
        questionComment.downvote.remove(user)
        questionComment.downvote_count = F("downvote_count") - 1
        questionComment.totalvote = F("totalvote") - 1
        questionComment.save()
        questionComment.refresh_from_db()
    return Response({'msg': 'questionComment downvoted undo'})


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def answerComment_api(request, id=None):
    if request.method == 'GET':
        question = AnswerComment.objects.filter(answer=id)
        serializer = answerCommentSerializer(question, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = answerCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Comment Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        questionComment = AnswerComment.objects.get(id=id)
        serializer = answerCommentSerializer(questionComment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Comment Updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        question = AnswerComment.objects.get(id=id).update(isdeleted=True)
        return Response({'msg': 'Question Deleted'})


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def answerComment_upvote(request, id=None):
    answerComment = AnswerComment.objects.get(id=id)
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
    user_id = valid_data['user_id']
    user = Account.objects.get(id=user_id)
    if not answerComment.upvote.exists():
        answerComment.upvote.add(user)
        answerComment.upvote_count = F("upvote_count") + 1
        answerComment.totalvote = F("totalvote") + 1
        answerComment.save()
        answerComment.refresh_from_db()
        return Response({'msg': 'answerComment upvoted'})
    else:
        answerComment.upvote.remove(user)
        answerComment.upvote_count = F("upvote_count") - 1
        answerComment.totalvote = F("totalvote") - 1
        answerComment.save()
        answerComment.refresh_from_db()
    return Response({'msg': 'answerComment upvoted undo'})


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def answerComment_downvote(request, id=None):
    answerComment = AnswerComment.objects.get(id=id)
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
    user_id = valid_data['user_id']
    user = Account.objects.get(id=user_id)
    if not answerComment.downvote.exists():
        answerComment.downvote.add(user)
        answerComment.downvote_count = F("downvote_count") + 1
        answerComment.totalvote = F("totalvote") + 1
        answerComment.save()
        answerComment.refresh_from_db()
        return Response({'msg': 'answerComment downvoted'})
    else:
        answerComment.downvote.remove(user)
        answerComment.downvote_count = F("downvote_count") - 1
        answerComment.totalvote = F("totalvote") - 1
        answerComment.save()
        answerComment.refresh_from_db()
    return Response({'msg': 'answerComment downvoted undo'})