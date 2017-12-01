from django.contrib import admin

from .models import Performer, Song


class SongInLine(admin.StackedInline):
    model = Song


class PerformerAdmin(admin.ModelAdmin):
    """This allows an admin to see songs with a performer."""
    inlines = [SongInLine, ]


admin.site.register(Performer, PerformerAdmin)
admin.site.register(Song)
