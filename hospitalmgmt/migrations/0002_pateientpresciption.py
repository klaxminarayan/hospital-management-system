# Generated by Django 3.0.6 on 2020-05-25 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalmgmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PateientPresciption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presicption', models.CharField(max_length=200)),
                ('date1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalmgmt.Appointment')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalmgmt.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalmgmt.Patient')),
            ],
        ),
    ]
