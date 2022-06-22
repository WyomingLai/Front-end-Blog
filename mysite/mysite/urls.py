"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from trips.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', wyWeb),
    path('blog/', wyBlog),
    path('blog/HTML/', wyBlog_HTML),
    path('blog/CSS/', wyBlog_CSS),
    path('blog/JavaScript/', wyBlog_JavaScript),
    path('blog/Forum/', wyBlog_Forum),
    path('blog/Forum/newArticle/', post_create_view),
    path('blog/Forum/<int:pk>', PostDetail.as_view()),
]


