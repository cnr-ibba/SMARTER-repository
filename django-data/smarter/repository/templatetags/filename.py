#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:32:41 2023

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>

found here: https://stackoverflow.com/a/4046508/4385116
"""

import os

from django import template

register = template.Library()


@register.filter
def filename(value):
    return os.path.basename(value)
