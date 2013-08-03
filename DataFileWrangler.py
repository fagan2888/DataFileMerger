# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:53:31 2013

@author: hok1
"""

import csv
import re

purifyStr = lambda mystr: re.sub('[^A-Za-z0-9]+', '', mystr)

def getDataType(header):
    datatype = str
    inttypes = ['VExoStart', 'VExoEnd', 'DExoStart', 'DExoEnd', 'JExoStart',
                'JExoEnd', 'VStart', 'VStop', 'DStart', 'DStop', 'JStart',
                'JStop', 'VScore', 'DScore', 'JScore', 'MatVStart', 'MatVEnd',
                'MatDStart', 'MatDStop', 'MatJStart', 'MatJStop', 'VDexoEnd',
                'VDexoStart', 'VDnAddition', 'VDpAddition', 'DJexoEnd',
                'DJexoStart', 'DJnAddition', 'DJpAddition', 'VJDistance',
                'VJexoEnd', 'VJexoStart', 'VJnAddition', 'VJpAddition']
    booltypes = ['VSuccess', 'DSuccess', 'JSuccess', 'AllSuccess']
    if header in inttypes:
        datatype = int
    elif header in booltypes:
        datatype = bool
    return datatype

def getGeneData(filename):
    infile = open(filename, 'rb')
    reader = csv.reader(infile, delimiter='\t')
    seq_items = []
    headers = reader.next()
    headers = map(purifyStr, headers)
    for row in reader:
        seq_item = {}
        for idx in range(min(len(row), len(headers))):
            datatype = getDataType(headers[idx])
            try:
                seq_item[headers[idx]] = datatype(row[idx])
            except ValueError:
                if datatype == int:
                    seq_item[headers[idx]] = float('-inf')
                elif datatype == bool:
                    seq_item[headers[idx]] = False
                else:
                    seq_item[headers[idx]] = row[idx]
                    print 'Error: ', headers[idx] +' : ', row[idx]
        seq_items.append(seq_item)
    infile.close()
    return seq_items
    
def getFilteredGeneData(filename, fields):
    seq_items = getGeneData(filename)
    filtered_seq_items = []
    for seq_item in seq_items:
        filtered_seq_item = {}
        for field in fields:
            if seq_item.has_key(field):
                filtered_seq_item[field] = seq_item[field]
        filtered_seq_items.append(filtered_seq_item)
    return filtered_seq_items
