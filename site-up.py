import requests
import sys
import argparse
import csv
import validators

#Use Chrome Mac User Agent to try and avoid blocked python requests User Agent
headers = {
     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
     }

def getURLs(file, column_header):
#Get URLs from .csv 
    try:
        with open (f"{file}","r", newline="") as f:
            reader = csv.DictReader(f)
            urls=[]
            if not column_header:
                column_header = "url"

            for row in reader:
                url = row[f"{column_header}"]
                if validators.url(url) == True:
                    urls.append(url)
                else:
                    print(f"{url} is not a valid URL! Ignoring.")
            print("URLs retrieved")
            return urls

    except Exception as e:
        print(f"Error opening the csv file: {e}")
        sys.exit(1)


def checkURLs(urls, timeout):
    to_output = []
    if not timeout:
         timeout = 10
    timeout = int(timeout)    

    for url in urls:
        try: 
            #req to URL
            res = requests.get(url, timeout=timeout, headers=headers)
        except requests.exceptions.ConnectionError:
                print(f"Could not connect to {url}, site appears down.")
                continue
        except requests.exceptions.Timeout:
                print(f"Request to {url} timed out and site appears to be down.")
                continue
        except requests.exceptions.RequestException:
                print(f"Site {url} appears down!")
                continue

        print(f"Site {url} is up and returned status code: {res.status_code}")
        to_output.append(f"{url}: {res.status_code}")
        
    return to_output
    
def writeOutput(output, file_name):
    output_file = open(file_name, 'w')
    for line in output:
        output_file.write(f"{line[0]}: {line[1]}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", metavar="\b", help="CSV File to pass into script")
    parser.add_argument("--column-header", "-c", metavar="\b", help="CSV Column Header for URL values (default: url)")
    parser.add_argument("--timeout", "-t", metavar="\b", help="Timeout in seconds (default: 10)")
    parser.add_argument("--output", "-o", metavar="Output", help="Write output to file")
    args=parser.parse_args()
    
    if args.file:
        print("Getting URLs from CSV file...")
        urls = getURLs(args.file, args.column_header)
        print("We are checking...")
        output = checkURLs(urls, args.timeout)

        if args.output:
            writeOutput(output, args.output)
        sys.exit(0)

    else:
        print("No file specified. Use: python3 site-up.py -f <file.csv> [optional args]")

if __name__ == "__main__":
    main()