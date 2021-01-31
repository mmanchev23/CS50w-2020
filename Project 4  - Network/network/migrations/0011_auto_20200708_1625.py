import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_auto_20200708_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='total_likes',
        ),
        migrations.AddField(
            model_name='post',
            name='is_liked',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='usersliked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 8, 16, 25, 16, 475586)),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]