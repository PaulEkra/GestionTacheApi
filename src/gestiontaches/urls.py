"""
URL configuration for gestiontaches project.

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
from django.urls import path, include
from rest_framework import routers
from project.viewsets.project_viewset import ProjectViewSet
from project.viewsets.task_viewset import TaskViewSet
from team.viewsets.team_viewset import TeamViewSet
from team.viewsets.member_viewset import MemberViewSet
from project.viewsets.summons_viewset import SummonsViewSet
from history.viewsets.notifications_viewset import NotificationViewset
from history.viewsets.histories_viewset import HistoriesViewset


router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'members', MemberViewSet)
router.register(r'summons', SummonsViewSet)
router.register(r'notifications', NotificationViewset)
router.register(r'histories', HistoriesViewset, basename="histories")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
