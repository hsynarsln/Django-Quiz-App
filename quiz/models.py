from django.db import models


# Create your models here.
class Category(models.Model):
    CATEGORY_NAME_CHOICES = [
        ("Mobile", 'Mobile'),
        ("Frontend", 'Frontend'),
        ("Backend", 'Backend'),
        ("DataScientist", 'DataScientist'),
        ("DevOps", 'DevOps'),
    ]
    name = models.CharField(
        max_length=13, choices=CATEGORY_NAME_CHOICES, default="Mobile")

    def __str__(self):
        return self.name


class Quiz(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="quizzes")
    title = models.CharField(max_length=30)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.category} - {self.title}'


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="questions")
    title = models.TextField(max_length=200)
    DIFFICULTY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'Hard'),
        (4, 'Expert'),
    ]
    difficulty = models.IntegerField(
        choices=DIFFICULTY_CHOICES, default="Low")
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quiz} - {self.title}'


class Answers(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers")
    answerText = models.TextField(max_length=200)
    isRight = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.question} - {self.answerText}'
