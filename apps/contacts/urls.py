from rest_framework.routers import DefaultRouter
from .views import ContactViewSet

app_name = "contacts"
router = DefaultRouter()
router.register("contact", ContactViewSet, basename="contact")

urlpatterns = [] + router.urls
