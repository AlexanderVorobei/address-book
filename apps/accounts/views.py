from django.contrib.auth.views import (
    LogoutView,
    LoginView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from .forms import (
    CreationForm,
    LogInForm,
    UpdateForm,
    ResetPasswordForm,
    PasswordSetForm,
)


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"


class LogIn(LoginView):
    form_class = LogInForm
    template_name = "accounts/login.html"

    def get_success_url(self):
        return reverse("index")


class LogOut(LogoutView):
    template_name = "accounts/logout.html"


class Profile(UpdateView):
    context_object_name = "variable_used_in `profile.html`"
    form_class = UpdateForm
    success_url = reverse_lazy("index")
    template_name = "accounts/profile.html"

    def get_object(self, queryset=None):
        return self.request.user


class ResetPassword(PasswordResetView):
    form_class = ResetPasswordForm
    success_url = reverse_lazy("accounts:reset_password_done")
    template_name = "accounts/reset_password.html"
    email_template_name = "accounts/reset_password_email.html"


class ResetPasswordDone(PasswordResetDoneView):
    template_name = "accounts/reset_password_done.html"


class ResetPasswordConfirm(PasswordResetConfirmView):
    form_class = PasswordSetForm
    success_url = reverse_lazy("accounts:reset_password_complete")
    template_name = "accounts/reset_password_confirm.html"


class ResetPasswordComplete(PasswordResetCompleteView):
    template_name = "accounts/reset_password_complete.html"
