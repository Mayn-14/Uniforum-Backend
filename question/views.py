from rest_framework import status
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import F, Q
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Question
from customUser.models import Account
from .serializers import questionSerializer, questionAnswerSerializer
import uuid 


@api_view()
def api_routes(request):
    print(str(uuid.uuid1()))
    if request.method == 'GET':
        routes = {"question": "http://127.0.0.1:8000/question/"}
    return Response(routes)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def question_api(request, slug=None):
    if request.method == 'GET':
        if slug is not None:
            question = Question.objects.get(question_slug=slug)
            question.views=F("views") + 1
            question.save()
            question.refresh_from_db()
            serializer = questionAnswerSerializer(question)
            return Response(serializer.data)

        question = Question.objects.exclude(answers__isnull=True)
        serializer = questionSerializer(question, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
        user_id = valid_data['user_id']
        request.data['user'] = user_id
        print(request.data)
        serializer = questionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Student Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        question = Question.objects.filter(question_slug=slug).update(isdeleted=True)
        return Response({'msg': 'Question Deleted'})

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def question_restore(request, slug=None):
    if request.method == 'PUT':
        question = Question.objects.filter(question_slug=slug).update(isdeleted=False)
        return Response({'msg': 'Question Restored'})

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def recommended_question(request):
    if request.method == 'GET':
        question = Question.objects.filter(Q(answers__upvote_count=0) | Q(answer_count=0))
        print(question.count())
        serializer = questionAnswerSerializer(question, many=True)
        return Response(serializer.data)