# Generated by Django 2.1.4 on 2019-08-07 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=177, unique=True)),
                ('summary', models.CharField(max_length=257)),
            ],
        ),
    ]
