from django.urls import path
from .views import *

urlpatterns = [
    path('image_list/', ImageListView.as_view(), name='image_list'),
    path('image_create/', ImageCreateView.as_view(), name='image_create'),
    path('image_update/<int:pk>/', ImageuUpdateView.as_view(), name='image_update'),
    path('image_delete/<int:pk>/', ImageuDeleteView.as_view(), name='image_delete'),

    path('project_list/', ProjestsListView.as_view(), name='project_list'),
    path('project_create/', ProjestsCreateView.as_view(), name='project_create'),
    path('project_update/<int:pk>/', ProjectsUpdateView.as_view(), name='project_update'),
    path('project_delete/<int:pk>/', ProjectsDeleteView.as_view(), name='project_delete'),
]

















