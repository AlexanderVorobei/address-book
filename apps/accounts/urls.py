from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("profile/<int:pk>/", views.Profile.as_view(), name="profile"),
    path("login/", views.LogIn.as_view(), name="login"),
    path("logout/", views.LogOut.as_view(), name="logout"),
    path("reset_password/", views.ResetPassword.as_view(), name="reset_password"),
    path(
        "reset_password_done/",
        views.ResetPasswordDone.as_view(),
        name="reset_password_done",
    ),
    path(
        "reset_password_complete/",
        views.ResetPasswordComplete.as_view(),
        name="reset_password_complete",
    ),
    path(
        "reset_password_confirm/$<uidb64>/<token>/",
        views.ResetPasswordConfirm.as_view(),
        name="reset_password_confirm",
    ),
]
