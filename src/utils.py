#!/usr/bin/env python3
"""
Utility Methods to automate reoccurring tasks.

"""

__author__ = "Nicole Hölzl"
__version__ = "0.1.0"
__license__ = "MIT"

# --- IMPORTS ---
import os
import sys
import logging
import pandas as pd

# set log level to DEBUG
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.DEBUG)

# --- define PATH ---
data_path = "../data/"


