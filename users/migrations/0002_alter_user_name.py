# Generated by Django 5.0.6 on 2024-07-05 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=150, verbose_name='이름'),
        ),
    ]