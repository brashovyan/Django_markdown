from django.contrib.auth.models import User
from django.db import models
from markdownx.models import MarkdownxField


class MyPost(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок", help_text="Введите заголовок", null=False)
    myfield = MarkdownxField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель', null=False)
    date = models.DateTimeField(auto_now_add=True, null=False, verbose_name="Дата")
    objects = models.Manager()


