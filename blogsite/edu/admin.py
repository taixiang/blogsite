from django.contrib import admin
from .models import ClassType, Mission, Ques, UserInfo, Result, Total


# Register your models here.
class MissionAdmin(admin.ModelAdmin):
    list_display = ('level', 'type_id')
    list_filter = ('type_id',)
    search_fields = ('type_id',)
    list_per_page = 10


class QuesAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_id')
    list_filter = ('type_id',)
    search_fields = ('title',)
    list_per_page = 10


admin.site.register(ClassType)
admin.site.register(Mission, MissionAdmin)
admin.site.register(Ques, QuesAdmin)
admin.site.register(UserInfo)
admin.site.register(Result)
admin.site.register(Total)
