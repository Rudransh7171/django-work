# Generated by Django 3.1.1 on 2020-10-03 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
