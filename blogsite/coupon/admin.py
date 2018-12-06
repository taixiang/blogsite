from django.contrib import admin

from .models import Coupon, Word, Ques, Advice

# Register your models here.

admin.site.register(Coupon)
admin.site.register(Word)
admin.site.register(Ques)
admin.site.register(Advice)
