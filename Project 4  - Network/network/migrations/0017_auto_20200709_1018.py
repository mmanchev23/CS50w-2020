import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0016_auto_20200708_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='value',
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 10, 18, 25, 974609)),
        ),
    ]