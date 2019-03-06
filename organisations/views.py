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
    return render(request, 'organisations/home.html')


class OrganisationListView(ListView):
    model = Organisation
    template_name = 'organisations/organisations.html'
    context_object_name = 'organisations'
    ordering = ['organisation_name']


class OrganisationDetailView(DetailView):
    model = Organisation

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['grants'] = Grant.objects.all()
        context['contacts'] = Contact.objects.all()
        return context


class GrantListView(ListView):
    model = Grant
    template_name = 'organisations/grants.html'
    context_object_name = 'grants'
    ordering = ['project_title']


class GrantDetailView(DetailView):
    model = Grant


class FundListView(ListView):
    model = Fund
    template_name = 'organisations/funds.html'
    context_object_name = 'funds'
    ordering = ['title']


class FundDetailView(DetailView):
    model = Fund


class ContactListView(ListView):
    model = Contact
    template_name = 'organisations/contacts.html'
    context_object_name = 'contacts'
    ordering = ['first_name']


class ContactDetailView(DetailView):
    model = Contact
