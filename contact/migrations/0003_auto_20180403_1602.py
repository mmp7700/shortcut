# Generated by Django 2.0.3 on 2018-04-03 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_servicerequest_type_of_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicerequest',
            name='type_of_service',
        ),
        migrations.DeleteModel(
            name='ServiceRequest',
        ),
    ]
