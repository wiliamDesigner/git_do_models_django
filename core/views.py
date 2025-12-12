from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


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
    else:
        return HttpResponse("Use POST para ver a mensagem.")

# View para a página inicial do site
def index(request):
    return render(request, 'core/index.html')

from django.shortcuts import render, get_object_or_404
from .models import Post

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'core/post_detail.html', {'post': post})
