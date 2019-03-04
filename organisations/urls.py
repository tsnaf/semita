from django.urls import path
from .views import (
    OrganisationListView,
    OrganisationDetailView,
    OrganisationCreateView,
    OrganisationDeleteView,
    OrganisationUpdateView,
)
from . import views

urlpatterns = [
    path('', OrganisationListView.as_view(), name='organisation-list'),
    path('organisation/<int:pk>/', OrganisationDetailView.as_view(), name='organisation-detail'),
    path('organisation/new/', OrganisationCreateView.as_view(), name='organisation-create'),
    path('organisation/<int:pk>/update/', OrganisationUpdateView.as_view(), name='organisation-update'),
    path('organisation/<int:pk>/delete/', OrganisationDeleteView.as_view(), name='organisation-delete'),

]
