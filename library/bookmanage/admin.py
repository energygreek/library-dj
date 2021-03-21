from django.contrib import admin

# Register your models here.

from .models import BookInfo, BookStyle, BorrowDetail, Reader, ReaderStyle, ReturnDetail, UserDetail

admin.site.register(BookInfo)
admin.site.register(BookStyle)
admin.site.register(Reader)
admin.site.register(ReaderStyle)
admin.site.register(ReturnDetail)
admin.site.register(BorrowDetail)
admin.site.register(UserDetail)