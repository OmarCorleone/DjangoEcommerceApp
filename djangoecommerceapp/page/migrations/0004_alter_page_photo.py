# Generated by Django 4.1 on 2023-03-04 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_alter_page_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='page'),
        ),
    ]
