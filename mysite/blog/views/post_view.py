from django.http import HttpResponse
from django.views import generic


class PostViews(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World')