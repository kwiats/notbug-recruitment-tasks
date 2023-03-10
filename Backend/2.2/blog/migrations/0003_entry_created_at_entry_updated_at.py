# Generated by Django 4.1.7 on 2023-02-24 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_entry_options_alter_entry_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="entry",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Created at"
            ),
        ),
        migrations.AddField(
            model_name="entry",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
    ]
