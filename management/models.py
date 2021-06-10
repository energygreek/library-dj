#from __future__ import unicode_literals

import time
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=16)
    permission = models.IntegerField(default=1)
    reader_id = models.CharField(max_length=32,unique=True, default=time.time() ,verbose_name="读者编号")


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "所有用户"


class Book(models.Model):
    book_id = models.CharField(max_length=32,unique=True, default=time.time(), verbose_name="图书编号")
    name = models.CharField(max_length=128)
    price = models.FloatField()
    author = models.CharField(max_length=128)
    publish_date = models.DateField()
    category = models.CharField(max_length=128)


    class Meta:
        ordering = ['name']
        verbose_name = "图书"
        verbose_name_plural = "所有图书"

    def __str__(self):
        return self.name


class Img(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    img = models.ImageField(upload_to='image/%Y/%m/%d/')
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['name']
        verbose_name = "封面"
        verbose_name_plural = "所有封面"

    def __str__(self):
        return self.name


class BorrowDetail(models.Model):
    
    class Meta:
        verbose_name = "借阅明细"
        verbose_name_plural = "所有借阅明细"

    reader_id = models.ForeignKey('MyUser',to_field='reader_id',default='0', verbose_name="读者编号", on_delete=models.DO_NOTHING)
    book_id = models.ForeignKey('Book',to_field='book_id',default=1, verbose_name="图书编号", on_delete=models.DO_NOTHING)

    borrow_time = models.DateField(verbose_name="借阅时间", default=timezone.now)
    borrow_sl = models.IntegerField(default=1,  verbose_name="借阅数量")
    return_time = models.DateField(verbose_name="规定还书时间")


class ReturnDetail(models.Model):
    
    class Meta:
        verbose_name = "归还明细"
        verbose_name_plural = "所有归还明细"

    reader_id = models.ForeignKey('MyUser',to_field='reader_id',default='0', verbose_name="读者编号", on_delete=models.DO_NOTHING)
    book_id = models.ForeignKey('Book',to_field='book_id',default=1, verbose_name="图书编号", on_delete=models.DO_NOTHING)

    return_time = models.DateField(verbose_name="归还时间", default=timezone.now)
    return_sl = models.IntegerField(default=1,  verbose_name="归还数量")
    return_time_ruled = models.DateField(verbose_name="规定还书时间")
    return_time_actual = models.DateField(verbose_name="实际归还时间")
