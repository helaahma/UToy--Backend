# Generated by Django 2.2.6 on 2019-10-09 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20191009_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectable',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
