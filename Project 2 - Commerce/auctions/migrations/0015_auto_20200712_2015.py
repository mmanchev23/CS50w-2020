from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20200712_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='closedbid',
            name='description',
        ),
        migrations.RemoveField(
            model_name='closedbid',
            name='link',
        ),
        migrations.RemoveField(
            model_name='closedbid',
            name='time',
        ),
        migrations.RemoveField(
            model_name='closedbid',
            name='titl',
        ),
    ]