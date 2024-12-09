from django.http import HttpResponse
from django.views import generic

from blog.models.post import Post


class PostViews(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"
    context_object_name = 'post_list'  

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = 'post' 