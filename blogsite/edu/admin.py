from django.contrib import admin
from .models import ClassType, Mission, Ques, UserInfo, Result, Total, \
    Question, QuestionM, Score, WrongQues, ErrorInfo, Advice, Sentence, Content, ContentType


# 下列汉字笔画、音序、部首都对的一组是（    ）

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


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_id')
    list_filter = ('type_id',)
    search_fields = ('title',)
    list_per_page = 10


class QuestionMAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_id')
    list_filter = ('type_id',)
    search_fields = ('title',)
    list_per_page = 10


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('point', 'user_id', 'type_id')
    list_per_page = 10


class WrongAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'qId', 'answer')
    list_per_page = 10


class ErrorAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'qId', 'type_id', 'content')
    list_per_page = 10


class AdviceAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'content')
    list_per_page = 10


class SentenceAdmin(admin.ModelAdmin):
    list_display = ('content',)
    list_per_page = 10

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_per_page = 10

# admin.site.register(ClassType)
# admin.site.register(Mission, MissionAdmin)
# admin.site.register(Ques, QuesAdmin)
admin.site.register(UserInfo)
# admin.site.register(Result)
# admin.site.register(Total)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionM, QuestionMAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(WrongQues, WrongAdmin)
admin.site.register(ErrorInfo, ErrorAdmin)
admin.site.register(Advice, AdviceAdmin)
admin.site.register(Sentence, SentenceAdmin)

admin.site.register(ContentType)
admin.site.register(Content, ContentAdmin)
