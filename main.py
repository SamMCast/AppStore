#!/usr/bin/python3
from csv import reader
from collections import defaultdict 
import optparse
import os
import zipfile
import sys

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

def main():
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
        print('[-] {0} doesn\'t exit.'. format(dataFile))
        exit(2)

    if not os.access(dataFile, os.R_OK):
        print("[-] {0} access denied.". format(dataFile))
        exit(2)

    fileExt = os.path.splitext(dataFile)[-1]

    maxattempts = 1
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



if __name__ == "__main__":
    main()