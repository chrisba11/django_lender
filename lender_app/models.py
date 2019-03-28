from django.db import models
from django.utils.timezone import now
from django.dispatch import receiver
from django.contrib.auth.models import User


class Book(models.Model):
    """
    Database model to create instances of books.
    """
    STATES = [
        ('in', 'Checked-In'),
        ('out', 'Checked-Out'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books',
        default=1
        )
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=48)
    description = models.CharField(
        max_length=4096,
        default='No Description Provided'
        )
    year = models.IntegerField(default=0000)
    status = models.CharField(
        choices=STATES,
        default='in',
        max_length=48
        )
    date_added = models.DateTimeField(default=now)
    last_borrowed = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return '<Book: {} | Status: {}>'.format(self.title, self.status)

    def __str__(self):
        return 'Book: {} | Status: {}'.format(self.title, self.status)
