# Generated by Django 4.2.16 on 2024-10-24 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
                ('salon', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=5)),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='horario.horario')),
            ],
        ),
    ]
