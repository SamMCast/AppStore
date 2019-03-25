from csv import reader

def readData(file):
    """Process the Apps cvs file and return a tuple of the Apps header and Apps Data ."""

    with open(file) as cvsfile:
        appsreader = reader(cvsfile)
        appslist = list(appsreader)

        appsHeader = appslist[0]
        appsdata = appslist[1:]
    
    return appsHeader, appsdata

def findAverage(appsData):
    """
    computes the average of a particular data set and returns the average

    Keyword arguments:
    appsData -- the data set we wish to compute the average for
    """
    return sum(appsData)/len(appsData)

def extractColumn(key, appsData):
    """
    extracts a data set from a specified column from a larger data set and returns the extracted data set

    Keyword arguments:
    key -- the attribute to look for when extracting the data set
    appsData -- our data set
    """

    columndata = [x[key] for x in range(appsData)]

    return columndata


def defineDataIntervals(appsData,block,min_data_set=None):
    """
    divides a dataset into well-defined intervals and returns the a new dataset based on the interval blocks

    Keyword arguments:
    appsData     -- the data set
    block        -- a number specifiying how many intervals should there be
    min_data_set -- the minimun start point for the data interval 
    """

    # columndata = extractColumn(key, appsData)
    # columndata = [float(x) for x in columndata]

    if(min_data_set==None):
        min_data_set = min(appsData)

    max_data_set = max(appsData)

    interval = (max_data_set - min_data_set)/block

    AppsData = [min_data_set]
    curr = 0
    while(AppsData[curr]+interval < max_data_set):
        AppsData.append(interval)
        curr +=1

    return AppsData


def dataFilter(appsData, filterRule):
    """Filters a data set based on select criterias and returns the filtered data set

    Keyword arguments:
    appsData -- the data set to be filtered
    filterRule -- a function supplied by the user that determines how to filter the data set
    """    
    appDataFilter = [x for x in appsData if filterRule(x)]

    return appDataFilter


def extractDataProportion(freqTable, datalegnth=None):
    """
    creates a proportion table from the frequency table and optionally the data length

    Keyword arguments:
    freqTable -- a Frequency Table 
    datalength -- the length of the data set
    """
    if(datalegnth == None):
        datalegnth = 0
        for key in freqTable:
            datalegnth += freqTable[key]
    
    for key in freqTable:
        freqTable[key]/=datalegnth
    

def extractDataPercentage(freqTable, datalegnth = None):
    """
    creates a percentage table from the frequency table and optionally the data length

    Keyword arguments:
    freqTable -- a Frequency Table 
    datalength -- the length of the data set
    """   
    extractDataProportion(freqTable, datalegnth)
    for key in freqTable:
        freqTable[key]*=100
    
    
def createFrequencyTable(keylist, appsData, freqRule):
    """
    Analyzes the frequencies of particular data points from the data set and then returns frequency table

    Keyword arguments:
    keylist  -- data points that we are trying to analyze
    appsData -- the data set from which we analyze the data points
    freqRule -- a function that defines how we will analyze the frequencies of the data point from the data set
    """
    freqTable = {}

    for datapoint in appsData:
        key, valid = freqRule(datapoint, keylist)
        if (valid):
            freqTable[key]+=1

    return freqTable
