# Generated by Django 2.1.3 on 2018-11-10 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100, verbose_name='Book title')),
                ('authors_info', models.CharField(max_length=200, verbose_name='Authors info')),
                ('ISBN', models.CharField(max_length=17, verbose_name='ISBN')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]