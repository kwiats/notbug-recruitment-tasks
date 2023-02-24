from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from blog.models import Entry
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView, LoginView


class RegisterView(CreateView):
    template_name = "blog/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        response = super().form_valid(form)
        raw_password = form.cleaned_data.get("password1")

        # login user after signing up
        user = authenticate(
            username=form.cleaned_data["username"], password=raw_password
        )
        login(self.request, user)

        return response


class CustomLoginView(LoginView):
    template_name = "blog/login.html"
    form_class = AuthenticationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.info(
            self.request, f"You are now logged in as {self.request.user.username}."
        )
        return response


class CustomLogoutView(LogoutView):
    template_name = "blog/logout.html"


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = "blog/add_entry.html"
    fields = ("title", "entries")
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EntryEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Entry
    template_name = "blog/edit_entry.html"
    fields = ("title", "entries")
    success_url = "/"

    def test_func(self):
        thisArticle = self.get_object()
        if self.request.user == thisArticle.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EntryListView(ListView):
    model = Entry
    template_name = "blog/index.html"
    ordering = ["-updated_at"]


class EntryDetailView(DetailView):
    model = Entry
    template_name = "blog/entry.html"
