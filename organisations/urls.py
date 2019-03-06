from django.urls import path
from .views import (
    OrganisationListView,
    OrganisationDetailView,
)
from . import views

urlpatterns = [
    path('', OrganisationListView.as_view(), name='organisations'),
    path('organisation/<int:pk>/', OrganisationDetailView.as_view(), name='organisation-detail'),
]
