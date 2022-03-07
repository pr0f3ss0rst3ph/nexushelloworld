from django import forms
from django.shortcuts import render
from django.http import HttpResponse


name = ""


class newHello(forms.Form):
    name = forms.CharField(label="Enter your name: ")

# Create your views here.


def index(request):
    return render(request, "index.html", {
        "name": name,
        "form": newHello()
    })


def response(request):
    if request.method == "POST":
        form = newHello(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
    return render(request, "response.html", {
        "name": name
    })
