from django.urls import path, include
from file_receive import views

urlpatterns = [ 
    path('', views.Form),
    path('upload/', views.Upload),
] 