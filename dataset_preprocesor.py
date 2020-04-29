#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

source_dir = './Dataset/chest_xray/train/PNEUMONIA/'
destination_dir_pneumonia_bacteria = './train_classifed/pneumonia_bacteria/'
destination_dir_pneumonia_virus = './train_classifed/pneumonia_virus/'

items = []
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if '.jpeg' in file:
           items.append(file)

for file in items:
    if 'bacteria' in file:                              
        os.rename(os.path.join(source_dir, file), os.path.join(destination_dir_pneumonia_bacteria, file))
    else: 
        os.rename(os.path.join(source_dir, file), os.path.join(destination_dir_pneumonia_virus, file))
