from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_closedbid'),
    ]

    operations = [
        migrations.AddField(
            model_name='closedbid',
            name='description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='closedbid',
            name='link',
            field=models.CharField(default=None, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='closedbid',
            name='time',
            field=models.CharField(default=None, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='closedbid',
            name='title',
            field=models.CharField(default=None, max_length=64),
            preserve_default=False,
        ),
    ]