"""AttendanceManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from users.views import *
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', home , name='home'),
    path('signup/',signUp, name='signup'),
    path('facultycourses/', facultyCourses , name='facultyCourses'),
    path('facultysections/',facultySections , name='facultySections'),
    path('admin/', admin.site.urls),

    path('reset_password/', authViews.PasswordResetView.as_view(template_name="password_reset.html") , name="reset_password"),
    path('reset_password_sent/', authViews.PasswordResetDoneView.as_view(template_name="password_reset_sent.html") , name="password_reset_done"),
    path('reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html") , name="password_reset_confirm"),
    path('reset_password_complete/', authViews.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html") , name="password_reset_complete"),
]


