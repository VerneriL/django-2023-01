from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Postaus


def postaukset(request):
    postaukset = Postaus.objects.all()
    context = {
        "postaukset": postaukset
    }
    return render(request, "blogi/postauslista.html", context)

def nayta_postaus(request, id):
    postaus = Postaus.objects.get(id=id)
    context = {
        "postaus": postaus
    }
    return render(request, "blogi/postaus.html", context)

def uusi_postaus(request):
    if request.method == "GET":
        return render(request, "blogi/uusi_postaus.html")
    elif request.method == "POST":
        otsikko = request.POST['otsikko']
        teksti = request.POST['teksti']
        postaus = Postaus.objects.create(
            otsikko=otsikko, 
            teksti=teksti)
        return redirect(reverse('nayta_postaus', args=(postaus.id,)))
    