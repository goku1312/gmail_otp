"""otp_verification URL Configuration

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
from django.urls import path
from sending import views
from sending .views import FieldsToBeSentViews

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.mail_sent,name="email"),
    path('hell/',FieldsToBeSentViews.as_view(),name="sending otp code"),
    path('',views.register,name="register"),
    path('otp/',views.otp_form,name="otpform"),
]
