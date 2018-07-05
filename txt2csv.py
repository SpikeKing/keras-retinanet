#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/7/5
"""

import csv

txt_file = r"/Users/wang/exercises/keras-retinanet/dataset/annotations.txt"
csv_file = r"/Users/wang/exercises/keras-retinanet/dataset/annotations.csv"

with open(txt_file, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open(csv_file, 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)
