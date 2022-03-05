from django.shortcuts import render
from rest_framework import generics

from .models import Answers, Category, Question, Quiz
from .serializers import CategorySerializer, QuestionSerializer, QuizSerializer


class QuizList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuizRead(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = 'id'


class QuestionRead(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'pk'
