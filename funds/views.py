from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Fund


class FundListView(ListView):
    model = Fund
    template_name = 'funds/funds.html'
    context_object_name = 'funds'
    ordering = ['title']


class FundDetailView(DetailView):
    model = Fund
