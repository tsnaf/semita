from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Organisation, Grant, Fund, Contact


def home(request):
    return render(request, 'core/home.html')


class OrganisationListView(ListView):
    model = Organisation
    template_name = 'core/organisations/organisations.html'
    context_object_name = 'organisations'
    ordering = ['organisation_name']


class OrganisationDetailView(DetailView):
    model = Organisation
    template_name = 'core/organisations/organisation_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet for all objects
        context['grants'] = Grant.objects.all()
        context['contacts'] = Contact.objects.all()
        return context


class GrantListView(ListView):
    model = Grant
    template_name = 'core/grants/grants.html'
    context_object_name = 'grants'
    ordering = ['project_title']


class GrantDetailView(DetailView):
    model = Grant
    template_name = 'core/grants/grant_detail.html'


class FundListView(ListView):
    model = Fund
    template_name = 'core/funds/funds.html'
    context_object_name = 'funds'
    ordering = ['title']


class FundDetailView(DetailView):
    model = Fund
    template_name = 'core/funds/fund_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet for all objects
        context['grants'] = Grant.objects.all()
        return context


class ContactListView(ListView):
    model = Contact
    template_name = 'core/contacts/contacts.html'
    context_object_name = 'contacts'
    ordering = ['first_name']


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'core/contacts/contact_detail.html'
