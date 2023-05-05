from django.shortcuts import render
from django.views.generic import View
from .models import MyPost


class Index(View):
    def get(self, request):
        my_posts = MyPost.objects.all()
        return render(request, 'mainapp/index.html', {'posts': my_posts})


