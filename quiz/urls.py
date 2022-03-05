from django.urls import include, path

from .views import QuestionRead, QuizList, QuizRead

urlpatterns = [
    path('', QuizList.as_view(), name='quiz_list'),
    path("<int:id>/", QuizRead.as_view(), name='quiz_read'),
    path("<int:id>/<int:pk>/", QuestionRead.as_view(), name='question_read'),
]
