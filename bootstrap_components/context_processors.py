#!/usr/bin/python 
#-*- coding: utf-8 -*-

""" The context_processors defined for handling the components necessities.
"""

from django.conf import settings

def common(request):
    """ Put common needed data on the context. Actually it adds:
    settings - The Django settings module.
    """
    return {
        'settings': settings,
    }
