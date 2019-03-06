from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Organisation
from grants.models import Grant
from contacts.models import Contact


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
