# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:36:17 2013

@author: hok1
"""

# Assuming the first line is the header, and all files have the same header
class DataFileMerger():
    def __init__(self):
        self.fileList = []
        
    def addFile(self, filename):
        self.fileList.append(filename)
        
    def extractHeader(self):
        if len(self.fileList) != 0:
            inputFile = open(self.fileList[0], 'r')
            header = inputFile.readline()
        inputFile.close()
        return header
        
    def merge(self, outputFilename):
        outputFile = open(outputFilename, 'wb')
        outputFile.write(self.extractHeader())
        for inputFilename in self.fileList:
            inputFile = open(inputFilename, 'r')
            allLines = inputFile.readlines()
            outputFile.writelines(allLines[1:])
            inputFile.close()
        outputFile.close()
        
    def clearList(self):
        self.fileList = []
        
def mergeFiles(inputFilePrefix, outputFilename):
    merger = DataFileMerger()
    mutRates = range(0, 100, 5)
    for mutRate in mutRates:
        inputFilename = inputFilePrefix+'MutRate'+str(mutRate)+'.txt'
        merger.addFile(inputFilename)
    merger.merge(outputFilename)
