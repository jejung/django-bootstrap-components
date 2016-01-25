#!/usr/bin/python 
#-*- coding: utf-8 -*-

""" The context_processors defined for handling the components necessities.
"""

from bootstrap_components.conf import settings

def commons(request):
    """ Put common needed data on the context. Actually it adds:
    settings - The Django settings object.
    """
    return {
        'settings': settings,
    }