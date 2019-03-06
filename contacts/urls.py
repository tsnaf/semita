from django.urls import path
from .views import (
    ContactListView,
    ContactDetailView,
)
from . import views

urlpatterns = [
    path('', ContactListView.as_view(), name='contacts'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
]
