import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_auto_20200708_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post_like_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 8, 16, 46, 36, 560546)),
        ),
        migrations.RemoveField(
            model_name='like',
            name='post_like_user',
        ),
        migrations.AddField(
            model_name='like',
            name='post_like_user',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 8, 16, 46, 36, 560546)),
        ),
    ]