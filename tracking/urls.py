from django.urls import path
from . import views

urlpatterns = [
    path('log/', views.log_time, name='log_time'),
    path('entries/', views.time_entries, name='time_entries'),
]
