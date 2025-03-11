# Generated by Django 3.2.9 on 2023-07-30 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('period', models.CharField(max_length=255)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.unit')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('period', models.CharField(max_length=255)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.topic')),
            ],
        ),
    ]
