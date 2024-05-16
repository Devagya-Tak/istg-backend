from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestionSerializer, UserSerializer
from .models import User, Question

@api_view(['POST'])
def login(request):
  serializer = UserSerializer(data=request.data)

  if serializer.is_valid():
    username = serializer.validated_data.get('username')
    user = User.objects.filter(username=username).first()

    if user:
      return Response({
        'id':user.id
      })
    else:
      new_user = User.objects.create(username=username)
      return Response({
        'id': new_user.id
      })

  else:
    return Response({
      'error': serializer.errors
    })

@api_view(['POST'])
def post_question(request, pk):
  request.data['user'] = pk
  serializer = QuestionSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  else:
    return Response({'error': serializer.errors})

@api_view(['GET'])
def get_questions(request, pk):
    try:
        user = User.objects.get(pk=pk)
        questions = Question.objects.filter(user=user)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({'error': 'User not found'})