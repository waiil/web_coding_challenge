# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mama_cas.views import LoginView as CasLoginView
from .forms import LoginForm, UserCreationForm
from django.views.generic.edit import FormView
from django.contrib import messages


class Signup(FormView):
    form_class = UserCreationForm
    success_url = 'http://127.0.0.1:8000/'
    template_name = 'signup.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Successfully Subscribed")
        return super(Signup, self).form_valid(form)


class LoginView(CasLoginView):
    form_class = LoginForm

