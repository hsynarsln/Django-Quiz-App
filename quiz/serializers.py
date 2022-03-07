from rest_framework import serializers

from .models import Answers, Category, Question, Quiz


class AnswersSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Answers
        fields = ('question_id', 'answerText', 'isRight')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswersSerializer(many=True, required=False)
    quiz_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Question
        fields = ('quiz_id', 'title', 'answers', 'difficulty',)

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        question = Question.objects.create(**validated_data)
        for answer in answers_data:
            answer["question_id"] = question.id
            question.answers.add(Answers.objects.create(**answer))
        question.save()
        return question


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, write_only=True)
    question_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Quiz
        fields = ('title', 'questions', 'question_count')

    def get_question_count(self, obj):
        return obj.questions.count()


class CategorySerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, write_only=True)
    quiz_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'quiz_count', 'quizzes', )

    def get_quiz_count(self, obj):
        return obj.quizzes.count()
