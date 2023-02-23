from django.shortcuts import get_object_or_404, render
from django.views import View
from django.http import HttpResponse
from blog.models import Entry


def EntryView(request, *args, **kwargs):
    entries = Entry.objects.all()
    context = {
        "entries": entries,
    }
    return render(request, "blog/index.html", context=context)
