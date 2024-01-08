from django.shortcuts import render

def index(request):
    # return render(request, 'index.html', {'name': 'Negueba'}) -> Você pode passar uma variável que será usada no 'index.html'
    return render(request, 'index.html')
