# Generated by Django 2.1.3 on 2018-11-12 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logging_time', models.DateTimeField(auto_now_add=True, verbose_name='Logging time')),
                ('logging_type', models.CharField(choices=[('create', 'Create'), ('edit', 'Edit'), ('delete', 'Delete')], db_index=True, max_length=6, verbose_name='Product color')),
                ('logging_text', models.TextField(verbose_name='Logging text')),
            ],
            options={
                'verbose_name': 'Log line',
                'verbose_name_plural': 'Log lines',
            },
        ),
    ]