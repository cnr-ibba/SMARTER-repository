#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:53:39 2023

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

from django.db import models
from django.conf import settings


class Dataset(models.Model):
    wp = models.IntegerField(help_text="SMARTER Work Package number (ex. 4")
    task = models.CharField(
        max_length=50,
        help_text="SMARTER taks (ex 2.1)"
    )
    species = models.CharField(
        max_length=50,
        help_text="Species description"
    )
    data_type = models.CharField(
        max_length=255,
        help_text="Data description"
    )
    owner = models.CharField(
        max_length=50,
        help_text="Who owns data (ex. INRAE)"
    )
    embargo = models.BooleanField(null=True, blank=True)
    time_series = models.BooleanField(null=True, blank=True)
    individual_data = models.BooleanField(null=True, blank=True)

    # HINT: should this be an email?
    contact = models.CharField(max_length=50)
    submitted = models.BooleanField(default=False)

    filename = models.FilePathField(
        path=str(settings.SHARED_DIR),
        null=True,
        blank=True,
        unique=True,
        max_length=255
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["data_type", "owner"],
                name="dataset_datatype_owner_idx"
            )
        ]

    def __str__(self):
        return f"{self.data_type} (WP{self.wp})"
