# Create your views here.

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)  # add the remember_me field


class UpdatedLoginView(LoginView):
    # https://stackoverflow.com/a/53431981
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']  # get remember me data from cleaned_data of form
        if not remember_me:
            self.request.session.set_expiry(0)  # if remember me is
            self.request.session.modified = True

        return super(UpdatedLoginView, self).form_valid(form)
