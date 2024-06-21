from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/edit/<int:id>/', views.edit_task, name="edit_task"),
    path('task/status_change/<int:id>/', views.status_change, name='status_change'),
    path('task/delete/<int:id>/', views.delete_task, name='delete_task'),
]
