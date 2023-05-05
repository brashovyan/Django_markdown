from django.shortcuts import render
from django.views.generic import View
from mainapp.models import MyPost


class Index2(View):
    def get(self, request):
        my_posts = MyPost.objects.all()
        return render(request, 'secondapp/index2.html', {'posts': my_posts})

# Create your views here.
