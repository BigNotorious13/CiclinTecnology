# Generated by Django 4.2.7 on 2023-11-14 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posiciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='clv',
            field=models.PositiveIntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
