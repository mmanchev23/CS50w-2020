import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_auto_20200708_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='like',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 8, 15, 14, 22, 106445)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 8, 15, 14, 22, 106445)),
        ),
    ]