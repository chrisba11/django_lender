# Generated by Django 2.1.7 on 2019-03-28 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lender_app', '0003_auto_20190328_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='books',
                to=settings.AUTH_USER_MODEL),
        ),
    ]
