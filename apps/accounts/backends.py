from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import User


class UserAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(email__iexact=username)) if username \
                else User.objects.get(Q(email__iexact=email))
        except User.DoesNotExist:
            return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
