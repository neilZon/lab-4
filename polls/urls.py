from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.IndexView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.IndexView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.IndexView.as_view(), name='vote'),
    path('api/questions/', views.get_questions, name='get_questions'),
    path('api/question/<int:pk>', views.update_question, name='update_question'),
]