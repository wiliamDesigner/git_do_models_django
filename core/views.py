from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Post




@csrf_exempt
def hello_form(request):
    html = """
    <form action="/hello/" method="POST">
        <button type="submit">Enviar POST</button>
    </form>
    """
    return HttpResponse(html)


@csrf_exempt
def hello_post(request):
    if request.method == "POST":
        return HttpResponse("Hello World")
    return HttpResponse("Use POST para ver a mensagem.")




def index(request):
    posts = Post.objects.all()
    return render(request, 'core/index.html', {
        'posts': posts
    })




def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'core/post_detail.html', {
        'post': post
    })
