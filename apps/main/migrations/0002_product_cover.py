# Generated by Django 5.0.2 on 2024-02-29 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cover',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]