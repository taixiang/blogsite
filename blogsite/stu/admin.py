from django.contrib import admin
from .models import StuImg
from django import forms
from django.utils.safestring import mark_safe
from django.db import models


# Register your models here.


class ImageWidget2(forms.FileInput):
    template = '%(input)s<br />%(image)s'

    def __init__(self, attrs=None, template=None, width=200, height=200):
        if template is not None:
            self.template = template
        self.width = width
        self.height = height
        super(ImageWidget2, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        input_html = super(ImageWidget2, self).render(name, value, attrs)
        if hasattr(value, 'width') and hasattr(value, 'height'):

            image_html = '<img src="/upload/%s" width="60px" height="60px" />' % value.name

            output = self.template % {'input': input_html,
                                      'image': image_html}
        else:
            output = input_html
        return mark_safe(output)


class stuImgAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    formfield_overrides = {models.ImageField: {'widget': ImageWidget2}}
    search_fields = ('title',)
    list_per_page = 10


admin.site.register(StuImg, stuImgAdmin)
