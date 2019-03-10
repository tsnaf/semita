from django.urls import path
from .views import (
    OrganisationListView,
    OrganisationDetailView,
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
    # path('organisation/<slug>/', OrganisationDetailView.as_view(), name='organisation-detail'),
    path('organisation/<str:slug>-<int:pk>/',
         OrganisationDetailView.as_view(), name='organisation-detail'),
    path('grants/', GrantListView.as_view(), name='grants'),
    path('grant/<int:pk>/', GrantDetailView.as_view(), name='grant-detail'),
    path('funds/', FundListView.as_view(), name='funds'),
    path('fund/<int:pk>/', FundDetailView.as_view(), name='fund-detail'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
]
