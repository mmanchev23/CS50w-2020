from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20200712_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alllisting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listingid', models.IntegerField()),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('link', models.CharField(blank=True, default=None, max_length=64, null=True)),
            ],
        ),
    ]