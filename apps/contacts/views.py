from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = IsAuthenticated

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)
