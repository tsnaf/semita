from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class OrganisationCreateView(LoginRequiredMixin, CreateView):
    model = Organisation
    fields = ['organisation_name', 'address_1', 'address_2',
              'postcode', 'county', 'type', 'website', 'notes']
    template_name = 'core/organisations/organisation_form.html'


class OrganisationUpdateView(LoginRequiredMixin, UpdateView):
    model = Organisation
    fields = ['organisation_name', 'address_1', 'address_2',
              'postcode', 'county', 'type', 'website', 'notes']
    template_name = 'core/organisations/organisation_form.html'


class OrganisationDeleteView(LoginRequiredMixin, DeleteView):
    model = Organisation
    success_url = '/'
    template_name = 'core/organisations/organisation_confirm_delete.html'


class GrantListView(ListView):
    model = Grant
    template_name = 'core/grants/grants.html'
    context_object_name = 'grants'
    ordering = ['project_title']


class GrantDetailView(DetailView):
    model = Grant
    template_name = 'core/grants/grant_detail.html'


class GrantCreateView(LoginRequiredMixin, CreateView):
    model = Grant
    fields = ['organisation', 'fund', 'project_title',
              'amount', 'status', 'notes']
    template_name = 'core/grants/grant_form.html'


class GrantUpdateView(LoginRequiredMixin, UpdateView):
    model = Grant
    fields = ['organisation', 'fund', 'project_title',
              'amount', 'status', 'notes']
    template_name = 'core/grants/grant_form.html'


class GrantDeleteView(LoginRequiredMixin, DeleteView):
    model = Grant
    success_url = '/'
    template_name = 'core/grants/grant_confirm_delete.html'


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


class FundCreateView(LoginRequiredMixin, CreateView):
    model = Fund
    fields = ['title', 'amount', 'open_date',
              'close_date', 'type', 'status', 'notes']
    template_name = 'core/funds/fund_form.html'


class FundUpdateView(LoginRequiredMixin, UpdateView):
    model = Fund
    fields = ['title', 'amount', 'open_date',
              'close_date', 'type', 'status', 'notes']
    template_name = 'core/funds/fund_form.html'


class FundDeleteView(LoginRequiredMixin, DeleteView):
    model = Fund
    success_url = '/'
    template_name = 'core/funds/fund_confirm_delete.html'


class ContactListView(ListView):
    model = Contact
    template_name = 'core/contacts/contacts.html'
    context_object_name = 'contacts'
    ordering = ['first_name']


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'core/contacts/contact_detail.html'


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['organisation', 'first_name', 'last_name',
              'job_title', 'email', 'phone', 'notes']
    template_name = 'core/contacts/contact_form.html'


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    fields = ['organisation', 'first_name', 'last_name',
              'job_title', 'email', 'phone', 'notes']
    template_name = 'core/contacts/contact_form.html'


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    success_url = '/'
    template_name = 'core/contacts/contact_confirm_delete.html'
