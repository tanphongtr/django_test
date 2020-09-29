"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from rest_framework.authtoken import views

from .post import PostViewSet, PostDetailViewSet
from .parent import ParentViewSet, ParentDetailViewSet
from .child import ChildViewSet, ChildDetailViewSet
from .auth import AuthViewSet

from .file import FileViewSet

urlpatterns = [
    path('posts/', PostViewSet.as_view()),
    path('posts/<str:uuid>', PostDetailViewSet.as_view()),

    path('parents/', ParentViewSet.as_view()),
    path('parents/<str:uuid>', ParentDetailViewSet.as_view()),

    path('childs/', ChildViewSet.as_view()),
    path('childs/<str:id>', ChildDetailViewSet.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('auth/', AuthViewSet.as_view()),

    path('files/', FileViewSet.as_view()),

    
]