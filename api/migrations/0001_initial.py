# Generated by Django 2.2.7 on 2019-12-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('api_key', models.CharField(db_index=True, max_length=32)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
