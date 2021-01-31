import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20200707_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 7, 17, 9, 3, 217773)),
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]