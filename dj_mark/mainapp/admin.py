from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import MyPost

admin.site.register(MyPost, MarkdownxModelAdmin)
