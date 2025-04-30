from django.urls import path
from .views import delete_file
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_file, name='upload'),
    path('file/<uuid:file_uuid>/', views.view_file, name='view_file'),
    path('download/<uuid:file_uuid>/', views.serve_file, name='serve_file'),
    path('file/<uuid:file_uuid>/delete/', delete_file, name='delete_file'),
]
