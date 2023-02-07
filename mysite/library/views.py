from django.shortcuts import render, reverse
from django.http import HttpResponse
from .models import Uzduotis
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import FormMixin
from .forms import UserUzduotisCreateForm

def index(request):
    num_uzduotis = Uzduotis.objects.all().count()
    context = {
        'num_uzduotis': num_uzduotis,
    }
    return render(request, 'index.html', context=context)

class UzduotisListView(generic.ListView):
    model = Uzduotis
    template_name = 'uzduotis_list.html'

class UzduotisDetailView(generic.DetailView):
    model = Uzduotis
    template_name = 'uzduotis_detail.html'



def form_valid(self, form):
    form.instance.uzduotis = self.object
    form.instance.vartotojas = self.request.user
    form.save()
    return super(UzduotisDetailView, self).form_valid(form)


class UserUzduotysListView(LoginRequiredMixin, generic.ListView):
    model = Uzduotis
    template_name = 'user_uzduotis.html'

    def get_queryset(self):
        return Uzduotis.objects.filter(vartotojas=self.request.user).order_by('data')

class UserUzduotisCreateView(LoginRequiredMixin, CreateView):
    model = Uzduotis
    # fields = ['uzduotis']
    success_url = "/library/user_uzduotis/"
    template_name = 'user_uzduotis_form.html'
    form_class = UserUzduotisCreateForm

    def form_valid(self, form):
        form.instance.vartotojas = self.request.user
        return super().form_valid(form)

class UserUzduotisUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Uzduotis
    fields = ['uzduoties_tekstas', 'data']
    success_url = "/library/user_uzduotis/"
    template_name = 'user_uzduotis_form.html'

    def form_valid(self, form):
        form.instance.vartotojas = self.request.user
        return super().form_valid(form)

    def test_func(self):
        uzduotis = self.get_object()
        return self.request.user == uzduotis.vartotojas

class UserUzduotisDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Uzduotis
    success_url = "/library/user_uzduotis/"
    template_name = 'user_uzduotis_delete.html'

    def test_func(self):
        uzduotis = self.get_object()
        return self.request.user == uzduotis.vartotojas