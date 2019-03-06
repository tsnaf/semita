from django.urls import path
from .views import (
    FundListView,
    FundDetailView,
)
from . import views

urlpatterns = [
    path('', FundListView.as_view(), name='funds'),
    path('fund/<int:pk>/', FundDetailView.as_view(), name='fund-detail'),
]
