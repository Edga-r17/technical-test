# Generated by Django 4.2.16 on 2024-11-21 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=130, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RawTransaction',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=130, null=True)),
                ('company_id', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=16)),
                ('status', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField()),
                ('paid_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=16)),
                ('status', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.company')),
            ],
        ),
    ]
