"""texas_holdem_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from poker.views import create_table, find_table, get_table, show_pre_flop, show_flop, show_turn, show_river

urlpatterns = [
    path('create_table/', create_table, name="create_table"),
    path('find_table/', find_table, name="find_table"),
    path('table/<str:name>', get_table, name="get_table"),
    path('pre_flop/', show_pre_flop, name="pre_flop"),
    path('flop/', show_flop, name="flop"),
    path('turn/', show_turn, name="turn"),
    path('river/', show_river, name="river"),
    
]
