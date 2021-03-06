# Generated by Django 2.1.15 on 2020-04-13 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('pluginapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu_Item',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='pluginapp_menu_item', serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='menu_items')),
                ('price', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
