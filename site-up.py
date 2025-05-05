import requests
import sys
import os
import csv

def getURLs():
#Get URLs from .csv 
    file = file.open(sys.argv[1])
    for line in file:

    print("URLs recieved")
    
def getStatusCode(res):
    res = res.split('\n')
    statusCode = res[0]
    
    return statusCode

def checkURL():

    #Make request to site
    """
    curl -I \
        -H 'User-Agent: ...' \
    
    """



    # return res.statuscode

def main():
    try:
        print("Getting URLs from CSV file...")
        urls = getURLs()
        print("We are checking...")
        for url in urls:
            statusCode = checkURL()
            print(f"{url}:{statusCode}")

        sys.exit(0)

    except Exception as e:
        print(f"An error has occured:{e}")
        sys.exit(1)




if __name__ == "__main__":
    main()