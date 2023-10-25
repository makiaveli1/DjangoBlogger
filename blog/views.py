from django.shortcuts import render, get_list_or_404, redirect
from django.views import generic, View
from .models import Post, Comment

# Create your views here.

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
    
    
    
class PostDetail(generic.ListView):


     def get_object(self, request, *args, **kwargs):
         queryset = Post.objects.filter(status=1)
         post = get_list_or_404(queryset, slug=slug)
         comments = post.comments.filter(approved=True).order_by('created_on')
         liked = False
         if post.likes.filter(id=self.request.user.id).exists():
             liked = True
             
         return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'liked': liked})