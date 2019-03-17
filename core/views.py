from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Sum
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Organisation, Grant, Fund, Contact, Dashboard
from .forms import attachmentuploadform


def home(request):
    return render(request, 'core/home.html')


class OrganisationListView(ListView):
    model = Organisation
    template_name = 'core/organisations/organisations.html'
    context_object_name = 'organisations'
    ordering = ['organisation_name']
    paginate_by = 20


class OrganisationDetailView(DetailView):
    model = Organisation
    template_name = 'core/organisations/organisation_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(OrganisationDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet for all objects
        context['contacts'] = Contact.objects.filter(organisation_id=self.kwargs['pk'])
        context['grants'] = Grant.objects.filter(
            organisation_id=self.kwargs['pk'])
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
    ordering = ['-date']
    paginate_by = 20

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet for all objects
        context['grantsapplied'] = Grant.objects.filter(
            status='Applied')
        context['grantsaccepted'] = Grant.objects.filter(
            status='Accepted')
        context['grantscontracted'] = Grant.objects.filter(
            status='Contracted')
        context['grantscompleted'] = Grant.objects.filter(
            status='Completed')
        context['grantsdeclined'] = Grant.objects.filter(
            status='Declined')
        return context


class GrantDetailView(DetailView):
    model = Grant
    template_name = 'core/grants/grant_detail.html'


class GrantCreateView(LoginRequiredMixin, CreateView):
    model = Grant
    fields = ['organisation', 'fund', 'project_title',
              'amount', 'status', 'attachment', 'notes']
    template_name = 'core/grants/grant_form.html'

    def file_upload(request):
        save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['file'])
        path = default_storage.save(save_path, request.FILES['file'])
        return default_storage.path(path)


class GrantUpdateView(LoginRequiredMixin, UpdateView):
    model = Grant
    fields = ['organisation', 'fund', 'project_title',
              'amount', 'status', 'attachment', 'notes']
    template_name = 'core/grants/grant_form.html'

    def attachmentupload(request):
        if request.method == 'POST':
            form = attachmentuploadform(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = attachmentuploadform()
        return render(request, 'core/grants/grant_form.html', {
            'form': form
        })


class GrantDeleteView(LoginRequiredMixin, DeleteView):
    model = Grant
    success_url = '/'
    template_name = 'core/grants/grant_confirm_delete.html'


class FundListView(ListView):
    model = Fund
    template_name = 'core/funds/funds.html'
    context_object_name = 'funds'
    ordering = ['-open_date']
    paginate_by = 20


class FundDetailView(DetailView):
    model = Fund
    template_name = 'core/funds/fund_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet for all objects
        context['grants'] = Grant.objects.filter(fund_id=self.kwargs['pk'])
        context['grants_active'] = Grant.objects.filter(fund_id=self.kwargs['pk']).filter(
            status__in=['Accepted', 'Contracted', 'Completed']).aggregate(Sum('amount'))
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
    ordering = ['organisation']
    paginate_by = 20


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


class DashboardView(ListView):
    model = Fund
    context_object_name = 'funds'
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet for all objects
        context['grants_applied'] = Grant.objects.filter(status='Applied')
        context['grants_completed'] = Grant.objects.filter(status='Completed')
        context['funds_open'] = Fund.objects.filter(status='Open')
        return context
