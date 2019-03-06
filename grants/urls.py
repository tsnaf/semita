from django.urls import path
from .views import (
    GrantListView,
    GrantDetailView,
)
from . import views

urlpatterns = [
    path('', GrantListView.as_view(), name='grants'),
    path('grant/<int:pk>/', GrantDetailView.as_view(), name='grant-detail'),
]
