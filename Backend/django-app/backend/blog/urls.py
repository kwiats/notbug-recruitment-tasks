from django.urls import path
from blog import views


urlpatterns = [
    path("", views.EntryListView.as_view(), name="homepage"),
    path("entry/add/", views.EntryCreateView.as_view(), name="entry-add"),
    path("entry/<pk>/", views.EntryDetailView.as_view(), name="entry-detail"),
    path("entry/edit/<pk>/", views.EntryEditView.as_view(), name="entry-edit"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path(
        "logout/",
        views.LogoutView.as_view(),
        name="log-out",
    ),
]
