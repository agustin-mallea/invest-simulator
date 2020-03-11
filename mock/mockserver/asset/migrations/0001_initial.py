# Generated by Django 2.1.2 on 2018-10-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('SHARE', 'share'), ('CURRENCY', 'currency')], max_length=8)),
                ('buy', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sell', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]