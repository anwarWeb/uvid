# Generated by Django 3.0.6 on 2020-09-19 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uvidapp', '0007_auto_20200917_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appoitement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(default='', max_length=70)),
                ('Date', models.DateField(default='')),
                ('gender', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone_number', models.CharField(default='', max_length=20)),
                ('symptom', models.ImageField(default='', upload_to='images/')),
            ],
        ),
    ]
