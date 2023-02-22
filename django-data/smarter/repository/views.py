#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 16:15:46 2023

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""


from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
import django_filters

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


class DataSetListView(LoginRequiredMixin, FilterView):
    """Display SMARTER datasets"""

    filterset_class = DatasetFilter
    paginate_by = 8
    filterset_fields = ('data_type',)
