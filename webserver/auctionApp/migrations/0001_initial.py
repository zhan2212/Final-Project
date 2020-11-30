# Generated by Django 3.0.3 on 2020-11-30 03:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('image', models.ImageField(default='profile_images/profilepic.jpg', upload_to='profile_images')),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be valid', regex='^\\+?1?\\d{9,10}$')])),
                ('address', models.TextField()),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('rating', models.FloatField(default=0.0)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('cap_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction', to='auctionApp.Auction')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_cost', models.IntegerField(default=0.0)),
                ('item_name', models.CharField(max_length=100)),
                ('item_description', models.TextField()),
                ('item_category', models.CharField(choices=[('1', 'Fashion'), ('2', 'Electronics'), ('3', 'Motors'), ('4', 'Collectibles'), ('5', 'Home'), ('6', 'Sporting Goods'), ('7', 'Toys'), ('8', 'Business'), ('9', 'Music')], default='1', max_length=1)),
                ('condition', models.CharField(choices=[('1', 'Fair'), ('2', 'Good'), ('3', 'Very Good'), ('4', 'Great'), ('5', 'Excellent'), ('6', 'Pristine')], default='1', max_length=1)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('base_price', models.IntegerField(default=0.0)),
                ('current_price', models.IntegerField(default=0.0)),
                ('shipping_address', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('1', 'Available'), ('2', 'Payment Due'), ('3', 'Payment Complete'), ('4', 'Delivered')], default='1', max_length=20)),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items_bought', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='auctionApp.Category')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items_to_sell', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='item_images/itemimage.jpg', upload_to='item_images')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_images', to='auctionApp.Item')),
            ],
        ),
        migrations.AddField(
            model_name='auction',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auction', to='auctionApp.Item'),
        ),
    ]
