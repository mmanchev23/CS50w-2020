from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200711_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='link',
            field=models.CharField(blank=True, default='https://wallpaperaccess.com/full/1605486.jpg', max_length=64, null=True),
        ),
    ]