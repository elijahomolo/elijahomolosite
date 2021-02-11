from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin


from .models import Tutorial, Category

class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)} # new

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)} # new

# Register your models here.
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Category, CategoryAdmin)
