from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='submit_request'),
    path('submit/', views.submit_request, name='submit_request'),
    path('track/<int:request_id>/', views.track_request, name='track_request'),
    path('account/', views.view_account, name='view_account'),
]