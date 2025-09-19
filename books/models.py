from django.db import models
from django.shortcuts import reverse

# Create your models here.
genre_choices = (
    ("classic", "Classic"),
    ("romantic", "Romantic"),
    ("comic", "Comic"),
    ("fantasy", "Fantasy"),
    ("horror", "Horror"),
    ("educational", "Educational"),
)

book_type_choices = (
    ("hardcover", "Hard cover"),
    ("ebook", "E-Book"),
    ("audiobook", "Audiobook"),
)


class Book(models.Model):
    name = models.CharField(max_length=120)
    author_name = models.CharField(max_length=120, null=True, blank=True)
    price = models.FloatField(help_text="in US dollars $")
    genre = models.CharField(max_length=12, choices=genre_choices, default="cl")
    book_type = models.CharField(max_length=12, choices=book_type_choices, default="hc")
    pic = models.CharField(
        max_length=255,
        default='no_picture.jpg',
        help_text="Filename of the book image stored in static/images/books/"
    )

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse ('books:detail', kwargs={'pk': self.pk})
