"""planner URL Configuration

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
from webpage.views import welcome
from meeting.views import detail_meeting
from meeting.views import detail_room

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name = 'welcome'),
    path('meeting/<int:id>', detail_meeting, name='detail_meeting'),
    path('room/<int:id>', detail_room, name='detail_room')
]
