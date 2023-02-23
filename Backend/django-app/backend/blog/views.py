from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.http import HttpResponse
from blog.models import Entry
from blog.forms import LoginUser, UserCreation
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


def EntryView(request, *args, **kwargs):
    entries = Entry.objects.all()
    context = {
        "entries": entries,
    }
    return render(request, "blog/index.html", context=context)


def EntryDetailView(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    context = {
        "entry": entry,
    }
    return render(request, "blog/entry.html", context=context)


def EntryAddedView(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    context = entry
    return render(request, "blog/add_entry.html", context=context)


def RegisterView(request):
    return render(request, "blog/register.html")


def LoginView(request):
    if request == "POST":
        form = AuthenticationForm(request, data=request.data)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("passowrd")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, username)
                return redirect("/blog/")
    form = AuthenticationForm()
    return render(request, "blog/login.html", context={"login_form": form})
