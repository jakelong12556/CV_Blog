from django.urls import path, include

from . import views

urlpatterns = [
    path('CV/', views.cv_base, name='cv_base'),
    #path('CV/edit/', views.cv_edit, name='cv_edit'),
]
