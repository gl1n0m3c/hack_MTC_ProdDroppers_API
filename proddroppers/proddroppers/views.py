from django.shortcuts import render


def start(request):
    template = "index.html"

    return render(request, template)
