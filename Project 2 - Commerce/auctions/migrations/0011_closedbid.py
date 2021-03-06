from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_watchlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Closedbid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=64)),
                ('winner', models.CharField(max_length=64)),
                ('listingid', models.IntegerField()),
                ('winprice', models.IntegerField()),
            ],
        ),
    ]