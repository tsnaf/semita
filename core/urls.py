from django.urls import path
from .views import (
    OrganisationListView,
    OrganisationDetailView,
    OrganisationCreateView,
    OrganisationUpdateView,
    OrganisationDeleteView,
    GrantListView,
    GrantDetailView,
    GrantCreateView,
    GrantUpdateView,
    GrantDeleteView,
    FundListView,
    FundDetailView,
    FundCreateView,
    FundUpdateView,
    FundDeleteView,
    ContactListView,
    ContactDetailView,
    ContactCreateView,
    ContactUpdateView,
    ContactDeleteView,
    DashboardView,
)
from . import views

urlpatterns = [
    path("", DashboardView.as_view(), name="home"),
    path("organisations/", OrganisationListView.as_view(), name="organisations"),
    path(
        "organisation/<str:slug>-<int:pk>/",
        OrganisationDetailView.as_view(),
        name="organisation-detail",
    ),
    path(
        "organisation/new/",
        OrganisationCreateView.as_view(),
        name="organisation-create",
    ),
    path(
        "organisation/<str:slug>-<int:pk>/update/",
        OrganisationUpdateView.as_view(),
        name="organisation-update",
    ),
    path(
        "organisation/<str:slug>-<int:pk>/delete/",
        OrganisationDeleteView.as_view(),
        name="organisation-delete",
    ),
    path("grants/", GrantListView.as_view(), name="grants"),
    path("grant/<str:slug>-<int:pk>/", GrantDetailView.as_view(), name="grant-detail"),
    path("grant/new/", GrantCreateView.as_view(), name="grant-create"),
    path(
        "grant/<str:slug>-<int:pk>/update/",
        GrantUpdateView.as_view(),
        name="grant-update",
    ),
    path(
        "grant/<str:slug>-<int:pk>/delete/",
        GrantDeleteView.as_view(),
        name="grant-delete",
    ),
    path("funds/", FundListView.as_view(), name="funds"),
    path("fund/<str:slug>-<int:pk>/", FundDetailView.as_view(), name="fund-detail"),
    path("fund/new/", FundCreateView.as_view(), name="fund-create"),
    path(
        "fund/<str:slug>-<int:pk>/update/", FundUpdateView.as_view(), name="fund-update"
    ),
    path(
        "fund/<str:slug>-<int:pk>/delete/", FundDeleteView.as_view(), name="fund-delete"
    ),
    path("contacts/", ContactListView.as_view(), name="contacts"),
    path(
        "contact/<str:slug>-<int:pk>/",
        ContactDetailView.as_view(),
        name="contact-detail",
    ),
    path("contact/new/", ContactCreateView.as_view(), name="contact-create"),
    path(
        "contact/<str:slug>-<int:pk>/update/",
        ContactUpdateView.as_view(),
        name="contact-update",
    ),
    path(
        "contact/<str:slug>-<int:pk>/delete/",
        ContactDeleteView.as_view(),
        name="contact-delete",
    ),
]
