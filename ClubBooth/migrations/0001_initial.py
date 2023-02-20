# Generated by Django 4.0.5 on 2023-02-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booth_name', models.CharField(blank=True, default='', max_length=50)),
                ('club_category', models.CharField(blank=True, default='무분류', max_length=30)),
                ('club_picture', models.ImageField(default='/iamges/club_image/default_image.jpg', upload_to='')),
                ('booth_location', models.CharField(default='XX00', max_length=5)),
                ('Introduction', models.TextField()),
            ],
        ),
    ]
