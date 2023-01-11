from django.shortcuts import render


def get_menu(request, name=None):
    return render(request, "index.html")
