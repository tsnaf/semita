from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Grant


class GrantListView(ListView):
    model = Grant
    template_name = 'grants/grants.html'
    context_object_name = 'grants'
    ordering = ['project_title']


class GrantDetailView(DetailView):
    model = Grant
