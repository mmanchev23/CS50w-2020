import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_auto_20200708_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 8, 16, 30, 28, 981445)),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_liked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersliked', to=settings.AUTH_USER_MODEL),
        ),
    ]