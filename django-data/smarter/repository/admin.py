#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 12:08:41 2023

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

from django.contrib import admin

from .models import Dataset


class DatasetAdmin(admin.ModelAdmin):
    list_display = (
        'data_type',
        'wp',
        'task',
        'contact',
        'submitted',
        'filename',
    )


admin.site.register(Dataset, DatasetAdmin)
