#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 12:38:31 2023

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>

Fill Dataset by reading XLS file
"""

import pandas as pd

from django.core.management.base import BaseCommand, CommandError
from repository.models import Dataset


columnsDict = {
    'WP': 'wp',
    'Task': 'task',
    'Species': 'species',
    'Data type': 'data_type',
    'Owner': 'owner',
    'Embargo (Y/N)': 'embargo',
    'Time series data (Y/N)': 'time_series',
    'Individual data (Y/N)': 'individual_data',
    'Contact': 'contact',
    'Submitted for DB SMARTER': 'submitted'
}


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument(
            '--input',
            type=str,
            help="Source data file"
        )

    def handle(self, *args, **options):
        data = pd.read_excel(options["input"])

        for index, row in data.iterrows():
            record = {}
            for source, target in columnsDict.items():
                record[target] = row[source]

            dataset = Dataset(**record)
            print(dataset)
