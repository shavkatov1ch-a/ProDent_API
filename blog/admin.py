from django.contrib import admin
from .models import (Tag,
                     Home,
                     Post,
                     About,
                     Service,
                     Blog)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created')
    list_display_links = ['id', 'title', 'created']


admin.site.register(Tag)
admin.site.register(Home)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Blog)


