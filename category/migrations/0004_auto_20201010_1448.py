# Generated by Django 3.1.1 on 2020-10-10 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0003_auto_20201010_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]