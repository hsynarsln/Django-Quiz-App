from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from quiz.pagination import SmallPageNumberPagination

from .models import Answers, Category, Question, Quiz
from .permissions import IsStuffOrReadOnly
from .serializers import CategorySerializer, QuestionSerializer, QuizSerializer


class QuizList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class QuizRead(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']

    def get_queryset(self):
        category = self.kwargs['category'].capitalize()
        return Quiz.objects.filter(category__name=category)


class QuestionRead(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsStuffOrReadOnly,)
    pagination_class = SmallPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["difficulty"]

    def get_queryset(self):
        quiz = self.kwargs['quiz'].capitalize()
        return Question.objects.filter(quiz__title=quiz)
