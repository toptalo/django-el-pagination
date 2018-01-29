"""Navigation bar context processor."""

from __future__ import unicode_literals
import platform

import django
try:
    from django.urls import reverse
except:
    from django.core.urlresolvers import reverse

import el_pagination


VOICES = (
    # Name and label pairs.
    ('complete', 'Complete example'),
    ('digg', 'Digg-style'),
    ('twitter', 'Twitter-style'),
    ('onscroll', 'On scroll'),
    ('feed-wrapper', 'Feed wrapper'),
    ('multiple', 'Multiple'),
    ('callbacks', 'Callbacks'),
    ('chunks', 'On scroll/chunks'),
)


def navbar(request):
    """Generate a list of voices for the navigation bar."""
    voice_list = []
    current_path = request.path
    for name, label in VOICES:
        path = reverse(name)
        voice_list.append({
            'label': label,
            'path': path,
            'is_active': path == current_path,
        })
    return {'navbar': voice_list}


def versions(request):
    """Add to context the version numbers of relevant apps."""
    values = (
        ('Python', platform.python_version()),
        ('Django', django.get_version()),
        ('EL Pagination', el_pagination.get_version()),
    )
    return {'versions': values}
