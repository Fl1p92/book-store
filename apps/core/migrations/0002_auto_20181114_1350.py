# Generated by Django 2.1.3 on 2018-11-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(db_index=True, max_length=190, verbose_name='Path')),
                ('body', models.TextField(blank=True, default='', verbose_name='Body')),
                ('method', models.CharField(max_length=10, verbose_name='Method')),
                ('time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Time')),
                ('user', models.CharField(db_index=True, max_length=100, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
                'ordering': ['-time'],
            },
        ),
        migrations.AlterModelOptions(
            name='logline',
            options={'ordering': ['-logging_time'], 'verbose_name': 'Log line', 'verbose_name_plural': 'Log lines'},
        ),
        migrations.AlterField(
            model_name='logline',
            name='logging_type',
            field=models.CharField(choices=[('create', 'Create'), ('edit', 'Edit'), ('delete', 'Delete')], db_index=True, max_length=6, verbose_name='Logging type'),
        ),
    ]
