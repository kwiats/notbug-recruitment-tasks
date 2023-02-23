from django.urls import path
from blog.views import EntryView


urlpatterns = [
    path("", view=EntryView),
]
