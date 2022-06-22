from django.shortcuts import render,get_object_or_404
from django.views import View

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Post
from .forms import PostForm


def wyWeb(request):
    return render(request, 'Home.html')


def wyBlog(request):
    return render(request, 'Blog.html')

def wyBlog_HTML(request):
    return render(request, 'HTML.html')
def wyBlog_CSS(request):
    return render(request, 'CSS.html')
def wyBlog_JavaScript(request):
    return render(request, 'JavaScript.html')
def wyBlog_Forum(request):
    post_list = Post.objects.all().order_by('-created_at')[:10]
    vars = {
        'post_list': post_list,
    }
    return render(request, 'Forum.html', vars)

# 接受 Form 的 POST
def post_create_view(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, 'Forum_newArticle.html', context)

# 顯示文章
class PostDetail(View):
    template_name = 'ForumPostDetail.html'
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, self.template_name, locals())