#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 16:15:46 2023

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

import magic
import django_filters

from django.views.generic import TemplateView
from django_filters.views import FilterView
from django_transfer import TransferHttpResponse
from django.conf import settings

from .models import Dataset


class IndexView(TemplateView):
    """Home Page"""

    template_name = "repository/index.html"


class DatasetFilter(django_filters.FilterSet):
    data_type = django_filters.CharFilter(
        field_name="data_type", label="Data type", lookup_expr='icontains')
    species = django_filters.CharFilter(
        field_name="species", label="Species", lookup_expr='icontains')

    class Meta:
        model = Dataset
        fields = ['data_type', 'species']


class DataSetListView(FilterView):
    """Display SMARTER datasets"""

    filterset_class = DatasetFilter
    paginate_by = 10
    filterset_fields = ('data_type',)


def download(request, file_name):
    file_path = str(settings.SHARED_DIR / file_name)

    # https://ajrbyers.medium.com/file-mime-types-in-django-ee9531f3035b
    mimetype = magic.from_file(file_path, mime=True)

    return TransferHttpResponse(file_path, mimetype=mimetype)
