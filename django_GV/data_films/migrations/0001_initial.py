# Generated by Django 4.1.5 on 2023-02-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'films',
                'managed': False,
            },
        ),
    ]
