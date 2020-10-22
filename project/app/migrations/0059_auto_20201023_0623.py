# Generated by Django 3.1.2 on 2020-10-22 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0058_auto_20201022_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrangThaiHoDan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', verbose_name='Tên trạng thái')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='Ngày tạo')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Cập nhật')),
            ],
        ),
        migrations.AddField(
            model_name='historicalhodan',
            name='status_key',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app.trangthaihodan', verbose_name='Trạng thái'),
        ),
        migrations.AddField(
            model_name='hodan',
            name='status_key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.trangthaihodan', verbose_name='Trạng thái'),
        ),
    ]
