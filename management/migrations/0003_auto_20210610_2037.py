# Generated by Django 3.2.4 on 2021-06-10 12:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20160112_2031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['name'], 'verbose_name': '图书', 'verbose_name_plural': '所有图书'},
        ),
        migrations.AlterModelOptions(
            name='img',
            options={'ordering': ['name'], 'verbose_name': '封面', 'verbose_name_plural': '所有封面'},
        ),
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': '用户', 'verbose_name_plural': '所有用户'},
        ),
        migrations.AddField(
            model_name='book',
            name='book_id',
            field=models.CharField(default=1623328659.2042856, max_length=32, unique=True, verbose_name='图书编号'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='reader_id',
            field=models.CharField(default=1623328659.2037947, max_length=32, unique=True, verbose_name='读者编号'),
        ),
        migrations.AlterField(
            model_name='img',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.book'),
        ),
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(upload_to='image/%Y/%m/%d/'),
        ),
        migrations.CreateModel(
            name='ReturnDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_time', models.DateField(default=django.utils.timezone.now, verbose_name='归还时间')),
                ('return_sl', models.IntegerField(default=1, verbose_name='归还数量')),
                ('return_time_ruled', models.DateField(verbose_name='规定还书时间')),
                ('return_time_actual', models.DateField(verbose_name='实际归还时间')),
                ('book_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='management.book', to_field='book_id', verbose_name='图书编号')),
                ('reader_id', models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='management.myuser', to_field='reader_id', verbose_name='读者编号')),
            ],
            options={
                'verbose_name': '归还明细',
                'verbose_name_plural': '所有归还明细',
            },
        ),
        migrations.CreateModel(
            name='BorrowDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_time', models.DateField(default=django.utils.timezone.now, verbose_name='借阅时间')),
                ('borrow_sl', models.IntegerField(default=1, verbose_name='借阅数量')),
                ('return_time', models.DateField(verbose_name='规定还书时间')),
                ('book_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='management.book', to_field='book_id', verbose_name='图书编号')),
                ('reader_id', models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='management.myuser', to_field='reader_id', verbose_name='读者编号')),
            ],
            options={
                'verbose_name': '借阅明细',
                'verbose_name_plural': '所有借阅明细',
            },
        ),
    ]