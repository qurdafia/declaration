# Generated by Django 3.1.2 on 2020-10-08 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0002_auto_20201008_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub',
            name='acknowledge',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
        ),
        migrations.AlterField(
            model_name='sub',
            name='has_travelled',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='sub',
            name='is_contacted',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='sub',
            name='is_quarantined',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='sub',
            name='is_unwell',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
    ]
