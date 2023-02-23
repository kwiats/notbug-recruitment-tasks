from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Entry(models.Model):
    title = models.CharField(_("Title of post"), max_length=50)
    entries = models.TextField(_("Entries"))
    author = models.ForeignKey(
        User, verbose_name=_("Author Post"), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Entries"
        verbose_name_plural = "Entries"
