# Generated by Django 4.0.6 on 2022-08-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wemes', '0003_alter_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
