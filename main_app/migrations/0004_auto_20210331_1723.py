# Generated by Django 3.1.7 on 2021-03-31 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210331_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('copies', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='listen',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='vinyl',
            name='stores',
            field=models.ManyToManyField(to='main_app.Store'),
        ),
    ]