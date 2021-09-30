# Generated by Django 3.2.7 on 2021-09-30 12:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last name')),
                ('country', models.CharField(blank=True, max_length=100, verbose_name='Country')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='City')),
                ('street', models.CharField(blank=True, max_length=100, verbose_name='Street')),
                ('building', models.CharField(blank=True, max_length=20, verbose_name='Building')),
                ('floor', models.CharField(blank=True, max_length=20, verbose_name='Floor')),
                ('url', models.URLField(blank=True, null=True, validators=[django.core.validators.RegexValidator(message='Not a valid URL', regex='(http|ftp|https)://([\\w_-]+(?:(?:\\.[\\w_-]+)+))([\\w.,@?^=%&:/~+#-]*[\\w@?^=%&/~+#-])?')])),
                ('phone', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+12223334455'", regex='^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$')])),
                ('image', models.ImageField(blank=True, null=True, upload_to='contact_image/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_contacts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
                'ordering': ('pk',),
                'unique_together': {('first_name', 'last_name')},
            },
        ),
    ]