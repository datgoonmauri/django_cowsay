from django.shortcuts import render, reverse
import subprocess
from pysay.forms import Cow_Form
from pysay.models import Cowsay


def cowsay_views(text):
    cmd = subprocess.Popen(
        ['cowsay', text],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    out, err = cmd.communicate()

    if err:
        raise err
    else:
        return out.decode().split("\n")


def index(request):
    html = 'index.html'

    if request.method == 'POST':
        form = Cow_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data['text']
            form.save()
            return render(request, html, {'form': Cow_Form(), 'text': cowsay_views(data)})
    return render(request, html, {'form': Cow_Form()})


def history(request):
    html = 'history.html'
    data = Cowsay.objects.all().order_by("-time")[:10]
    return render(request, html, {'data': data})