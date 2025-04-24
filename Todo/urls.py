"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from myapp.views import UserRegistrationView, LoginView, LogoutView, TaskView
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path("register/", UserRegistrationView.as_view()),

    path("login/",LoginView.as_view(), name="login"),

    path("logout/", LogoutView.as_view(), name="logout"),

    path("task/",TaskView.as_view()),

    path("task/list",TaskReadView.as_view(), name="tasklist"),

    path("task/update/<int:pk>",TaskUpdateView.as_view()),      # /task/update/1

    path("task/delete/<int:pk>",TaskDeleteView.as_view()),

    path("task/detail/<int:pk>", TaskDetailView.as_view()),

    path("task/edit/<int:pk>", TaskStatusEdit.as_view()),

    path("forgotpwd", ForgotPassView.as_view() , name="forgot"),
]
