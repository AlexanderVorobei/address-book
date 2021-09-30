from apps.accounts.models import User
from django.conf import settings
from django.core.files.storage import get_storage_class
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.functional import LazyObject


class AvatarStorage(LazyObject):
    def _setup(self):
        AVATAR_FILE_STORAGE = getattr(settings, 'AVATAR_FILE_STORAGE', settings.DEFAULT_FILE_STORAGE)
        self._wrapped = get_storage_class(AVATAR_FILE_STORAGE)()


avatar_storage = AvatarStorage()


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_contacts")
    first_name = models.CharField(_('first name'), max_length=150, blank=False, null=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False, null=False)
    country = models.CharField(_('Country'), max_length=100, blank=True)
    city = models.CharField(_('City'), max_length=100, blank=True)
    street = models.CharField(_('Street'), max_length=100, blank=True)
    building = models.CharField(_('Building'), max_length=20, blank=True)
    floor = models.CharField(_('Floor'), max_length=20, blank=True)
    url = models.URLField(max_length=200,
                          null=True,
                          blank=True,
                          validators=[RegexValidator(
                              regex=r'(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?',
                              message='Not a valid URL',
                          )])
    phone = models.CharField(max_length=17,
                             null=False,
                             blank=False,
                             unique=True,
                             validators=[RegexValidator(
                                 regex=r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$',
                                 message="Phone number must be entered in the format: '+12223334455'")])
    image = models.ImageField(upload_to="contact_image/", null=True, blank=True)

    class Meta:
        unique_together = ('first_name', 'last_name')
        verbose_name = "contact"
        verbose_name_plural = "contacts"
        ordering = ("pk",)

    def __init__(self, *args, **kwargs):
        super(Contact, self).__init__(*args, **kwargs)
        self.image.storage = avatar_storage
        self.image.thumbnail_storage = avatar_storage

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_address(self):
        return '%s %s, %s' % (
            self.country,
            self.city,
            self.street
        )
