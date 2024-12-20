# Generated by Django 5.1.3 on 2024-11-11 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='eeci',
            name='cat_id',
        ),
        migrations.AddField(
            model_name='eeci',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='panel.cat'),
        ),
    ]
