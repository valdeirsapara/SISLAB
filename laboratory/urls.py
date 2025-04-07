from django.urls import path
from .views import index, add_laboratory


urlpatterns = [
    path('', index, name='laboratory_index'),
    path('add/', add_laboratory, name='add_laboratory'),
    path('add/<int:id>/', add_laboratory, name='add_laboratory')
]