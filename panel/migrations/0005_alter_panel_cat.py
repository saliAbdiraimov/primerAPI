# Generated by Django 5.1.3 on 2024-11-17 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_alter_panel_cat_delete_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel',
            name='cat',
            field=models.CharField(choices=[('Менеджер', 'Менеджер'), ('Тренер', 'Тренер'), ('Клиент', 'Клиент')], max_length=20, null=True),
        ),
    ]
