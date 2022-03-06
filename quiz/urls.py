from django.urls import include, path, re_path

from .views import QuestionRead, QuizList, QuizRead

urlpatterns = [
    path('', QuizList.as_view(), name='quiz_list'),
    path("<category>/", QuizRead.as_view(), name='quiz_read'),
    path("<category>/<quiz>/", QuestionRead.as_view(), name='question_read'),
]
