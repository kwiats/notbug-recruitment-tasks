from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Entry(models.Model):
    title = models.CharField(_("Title of post"), max_length=50)
    entries = models.TextField(_("Entries"))

    created_at = models.DateTimeField(_("Created at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    author = models.ForeignKey(
        User, verbose_name=_("Author Post"), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Entries"
        verbose_name_plural = "Entries"
