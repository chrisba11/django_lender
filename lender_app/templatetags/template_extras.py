from django.utils import timezone
from django import template


register = template.Library()


@register.filter
def get_date_string(value):
    now_aware = timezone.now()
    delta = value - now_aware

    if delta.days == 0:
        return 'Today'
    elif delta.days == 1:
        return 'Yesterday'
    elif delta.days > 1:
        return '{} days ago'.format(delta.days)
