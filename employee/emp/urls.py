from django.urls import path
from .views import create_view, show_view, update_view, delete_view


urlpatterns = [
    path('create/', create_view.as_view(), name='create_url'),
    path('show/', show_view.as_view(), name='show_url'),
    path('update/<int:pk>/', update_view.as_view(), name='update_url'),
    path('delete/<int:pk>/', delete_view.as_view(), name='delete_url'),
]
