from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20200712_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='closedbid',
            old_name='title',
            new_name='titl',
        ),
    ]