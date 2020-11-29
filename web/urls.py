from django.urls import path
from web.views import DashboardView

from . import views

urlpatterns = [
    path('', DashboardView.as_view()),
]