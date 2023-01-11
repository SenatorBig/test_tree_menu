# Generated by Django 4.1.5 on 2023-01-09 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_key', models.IntegerField()),
                ('right_key', models.IntegerField()),
                ('level', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tree_menu.menu')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tree_menu.item')),
            ],
        ),
    ]
