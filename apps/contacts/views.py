from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import renderers
from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [renderers.JSONRenderer, renderers.BrowsableAPIRenderer, renderers.TemplateHTMLRenderer]
    search_fields = (
        "first_name",
        "last_name",
        "phone",
        "country",
        "city",
        "street",
    )

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)
