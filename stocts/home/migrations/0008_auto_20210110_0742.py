# Generated by Django 3.0.6 on 2021-01-10 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=225),
        ),
    ]