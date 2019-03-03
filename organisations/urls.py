from django.urls import path
from .views import (
    OrganisationtListView,
    OrganisationDetailView,
)
from . import views

urlpatterns = [
    path('', OrganisationListView.as_view(), name='organisations'),
    path('post/<int:pk>/', OrganisationDetailView.as_view(), name='organisation-detail'),

]
