#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:32:19 2023

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>

Attempt to deal with query parameters and pagination. See
https://stackoverflow.com/a/56824200/4385116
for more information
"""

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        query[k] = v
    return query.urlencode()
