# Generated by Django 2.0.7 on 2020-05-05 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('no_idea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art_gallery',
            name='user',
            field=models.ForeignKey(default=753339989936, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]