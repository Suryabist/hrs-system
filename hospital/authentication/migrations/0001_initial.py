# Generated by Django 3.2.1 on 2021-05-24 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('device_id', models.CharField(help_text='Unique device identifier', max_length=150, null=True, verbose_name='Device ID')),
                ('last_used', models.DateTimeField(blank=True, null=True)),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital_tokens', to='core.hospitals')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
                'abstract': False,
            },
        ),
    ]
