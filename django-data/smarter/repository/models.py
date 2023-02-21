#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:53:39 2023

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

from enum import Enum

from django.db import models


class EnumMixin():
    """Common methods for my Enum classes"""

    @classmethod
    def get_value(cls, member):
        """Get numerical representation of an Enum object"""

        return cls[member].value[0]

    @classmethod
    def get_value_display(cls, value):
        """Get the display value from a key"""

        if value is None:
            return None

        for el in cls:
            if el.value[0] == value:
                return el.value[1]

        raise KeyError("value %s not in %s" % (value, cls))

    @classmethod
    def get_value_by_desc(cls, value):
        """
        Get numerical representation of an Enum object by providing a
        description
        """

        if value is None:
            return None

        for el in cls:
            if el.value[1] == value:
                return el.value[0]

        raise KeyError("value '%s' not in '%s'" % (value, cls))


class SPECIES(EnumMixin, Enum):
    sheep = (0, "Sheep")
    goat = (1, "Goat")


class Dataset(models.Model):
    wp = models.IntegerField(help_text="SMARTER Work Package number (ex. 4")
    task = models.CharField(
        max_length=50,
        help_text="SMARTER taks (ex 2.1)"
    )
    species = models.SmallIntegerField(
        choices=[x.value for x in SPECIES],
        help_text="Species (Goat or Sheep)"
    )
    data_type = models.CharField(
        max_length=255,
        help_text="Data description"
    )
    owner = models.CharField(
        max_length=50,
        help_text="Who owns data (ex. INRAE)"
    )
    embargo = models.BooleanField(null=True)
    time_series = models.BooleanField(null=True)
    individual_data = models.BooleanField(null=True)
    # HINT: should this be an email?
    contact = models.CharField(max_length=50)
    submitted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.data_type} (WP{self.wp})"
