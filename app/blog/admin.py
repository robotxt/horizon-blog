from django.contrib import admin
from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    class Meta:
        model = Blog

    list_display = ["title", "content", "published_date"]
    fieldsets = [
        ["Info", {"fields": ["title", "content", "published_date"]}],
    ]


admin.site.register(Blog, BlogAdmin)
