from django.urls import path
from .import views
app_name = "main"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('add/', views.add, name="add"),
    path('delete/<int:todo_id>/', views.delete, name="delete"),
]
