from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Organisation


def home(request):
    context = {
        'organisations': Organisation.objects.all()
    }
    return render(request, 'organisations/temp.html', context)


class OrganisationListView(ListView):
    model = Organisation
    template_name = 'organisations/organisations.html'
    context_object_name = 'organisations'
    ordering = ['organisation_name']


class OrganisationDetailView(DetailView):
    model = Organisation


class OrganisationCreateView(CreateView):
    model = Organisation
    fields = ['organisation_name', 'address_1', 'address_2',
              'postcode', 'county', 'website', 'notes']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class OrganisationUpdateView(UpdateView):
    model = Organisation
    fields = ['organisation_name', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class OrganisationDeleteView(DeleteView):
    model = Organisation
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
