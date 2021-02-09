from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin


from .models import Post, Category

# Register your models here.
#admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Post, MarkdownxModelAdmin)
