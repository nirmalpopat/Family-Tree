# Generated by Django 4.0.3 on 2022-03-11 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0003_alter_person_phone_number'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='relation',
            unique_together={('person1', 'relation', 'person2')},
        ),
    ]