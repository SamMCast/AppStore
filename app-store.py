from csv import reader



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

    columndata = [x[key] for x in range(appsData)]

    return columndata


def defineDataIntervals(appsData,key, block,min_data_set=None):

    columndata = extractColumn(key, appsData)
    columndata = [float(x) for x in columndata]

    if(min_data_set==None):
        min_data_set = min(columndata)
        
    max_data_set = max(columndata)

    interval = (max_data_set - min_data_set)/block

    AppsData = [min_data_set]
    curr = 0

    while(AppsData[curr]+interval < max_data_set):
        curr+=1
        AppsData[curr]+=interval

    return AppsData


def dataFilter(appsData, filterRule):
    
    appDataFilter = [x for x in appsData if filterRule(x)]

    return appDataFilter


def extractDataProportion(freqTable, datalegnth=None):
    if(datalegnth == None):
        datalegnth = 0
        for key in freqTable:
            datalegnth += freqTable[key]
    
    for key in freqTable:
        freqTable[key]/=datalegnth
    

def extractDataPercentage(freqTable, datalegnth = None):
    
    extractDataProportion(freqTable, datalegnth)
    for key in freqTable:
        freqTable[key]*=100
    
    
def createFrequencyTable(keylist, appsData, freqRule):
    freqTable = {}

    for datapoint in appsData:
        key, valid = freqRule(datapoint, keylist)
        if (valid):
            freqTable[key]+=1

    return freqTable
