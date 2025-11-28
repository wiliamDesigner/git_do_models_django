from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
