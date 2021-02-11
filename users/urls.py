from django.urls import path

from .views import signup, users

urlpatterns = [
    path('signup', signup),
    path('users', users)
]
