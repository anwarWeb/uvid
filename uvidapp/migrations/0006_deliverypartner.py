# Generated by Django 3.0.6 on 2020-09-17 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uvidapp', '0005_jan_aushadhi_registration_application_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='deliveryPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=70)),
                ('message', models.CharField(default='', max_length=500)),
                ('driving_icence', models.ImageField(default='', upload_to='images/')),
                ('aadhar_card', models.ImageField(default='', upload_to='images/')),
                ('pan_card', models.ImageField(default='', upload_to='images/')),
            ],
        ),
    ]
