from django.urls import path
from . import views

#url patterns

urlpatterns = [
    path('', views.post_list, name='post_list'),
]