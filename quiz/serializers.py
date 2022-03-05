from unicodedata import category

from rest_framework import serializers

from .models import Answers, Category, Question, Quiz


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ('answerText', 'isRight')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswersSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('title', 'answers', 'difficulty',)


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, write_only=True)
    question_count = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ('title', 'questions', 'question_count')

    def get_question_count(self, obj):
        return obj.questions.count()


class CategorySerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, write_only=True)
    quiz_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'quiz_count', 'quizzes',)

    def get_quiz_count(self, obj):
        return obj.quizzes.count()
