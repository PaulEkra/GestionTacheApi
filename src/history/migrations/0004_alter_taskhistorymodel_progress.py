# Generated by Django 5.1.1 on 2024-09-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0003_alter_taskhistorymodel_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskhistorymodel',
            name='progress',
            field=models.TextField(),
        ),
    ]
