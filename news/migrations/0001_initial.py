# Generated by Django 4.1.4 on 2022-12-18 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Science and Technology', 'Science and Technology'), ('Economy', 'Economy'), ('Business', 'Business'), ('Culture', 'Culture'), ('Ideas', 'Ideas')], max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='news/images/')),
                ('article', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
