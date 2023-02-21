#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 16:15:46 2023

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""


from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Dataset


class IndexView(TemplateView):
    """Home Page"""

    template_name = "repository/index.html"


class DataSetListView(LoginRequiredMixin, ListView):
    """Display SMARTER datasets"""

    model = Dataset
    paginate_by = 8
