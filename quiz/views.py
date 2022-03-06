from rest_framework import generics

from .models import Answers, Category, Question, Quiz
from .permissions import IsStuffOrReadOnly
from .serializers import CategorySerializer, QuestionSerializer, QuizSerializer


class QuizList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsStuffOrReadOnly,)


class QuizRead(generics.ListCreateAPIView):
    serializer_class = QuizSerializer
    permission_classes = (IsStuffOrReadOnly,)

    def get_queryset(self):
        category = self.kwargs['category'].capitalize()
        return Quiz.objects.filter(category__name=category)


class QuestionRead(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = (IsStuffOrReadOnly,)

    def get_queryset(self):
        quiz = self.kwargs['quiz'].capitalize()
        return Question.objects.filter(quiz__title=quiz)
