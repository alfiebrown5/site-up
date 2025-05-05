I started this project to refresh my python scripting skills, in particular, using requests and handling errors from requests. I wanted to tackle something that would absolutely return errors, so I decided to look at a script which checks whether or not a website / URL is available, as unavailable sites would absolutely return an error that needs to be handled. 

## Installation

```
git clone https://github.com/alfiebrown5/site-up.git
cd site-up
pip3 install -r requirements.txt
```

## Using the script

Example usage:
`python3 site-up.py -f <file.csv> [optional parameters -o out-file.txt -t timeout-in-seconds (default: 10) -c optional column header (default: url)]`

The file with your URLs in must be specified with the `--file` or `-f` flag. 

The list of sites will need to be passed into the script as a CSV file. You can specify the column header for the file with the `--column-header` or `-c` flag. 

If you are experiencing issues with requests timing out, you can specify the `--timeout` or `-t` flag to change the timeout. 

If you wish to export a list of sites that are up / available, you can do so with the `--output` or `-o` flag. 