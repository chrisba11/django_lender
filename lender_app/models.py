from django.db import models


class Book(models.Model):
    """

    """
    STATES = [
        ('in', 'Checked-In'),
        ('out', 'Checked-Out'),
    ]

    title = models.CharField(max_length=48),
    author = models.CharField(max_length=48),
    year = models.IntegerField(max_length=4)
    status = models.CharField(choices=STATES, default='in', max_length=24)
    date_added = models.DateField(auto_now_add=True)
    last_borrowed = models.DateField(auto_now=True)

    def __repr__(self):
        return '<Book: {} | Status: {}>'.format(self.title, self.status)

    def __str__(self):
        return 'Book: {} | Status: {}'.format(self.title, self.status)
