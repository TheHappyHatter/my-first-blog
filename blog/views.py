from django.shortcuts import render
from .models import Post
from drango.utils import timezone
# Create your views here.

def post_list(request):
    p = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})