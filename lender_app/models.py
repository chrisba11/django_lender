from django.db import models
from django.utils.timezone import now


class Book(models.Model):
    """
    Database model to create instances of books.
    """
    STATES = [
        ('in', 'Checked-In'),
        ('out', 'Checked-Out'),
    ]

    title = models.CharField(max_length=48)
    author = models.CharField(max_length=48)
    year = models.IntegerField(default=0000)
    status = models.CharField(choices=STATES, default='in', max_length=48)
    date_added = models.DateField(default=now)
    last_borrowed = models.DateField(auto_now=True)

    def __repr__(self):
        return '<Book: {} | Status: {}>'.format(self.title, self.status)

    def __str__(self):
        return 'Book: {} | Status: {}'.format(self.title, self.status)
