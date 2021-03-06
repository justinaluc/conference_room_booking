# Generated by Django 4.0.3 on 2022-03-23 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room_manager', '0002_alter_conferenceroom_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReserveRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('comment', models.TextField(null=True)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room_manager.conferenceroom')),
            ],
            options={
                'unique_together': {('room_id', 'date')},
            },
        ),
    ]
