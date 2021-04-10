from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import settings

class BookInfo(models.Model):
    
    class Meta:
        verbose_name = "图书信息"
        verbose_name_plural = "图书信息s"

    book_id = models.CharField(max_length=32,unique=True, verbose_name="图书编号")
    book_name = models.CharField(max_length=100, verbose_name="图书名称")
    book_author = models.CharField(max_length=100, verbose_name="作者")
    book_price = models.IntegerField(default=0,  verbose_name="价格")
    book_mess = models.CharField(max_length=100, verbose_name="图书简介")
    book_cbs = models.CharField(max_length=100, verbose_name="出版社")
    book_sl = models.IntegerField(default=0,  verbose_name="库存数量")
    op_rq = models.DateField(verbose_name="操作日期", default=timezone.now)
    bookstyle_id = models.ForeignKey('BookStyle',to_field='booksytle_id', verbose_name="图书类别", on_delete=models.DO_NOTHING)
    book_shelf = models.CharField(max_length=32, verbose_name="所在书架")
    def __str__(self):
        return self.book_name
 

class BookStyle(models.Model):
    booksytle_id = models.CharField(max_length=32, unique=True, verbose_name="类别编号")
    booksytle_name = models.CharField(max_length=32, verbose_name="类别名称")
    parent_id = models.CharField(max_length=32, verbose_name="父类别编号")

    def __str__(self):
        return self.booksytle_name
    
    class Meta:
        verbose_name = "图书类别"
        verbose_name_plural = "图书类别s"


class Reader(models.Model):

    reader_id = models.CharField(max_length=32,unique=True, verbose_name="读者编号")
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户名',on_delete=models.SET_NULL,blank=True, null=True)
    op_name = models.CharField(max_length=32, verbose_name="操作人")
    op_rq = models.DateField(verbose_name="操作日期", default=timezone.now)
    readerstype_id = models.ForeignKey('ReaderStyle',to_field='readerstyle_id', verbose_name="读者类别编号", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.reader_id
    
    class Meta:
        verbose_name = "读者"
        verbose_name_plural = "读者s"


class ReaderStyle(models.Model):
    
    class Meta:
        verbose_name = "读者类别"
        verbose_name_plural = "读者类别s"

    readerstyle_id = models.IntegerField(unique=True, verbose_name="读者类别编号")
    readerstyle_name = models.CharField(max_length=32, verbose_name="读者类别名称")
    parent_id = models.CharField(max_length=32, verbose_name="父类别编号")
    book_sl = models.IntegerField(default=0,  verbose_name="允许借书数量")
    book_ts = models.IntegerField(default=0,  verbose_name="允许借书天数")
    book_ts_renew = models.IntegerField(default=0,  verbose_name="允许续接天数")
    
    def __str__(self):
        return self.readerstyle_name


class BorrowDetail(models.Model):
    
    class Meta:
        verbose_name = "借阅明细"
        verbose_name_plural = "借阅明细s"

    borrowdetail_id = models.CharField(max_length=32, verbose_name="借阅明细编号")
    reader_id = models.ForeignKey('Reader',to_field='reader_id',default='0', verbose_name="读者编号", on_delete=models.DO_NOTHING)
    book_id = models.ForeignKey('BookInfo',to_field='book_id',default=1, verbose_name="图书编号", on_delete=models.DO_NOTHING)
    borrow_sl = models.IntegerField(default=0,  verbose_name="借阅数量")
    return_time = models.DateField(verbose_name="规定还书时间")
    borrow_time = models.DateField(verbose_name="借阅时间", default=timezone.now)


class ReturnDetail(models.Model):
    
    class Meta:
        verbose_name = "归还明细"
        verbose_name_plural = "归还明细s"

    returndetail_id = models.CharField(max_length=32, verbose_name="归还明细编号")    
    reader_id = models.ForeignKey('Reader',to_field='reader_id',default='0', verbose_name="读者编号", on_delete=models.DO_NOTHING)
    borrow_time = models.DateField(verbose_name="借阅时间", default=timezone.now)
    borrow_sl = models.IntegerField(default=0,  verbose_name="借阅数量")
    book_id = models.ForeignKey('BookInfo',to_field='book_id',default=1, verbose_name="图书编号", on_delete=models.DO_NOTHING)
    return_sl = models.IntegerField(default=0,  verbose_name="归还数量")
    return_time_ruled = models.DateField(verbose_name="规定还书时间")
    return_time_actual = models.DateField(verbose_name="实际归还时间")

class Profile(models.Model):
    class Meta:
        verbose_name = "用户详情"
        verbose_name_plural = "用户详情s"

    def __str__(self):
        return f'{self.user.username} 详情'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userdetail_name = models.CharField(max_length=32,default="", verbose_name="真实姓名")
    userdetail_sex = models.CharField(max_length=32, default="",verbose_name="性别")
    userdetail_birth = models.DateField(verbose_name="出生日期", default=timezone.now)

    userdetail_phone = models.CharField(max_length=11, default="",verbose_name="电话")
    userdetail_qq = models.CharField(max_length=15, default="",verbose_name="QQ")
    userdetail_mess = models.CharField(max_length=15, default="",verbose_name="简介")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()