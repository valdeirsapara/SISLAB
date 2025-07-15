from django.urls import path
from .views import index, add_laboratory, edit_laboratory


urlpatterns = [
    path('', index, name='laboratory_index'),
    path('add/', add_laboratory, name='add_laboratory'),
    path('edit/<int:id>/', edit_laboratory, name='edit_laboratory'),
]