from csv import reader
from collections import defaultdict 



def readline(file):
    with open(file) as cvsfile:
        appsreader = reader(cvsfile)
        appslist = list(appsreader)

        appsHeader = appslist[0]
        appsdata = appslist[1:]
    
    return appsHeader, appsdata

def findAverage(appsData):
    return sum(appsData)/len(appsData)

def extractColumn(key, appsData):

    columndata = [int(x[key]) for x in range(appsData)]

    return columndata


def defineDataIntervals(appsData, block):
    interval = appsData//block

    AppsData = [x*interval for x in range(1, block+1)]

    return AppsData


def dataFilter(appsData, filterRule):
    
    appDataFilter = [x for x in appsData if filterRule(x)]

    return appDataFilter

def createFrequencyTable(keylist, appsData, freqRule, updatefrq):
    freqTable = {}

    for datapoint in appsData:
        key, valid = freqRule(datapoint, keylist)
        if (valid):
            freqTable[key]+=1

    return freqTable
