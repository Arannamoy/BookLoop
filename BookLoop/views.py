from django.shortcuts import render


def homeView(r):
    return render(r,"index.html")