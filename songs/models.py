from django.db import models


class Performer(models.Model):
    """This is the model for a Performer."""
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Song(models.Model):
    """This is the model for a song."""
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    length = models.IntegerField(default=0)
    performer = models.ForeignKey(Performer)

    def __str__(self):
        return "{} by {}.".format(self.title, self.artist)
