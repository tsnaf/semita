from django.urls import path
from .views import (
    OrganisationListView,
    OrganisationDetailView,
    OrganisationCreateView,
    OrganisationUpdateView,
    OrganisationDeleteView,
    GrantListView,
    GrantDetailView,
    FundListView,
    FundDetailView,
    ContactListView,
    ContactDetailView,
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('organisations/', OrganisationListView.as_view(), name='organisations'),
    path('organisation/<str:slug>-<int:pk>/',
         OrganisationDetailView.as_view(), name='organisation-detail'),
    path('organisation/new/',
         OrganisationCreateView.as_view(), name='organisation-create'),
    path('organisation/<str:slug>-<int:pk>/update/',
         OrganisationUpdateView.as_view(), name='organisation-update'),
    path('organisation/<str:slug>-<int:pk>/delete/',
         OrganisationDeleteView.as_view(), name='organisation-delete'),
    path('grants/', GrantListView.as_view(), name='grants'),
    path('grant/<str:slug>-<int:pk>/', GrantDetailView.as_view(), name='grant-detail'),
    path('funds/', FundListView.as_view(), name='funds'),
    path('fund/<str:slug>-<int:pk>/', FundDetailView.as_view(), name='fund-detail'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('contact/<str:slug>-<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
]
