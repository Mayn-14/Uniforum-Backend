from django.shortcuts import render
from .models import QuestionComment, AnswerComment
from rest_framework.decorators import api_view
from .serializers import questionCommentSerializer, answerCommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
# from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from customUser.models import Account
from django.db.models import F, Q


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def questionComment_api(request, id=None):
    # for k, v in request.__dict__.items():
    #         print(k, " : ", v)

    if request.method == 'GET':
        questionComments = QuestionComment.objects.filter(question=id)
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
        user_id = valid_data['user_id']
        user = Account.objects.get(id=user_id)
        print('.')
        for questionComment in questionComments:
            if not questionComment.upvote.through.objects.filter(Q(account_id=user) & Q(questioncomment_id=questionComment.id)).exists():
                print('f')
                questionComment.hasUpvoted = False
            else:
                print('t')
                questionComment.hasUpvoted = True

            if not questionComment.downvote.through.objects.filter(Q(account_id=user) & Q(questioncomment_id=questionComment.id)).exists():
                questionComment.hasUpvoted = False
            else:
                questionComment.hasUpvoted = True        
        print('.')
        serializer = questionCommentSerializer(questionComments, many=True)
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
    if not questionComment.upvote.through.objects.filter(Q(account_id=user) & Q(questioncomment_id=id)).exists():
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
    if not questionComment.downvote.through.objects.filter(Q(account_id=user) & Q(questioncomment_id=id)).exists():
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
        answerComments = AnswerComment.objects.filter(answer=id)
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
        user_id = valid_data['user_id']
        user = Account.objects.get(id=user_id)
        print(user_id)
        for answerComment in answerComments:
            if not answerComment.upvote.through.objects.filter(Q(account_id=user) & Q(answercomment_id=answerComment.id)).exists():
                print('f')
                answerComment.hasUpvoted = False
            else:
                print('t')
                answerComment.hasUpvoted = True

            if not answerComment.downvote.through.objects.filter(Q(account_id=user) & Q(answercomment_id=answerComment.id)).exists():
                answerComment.hasUpvoted = False
            else:
                answerComment.hasUpvoted = True

        serializer = answerCommentSerializer(answerComments, many=True)
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
    if not answerComment.upvote.through.objects.filter(Q(account_id=user) & Q(answercomment_id=id)).exists():
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
    if not answerComment.downvote.through.objects.filter(Q(account_id=user) & Q(answercomment_id=id)).exists():
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