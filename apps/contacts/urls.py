from rest_framework.routers import DefaultRouter
from .views import ContactViewSet

app_name = "contacts"
router = DefaultRouter()
router.register("contacts", ContactViewSet, basename="contacts")

urlpatterns = [] + router.urls
