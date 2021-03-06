# Generated by Django 2.0.7 on 2019-01-15 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0003_auto_20190115_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dingdept',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ding_dept', to='oneid_meta.Dept'),
        ),
        migrations.AlterField(
            model_name='dinguser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='ding_user', to='oneid_meta.User', verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='posixuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='posix_user', to='oneid_meta.User', verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='user',
            name='django_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(0, '未知'), (1, '男'), (2, '女')], default=0, verbose_name='性别'),
        ),
    ]
