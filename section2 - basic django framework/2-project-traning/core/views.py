from django.shortcuts import render
from .models import Produto
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    # print(dir(request))
    # print(f'Método: {request.method}')
    # print(f"Headers: {request.headers}")
    print(f"Headers: {request.headers['User-Agent']}")
    # print(dir(request.user))
    print(f'User: {request.user}')

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = 'Usuáro logado'
        print(f'Email User: {request.user.email}')

    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação web com Django Framework',
        'outros': 'Django é top',
        'logado': teste,
        'produtos': produtos,
    }

    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    # print(f'PK: {pk}')
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }

    return render(request, 'produto.html', context)

# def error404(request, exception):
#     return render(request, '404.html')

def error404(request,exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
