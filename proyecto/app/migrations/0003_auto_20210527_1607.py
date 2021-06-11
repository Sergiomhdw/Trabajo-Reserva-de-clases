# Generated by Django 3.2.3 on 2021-05-27 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20210525_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='password',
        ),
        migrations.AddField(
            model_name='profesor',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
