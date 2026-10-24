from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_details, name='course_details'),
    path('lesson/<int:lesson_id>/exam/', views.mock_exam, name='mock_exam'),
    path('submit/<int:lesson_id>/', views.submit, name='submit'),
    path('exam-result/<int:submission_id>/', views.show_exam_result, name='show_exam_result'),
]
