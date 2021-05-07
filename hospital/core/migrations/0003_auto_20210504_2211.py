# Generated by Django 3.2.1 on 2021-05-04 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_normal_bed_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitals',
            name='icu_bed',
        ),
        migrations.RemoveField(
            model_name='hospitals',
            name='normal_bed',
        ),
        migrations.RemoveField(
            model_name='hospitals',
            name='ventilators',
        ),
        migrations.AddField(
            model_name='icu_bed',
            name='hospitals',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.hospitals'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='normal_bed',
            name='hospitals',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.hospitals'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ventilators',
            name='hospitals',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.hospitals'),
            preserve_default=False,
        ),
    ]