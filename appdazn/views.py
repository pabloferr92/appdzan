from django.shortcuts import render


def hello_world(request):
    return render(request, "helloworld.html")