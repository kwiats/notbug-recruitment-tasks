from django.urls import path
from blog.views import EntryView, EntryDetailView, RegisterView, LoginView


urlpatterns = [
    path("", view=EntryView, name="homepage"),
    path("edit/<int:pk>/", view=EntryDetailView),
    path("register/", view=RegisterView),
    path("login/", view=LoginView),
]
