# Generated by Django 4.2.7 on 2023-11-29 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproducts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=255)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
