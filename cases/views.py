from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Client, Lawyer, Case
from .forms import ClientForm, LawyerForm, CaseForm
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

# client
class ClientListView(ListView):
    model = Client
    template_name = "clients/clientlist.html"

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = "clients/clientform.html"
    success_url = "/clients/"

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = "clients/clientform.html"
    success_url = "/clients/"

class ClientDeleteView(DeleteView):
    model = Client
    template_name = "clients/clientdelete.html"
    success_url = reverse_lazy("cases:clientlist")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Client"
        return context


# lawyer
class LawyerListView(ListView):
    model = Lawyer
    template_name = "lawyers/lawyerlist.html"

class LawyerCreateView(CreateView):
    model = Lawyer
    form_class = LawyerForm
    template_name = "lawyers/lawyerform.html"
    success_url = "/lawyers/"

class LawyerUpdateView(UpdateView):
    model = Lawyer
    form_class = LawyerForm
    template_name = "lawyers/lawyerform.html"
    success_url = "/lawyers/"

class LawyerDeleteView(DeleteView):
    model = Lawyer
    template_name = "lawyers/lawyerdelete.html"
    success_url = reverse_lazy("cases:lawyerlist")


# Case
class CaseListView(ListView):
    model = Case
    template_name = "cases/caselist.html"

class CaseCreateView(CreateView):
    model = Case
    form_class = CaseForm
    template_name = "cases/caseform.html"
    success_url = "/cases/"

class CaseUpdateView(UpdateView):
    model = Case
    form_class = CaseForm
    template_name = "cases/caseform.html"
    success_url = "/cases/"

class CaseDeleteView(DeleteView):
    model = Lawyer
    template_name = "cases/casedelete.html"
    success_url = reverse_lazy("cases:caselist")