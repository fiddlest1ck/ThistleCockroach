from django.urls import path

from cockroach import views

urlpatterns = [
    path('projection', views.ProjectionView.as_view())
]
