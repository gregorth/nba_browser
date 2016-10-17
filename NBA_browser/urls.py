"""NBA_browser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_nested import routers

from endpoints.views import PlayerAPI, StatisticAPI

router = routers.DefaultRouter()
router.register(r'players', PlayerAPI)

player_router = routers.NestedSimpleRouter(router, r'players', lookup='player')
player_router.register(r'statistics', StatisticAPI, r'player-statistics')

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'', include(player_router.urls))
]
