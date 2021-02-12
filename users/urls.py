from django.urls import path

from .views import signup, users, signin, CurrentUser, signout

urlpatterns = [
    path('signup', signup),
    path('users', users),
    path('signin', signin),
    path('currentuser', CurrentUser.as_view()),
    path('signout', signout)

]
