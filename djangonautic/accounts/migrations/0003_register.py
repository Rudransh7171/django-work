# Generated by Django 3.1.1 on 2020-10-03 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_delete_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailornumber', models.CharField(max_length=60)),
                ('fullname', models.CharField(max_length=40)),
            ],
        ),
    ]