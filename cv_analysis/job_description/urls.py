from django.urls import path
from job_description import views

urlpatterns = [
    path('job_description/', views.JobDescriptionListAPIView.as_view()),
    path('job_description/<str:id>/', views.JobDescriptionDetailAPIView.as_view()),
]