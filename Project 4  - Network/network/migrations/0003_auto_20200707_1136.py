import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_post_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='unlikes',
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 7, 11, 36, 10, 127929)),
        ),
    ]