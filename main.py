#!/usr/bin/python3
import optparse
import os
import zipfile
import sys
from collections import defaultdict 
from app_store import *

def extractFile(zFile, maxattempts, passwd, filename):
    attempts = 0
    while attempts < maxattempts:
        try:
            print("--------Extracting contents from {0}------------------". format(filename))
            datafile = zFile.extractall(pwd=passwd)
            break
        except:
            if attempts == 0:
                print("Error.")
                print("------------------------------Exiting---------------------------------")
                exit(2)
            attempts_str = 'attempts'

            if attempts == 1:
                attempts_str == 'attempt'

            print("Error. You have {0} {1}". format(attempts, attempts_str))
            passwd = input("If the zip file is password protected enter the password otherwise press return: ").strip()
            passwd = str.encode(passwd)
            if not passwd:
                passwd = None
            attempts -=1

    return datafile


def checkUserInput():
    numOfargs = len(sys.argv)

    parser = optparse.OptionParser(usage="%prog -f <data filename> -p <zipfile password>")
    parser.add_option('-f', dest='dataFile', type='string', help='specifiy the a file (.zip or .csv) to gather data from.' )
    parser.add_option('-p','--password', dest='passwd', type='string', help ='password supplied for the zipfile to be looked at.')

    (options, args) = parser.parse_args()
    dataFile = options.dataFile
    passwd = options.passwd

    if(passwd == None and dataFile == None and numOfargs > 1):
        print(parser.usage)
        exit(2)

    ShouldPrompt = False

    if(dataFile == None):
        dataFile = input("Enter the name of the data file to be processed: ")
        ShouldPrompt = True
    
    if not os.path.isfile(dataFile):
        exitmessage = '[-] ' + str(dataFile) + 'doesn\'t exit.\n'
        sys.exit(exitmessage)

    if not os.access(dataFile, os.R_OK):
        exitmessage= "[-] " + str(dataFile) + " access denied.\n"
        sys.exit(exitmessage)

    fileExt = os.path.splitext(dataFile)[-1]

    maxattempts = 1

    if fileExt != '.zip' and fileExt != '.csv':
        exitmessage = "[-] Wrong file format.\n"
        sys.exit(exitmessage)
    
    else:
        if fileExt == '.zip':
            zFile = zipfile.ZipFile(dataFile)
            if ShouldPrompt == True and passwd == None:
                passwd = input("Looks like you provided a zip file, if the zip file is password protected enter the password otherwise press return: ").strip()
                passwd = str.encode(passwd)

                if not passwd:
                    passwd = None

            if ShouldPrompt == True and passwd == None or passwd != None:
                maxattempts = 5

            dataFile = extractFile(zFile, maxattempts, passwd, dataFile)

    return dataFile        


def groupbyratingtotal(datapoint, ratingList):
    """
    Classify a datapoint based on rating totals interval and returns an interval where the data point lies 

    Keyword arguments:
    datapoint  -- the data point we are considering
    ratingList -- a numerical list containing data intervals used for the purposes for classifying

    returns a tuple of the min and max interval in which the data point lies
    """
    # We are going to assume the list is sorted

    prevRate = ratingList[0]
    for rateBlock in ratingList[1:]:
        if prevRate < datapoint <= rateBlock:
            return str(prevRate)+ "-" + str(rateBlock) + " rating count" , True
        prevRate = rateBlock

    return str(prevRate), False

def main():
    #validate the user input
    dataFile = checkUserInput()

    AppHeader, mobileAppData = readData(dataFile)

    #Only consider Apps from the 



if __name__ == "__main__":
    main()