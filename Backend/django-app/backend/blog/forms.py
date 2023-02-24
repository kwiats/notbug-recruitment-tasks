from django import forms
from blog.models import Entry


class EntryForm(forms.Form):
    title = forms.CharField(max_length=50, required=True)
    entries = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Entry
        fields = ("title", "entries")

    def save(self, author, commit=True):
        entry = super().save(commit=False)
        entry.author = author
        if commit:
            entry.save()
        return entry
