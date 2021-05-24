# Generated by Django 3.2.1 on 2021-05-24 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='death',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today', models.IntegerField()),
                ('total', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='discharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today', models.IntegerField()),
                ('total', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='focalperson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='HduBeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('occupied', models.IntegerField()),
                ('available', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='icu_bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('occupied', models.IntegerField()),
                ('available', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='normal_bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('occupied', models.IntegerField()),
                ('available', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OxygenCylinders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('occupied', models.IntegerField()),
                ('available', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ventilators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('occupied', models.IntegerField()),
                ('available', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='hospitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('hospital_type', models.CharField(choices=[('Government', 'Government'), ('Private', 'Private')], default='Government', max_length=10)),
                ('phone_no', models.CharField(max_length=125)),
                ('images', models.ImageField(upload_to='images')),
                ('lat', models.DecimalField(decimal_places=5, max_digits=10)),
                ('long', models.DecimalField(decimal_places=5, max_digits=10)),
                ('death', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.death')),
                ('discharge', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.discharge')),
                ('focalperson', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.focalperson')),
                ('hdu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.hdubeds')),
                ('icu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.icu_bed')),
                ('normal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.normal_bed')),
                ('oxygen_plant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.oxygencylinders')),
            ],
        ),
    ]
