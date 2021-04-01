# Generated by Django 3.1.7 on 2021-03-31 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210331_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Store',
        ),
        migrations.AlterField(
            model_name='vinyl',
            name='stores',
            field=models.ManyToManyField(to='main_app.StoreTwo'),
        ),
    ]