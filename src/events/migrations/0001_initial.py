# Generated by Django 2.1.7 on 2019-03-27 19:50

from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('location', geoposition.fields.GeopositionField(max_length=42)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Event Type',
                'verbose_name_plural': 'Events Types',
            },
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Reporter',
                'verbose_name_plural': 'Reporters',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='events', to='events.Reporter'),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='events', to='events.EventType'),
        ),
    ]
