from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_practice, name = 'gmat-practice-list'),
    path('practice/<int:pk>/start/', views.start_practice, name='gmat-practice-start'),
    path('practice/<int:pk>/submit/', views.submit_practice, name='gmat-submit-practice'),
    path('practice-results/<int:pk>/', views.practice_results, name='gmat-practice-results'),
    path('pr-question-details/<int:pk>/', views.pr_question_detail, name = 'gmat-pr-question-detail'),
]