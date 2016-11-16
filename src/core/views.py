from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import UpdateView

from .models import Myuser


class MyUserForm(forms.ModelForm):
    class Meta:
        model = Myuser
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'email',
            'avatar',
        ]

    def save(self, commit=True):
        user = super(MyUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserView(DetailView):
    model = Myuser
    template_name = "user.html"
    context_object_name = 'myuser'


class UserEdit(UpdateView):
    template_name = 'user_edit.html'
    model = Myuser
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'avatar',
    ]

    def get_success_url(self, **kwargs):
        if kwargs != None:
            return reverse_lazy('main_page:user', kwargs=self.kwargs)
        else:
            return reverse_lazy('galleries:list')


def main_page(request):
    return render(request, 'main_page.html')
