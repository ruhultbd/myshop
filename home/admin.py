from django.contrib import admin
from home.models import Banner
from django.utils.html import format_html

class BannerAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img height="100" src="{}" />'.format(obj.image.url))
    image_tag.short_description = 'Banner Image'

    def link_tag(self, obj):
        return format_html('<a href="{}">Link<a/>'.format(obj.link))

    list_display = ['ordering', 'image_tag', 'title_1', 'title_2', 'link_tag', 'status', 'updated_at']
    search_fields = ['title_1', 'title_2', 'status']
    list_filter = ['status', 'created_at']
    ordering = ('ordering', 'title_1', 'title_2', 'status', 'updated_at')
    readonly_fields = ('image_tag',)

admin.site.register(Banner, BannerAdmin)
