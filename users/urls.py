from django.urls import path

from .views import(signup, signin, CurrentUser, signout,
                   PermissionView, RoleViewSet, UserGenericAPIVIEW)

urlpatterns = [
    path('signup', signup),
    path('signin', signin),
    path('currentuser', CurrentUser.as_view()),
    path('signout', signout),
    path('permissions', PermissionView.as_view()),
    path('roles', RoleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('roles/<str:pk>', RoleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('users', UserGenericAPIVIEW.as_view()),
    path('users/<str:pk>', UserGenericAPIVIEW.as_view())


]
