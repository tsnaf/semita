from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Contact


class ContactListView(ListView):
    model = Contact
    template_name = 'contacts/contacts.html'
    context_object_name = 'contacts'
    ordering = ['first_name']


class ContactDetailView(DetailView):
    model = Contact
