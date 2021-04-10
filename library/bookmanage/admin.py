from django.contrib import admin

# Register your models here.

from .models import BookInfo, BookStyle, BorrowDetail, Profile, Reader, ReaderStyle, ReturnDetail

admin.site.register(BookInfo)
admin.site.register(BookStyle)
admin.site.register(ReaderStyle)
admin.site.register(ReturnDetail)
admin.site.register(BorrowDetail)
admin.site.register(Profile)
admin.site.register(Reader)