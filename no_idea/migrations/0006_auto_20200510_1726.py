# Generated by Django 2.0.7 on 2020-05-10 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('no_idea', '0005_auto_20200510_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art_gallery',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='no_idea.category'),
        ),
        migrations.AlterField(
            model_name='art_gallery',
            name='user',
            field=models.ForeignKey(default=52442299888, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]